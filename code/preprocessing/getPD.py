import os
import glob
import pandas as pd

def getPD(code1File, saveDatafilePath, rawDatafilePath):

    # print('Extracting Pitch Discrimination data...............')
    # print('find ' + str(len(code1Files)) + ' files')
    os.makedirs(saveDatafilePath + 'CleanData_PD/', exist_ok=True)

    #read in a file & open it
    f = code1File
    # print(f)
    dat = pd.read_csv(f)
    #print(dat)
    
    #Get the ps ID as a string (for later saving out)
    # f2= f.replace(saveDatafilePath,'')
    # print(f2)
    f2 = f.replace(rawDatafilePath,'')
    numIdx = f2.find('_')
    f2 = f2[0:numIdx]
    print('get Pitch Discrimination data from participant ' + f2)
    
    #From dat, get just pitch discrim trials
    if 'cross_hold.started' in dat.columns:
        datPD = dat.dropna(subset=['cross_hold.started'])
    else:
        print('Not Found PD in participant ' + f2 + '!')
        return -999, -999
    
    datPD = datPD.reset_index()
    datPD = datPD[['toneHz1','audioFile1','toneHz2','audioFile2','cond','getResponse.keys']]
    # new
    datPD = datPD.dropna()
    #print(datPD)
    
    #create list for ps accuracy
    pitchAcc = list()
    pitchDiff = list()
    
    #loop through trials
    for pInd in range(len(datPD['toneHz1'])):
        
        #get diff in pitch for each trial (relative to 550)
        if int(datPD.iloc[pInd]['toneHz2'])== 550:
            pitchDiff.append(float(datPD.iloc[pInd]['toneHz1'])-float(datPD.iloc[pInd]['toneHz2']))
        else:
            pitchDiff.append(float(datPD.iloc[pInd]['toneHz2'])-float(datPD.iloc[pInd]['toneHz1']))
            
        #score each response as correct or not. 
        if int(datPD.iloc[pInd]['cond'])== int(datPD.iloc[pInd]['getResponse.keys']): 
            pitchAcc.append(1)
        else: 
            pitchAcc.append(0)
            

    #print(pitchAcc)
    #print(pitchDiff)
    
    datPD['pitchDiff']=pitchDiff
    datPD['pitchAcc']=pitchAcc
    
    #create data frame for overall pitch dat & save
    pDPath = saveDatafilePath + 'CleanData_PD/' + f2 + '_pitchDiscrim_perTrial_clean.csv'
    
    #save file
    datPD.to_csv(pDPath, index=False)
    
    # add accuracy to summary stats
    # pitchSummaryAcc.append(sum(pitchAcc)/len(pitchAcc))
    # print(pitchSummaryAcc)

    return int(f2), (sum(pitchAcc)/len(pitchAcc))