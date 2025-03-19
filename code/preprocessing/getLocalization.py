import pandas as pd
import numpy as np
import os

def getLocalization(code3File, saveDatafilePath, rawDatafilePath, locKey):
    #read in a file & open it
    f = code3File
    # print(f)
    dat = pd.read_csv(f)
    #print(dat)
    
    #Get the ps ID as a string (for later saving out)
    # f2= f.replace(saveDatafilePath,'')
    # print(f2)
    f2 = f.replace(rawDatafilePath,'')
    numIdx = f2.find('_')
    f2 = f2[0:numIdx]
    print('get Localization data from participant ' + f2)

    os.makedirs(saveDatafilePath+'cleanLocalization', exist_ok=True )
    localizationDistV = list()
    localizationDistA = list()
    localizationEccentricity = list()

    if not ('targetSpeakerName' in dat.columns):
        for iSpkr in range(0,7):
        #WRITE OUT NAs to relevant columns, continue
            return -999, -999, -999
    else: 
        #STEP 1: EXTRACT TASK (A,V)
        holdLocA = dat.dropna(subset=['audLocalLoop.thisRepN'])
        holdLocV = dat.dropna(subset=['visualLocalLoop.thisRepN'])
        
        holdLocA = holdLocA.reset_index()
        holdLocV = holdLocV.reset_index()
        
        holdLocA = holdLocA[['targetSpeakerName','targetSpeakerEccen','targetSpkrChannel','targetVisualDegrees','visStimW','slider.response','slider.rt']]
        holdLocV = holdLocV[['targetSpeakerName','targetSpeakerEccen','targetSpkrChannel','targetVisualDegrees','visStimW','slider.response','slider.rt']]
        
        #STEP 2: POSITIONS
        #at each speaker position...
        for iSpkr in range(0,7):
            AThisSpkr = holdLocA.loc[holdLocA['targetSpkrChannel']==iSpkr]
            VThisSpkr = holdLocV.loc[holdLocV['targetSpkrChannel']==iSpkr]
            #print(iSpkr)
            #print(VThisSpkr)
            
            #average scores for each ps
            Amean = AThisSpkr['slider.response'].mean()
            Vmean = VThisSpkr['slider.response'].mean()
            #print(Amean)
            #print(Vmean)
            
            #keyLocA
            # Atrue = float(locKey.loc[locKey['targetSpkrChannel']==iSpkr, 'trueAudioLocation_proportion'])
            Atrue = float(locKey.loc[locKey['targetSpkrChannel'] == iSpkr, 'trueAudioLocation_proportion'].iloc[0])
            # Vtrue = float(locKey.loc[locKey['targetSpkrChannel']==iSpkr, 'trueVisualLocation_proportion'])
            Vtrue = float(locKey.loc[locKey['targetSpkrChannel'] == iSpkr, 'trueVisualLocation_proportion'].iloc[0])
            #print(Atrue)
            #print(Vtrue)
            
            #score distance per ps & convert to pixels
            Adist = abs(Amean - Atrue)*1890
            #print(Adist)
            Vdist = abs(Vmean - Vtrue)*1890
            #print(Vdist)
            
            #put that distance somewhere!
            localizationDistV.append(Vdist)
            localizationDistA.append(Adist)
            # localizationEccentricity.append(float(locKey.loc[locKey['targetSpkrChannel']==iSpkr, 'targetVisualDegrees']))
            localizationEccentricity.append(float(locKey.loc[locKey['targetSpkrChannel'] == iSpkr, 'targetVisualDegrees'].iloc[0]))
        
        psLocalization = {'localizationDistV': localizationDistV,\
                        'localizationDistA':localizationDistA,\
                        'localizationEccentricity':localizationEccentricity}
        psLocalization = pd.DataFrame(psLocalization)
        psLocalization.to_csv(saveDatafilePath+'cleanLocalization/'+f2+'_Localization_clean.csv',index=False)

        return int(f2), np.mean(localizationDistV), np.mean(localizationDistA)
