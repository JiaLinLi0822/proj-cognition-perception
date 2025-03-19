import os
import glob
import pandas as pd
import numpy as np

def getTrail(code4File, saveDatafilePath, rawDatafilePath):

    # print('Extracting Pitch Discrimination data...............')
    # print('find ' + str(len(code1Files)) + ' files')
    # os.makedirs(saveDatafilePath + 'CleanData_getTrail/', exist_ok=True)

    #read in a file & open it
    f = code4File
    # print(f)
    dat = pd.read_csv(f)
    #print(dat)

    #Get the ps ID as a string (for later saving out)
    # f2= f.replace(saveDatafilePath,'')
    # print(f2)
    f2 = f.replace(rawDatafilePath,'')
    numIdx = f2.find('_')
    f2 = f2[0:numIdx]
    print('get Trial data from participant ' + f2)

       #get num rows and columns
    nRow, nCol = dat.shape
    #print(nRow)
    #print(nCol)
    #for col in dat.columns:
    #    print(col)
    #print(dat['trialMouse.time'])
    #print('\n')
    
    #Get new list for ps
    holdIT = list()
    
    #Data will be in the 'trialMouse.time' column.
    #Get RT: last item in list in each row in this column.
    for i2 in range(0,nRow): 
        holdTimes = dat.iloc[i2]['trialMouse.time']
        #print(type(holdTimes))
        #print(holdTimes.rfind(','))
        pos1 = holdTimes.rfind(',')
        #print(holdTimes[pos1+1:len(holdTimes)-1])
        trialRT = float(holdTimes[pos1+1:len(holdTimes)-1])
        #print(trialRT)
        holdIT.append(trialRT)
    
    return int(f2), min(holdIT), np.mean(holdIT), np.median(holdIT)