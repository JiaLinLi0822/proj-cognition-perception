
import os
import glob
import pandas as pd

def getRhythm(code2File, saveDatafilePath, rawDatafilePath):

    # print('Extracting Pitch Discrimination data...............')
    # print('find ' + str(len(code1Files)) + ' files')
    # os.makedirs(saveDatafilePath + 'CleanData_PD/', exist_ok=True)

    #read in a file & open it
    f = code2File
    # print(f)
    dat = pd.read_csv(f)
    #print(dat)
    
    #Get the ps ID as a string (for later saving out)
    # f2= f.replace(saveDatafilePath,'')
    # print(f2)
    f2 = f.replace(rawDatafilePath,'')
    numIdx = f2.find('_')
    f2 = f2[0:numIdx]
    print('get Rhythm data from participant ' + f2)
       
    ### NEXT TASK: RHYTHM DATA ###
    visualConds = (4, 5, 6, 7)
    audConds = (1, 2, 3)
    
    rhythmVAccStore = list()
    rhythmAAccStore = list()
    
    if 'similCat' in dat.columns:
        dat = dat.dropna(subset=['similCat'])
    else:
        return -999, -999, -999
    
    dat = dat[['similCat','rhythm','rhythm_i2','corrMatchAnswer','rhythmChoice.keys']]
    dat = dat[~ dat['similCat'].isin(['pc1', 'pc2', 'pc3', 'pc4'])]
    dat['similCat'] = pd.to_numeric(dat['similCat'])
    
    # print(dat)
    #get only VISUAL data
    rhythmVDat = dat[dat['similCat'].isin(visualConds)]
    rhythmVDat = rhythmVDat[['rhythm','rhythm_i2','corrMatchAnswer','rhythmChoice.keys']]
    rhythmVDat = rhythmVDat.reset_index()

    #score the data 
    for rInd in range(len(rhythmVDat['rhythm'])):
        if int(rhythmVDat.iloc[rInd]['corrMatchAnswer'])==int(rhythmVDat.iloc[rInd]['rhythmChoice.keys']):
            rhythmVAccStore.append(1)
        else:
            rhythmVAccStore.append(0)
    
    #print(rhythmVAccStore)
    
    #summaries ps Dat for summary stats
    # rhythmVSummaryAcc.append(sum(rhythmVAccStore)/len(rhythmVAccStore))
    #print(rhythmVSummaryAcc)
    
    #get only AUDITORY data
    rhythmADat = dat[dat['similCat'].isin(audConds)]
    rhythmADat = rhythmADat[['rhythm','rhythm_i2','corrMatchAnswer','rhythmChoice.keys']]
    rhythmADat = rhythmADat.reset_index()
    
    #Score the data 
    for rInd2 in range(len(rhythmADat['rhythm'])):
        if int(rhythmADat.iloc[rInd2]['corrMatchAnswer'])==int(rhythmADat.iloc[rInd2]['rhythmChoice.keys']):
            rhythmAAccStore.append(1)
        else:
            rhythmAAccStore.append(0)
         
    #print(rhythmAAccStore)
    #summary stat extraction A 
    # rhythmASummaryAcc.append(sum(rhythmAAccStore)/len(rhythmAAccStore))
    #print(rhythmASummaryAcc)

    return int(f2), (sum(rhythmVAccStore)/len(rhythmVAccStore)), (sum(rhythmAAccStore)/len(rhythmAAccStore))