import pandas as pd
import numpy as np

def getWM(code2File, saveDatafilePath, rawDatafilePath, wordKey):

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
    print('get WordMemory data from participant ' + f2)
       
    #hold data from all trials
    wordHold = list()
    #Extract data
    #for some reason, ps 4 has this in a diff column name? How odd.
    if 'textForWords.started' in dat.columns:
        wordDat = dat.dropna(subset=['textForWords.started'])
        wordList = wordDat.iloc[0]['textForWords.text']
    else:
        return -999, -999
    #print(wordList)
    
    #separate list items based on new line
    wordList = list(str(wordList).split(sep="\n"))
    #print(len(wordList))
    #print(wordList)
    
    for wInd in range(len(wordList)):
        holdWord = wordList[wInd].strip(' ').lower()
        holdWord = holdWord.strip('\n')
        #print(wordList[wInd])
        if wordList[wInd].strip().lower() in wordKey: 
            #print(wordList[wInd].strip().lower())
            wordHold.append(1)
        else:
            wordHold.append(0)

    return int(f2), sum(wordHold)/20