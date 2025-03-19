
import os
import glob
import pandas as pd

def getRaven(code1File, saveDatafilePath, rawDatafilePath, ravKey):
    # print('Extracting Pitch Discrimination data...............')
    # print('find ' + str(len(code1Files)) + ' files')
    os.makedirs(saveDatafilePath + 'CleanData_Raven/', exist_ok=True)

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
    print('get Raven data from participant ' + f2)

    ravenAcc = list()
    
    #get just raven data subset
    if 'ravenProbIm.started' in dat.columns:
        datRav = dat.dropna(subset=['ravenProbIm.started'])
    else:
        print('Not Found Raven in participant ' + f2 + '!')
        return -999, -999
    datRav = datRav.reset_index()
    #print(datRav)
    
    #score each trial
    for rInd in range(len(datRav['key_resp_4.keys'])):
        if datRav.iloc[rInd]['key_resp_4.keys']==ravKey.iloc[rInd]['CorrAnswer']:
            ravenAcc.append(1)
        else: 
            ravenAcc.append(0)
    #print(ravenAcc)
              
    #add mean to summary stats
    return int(f2), (sum(ravenAcc)/len(ravenAcc))