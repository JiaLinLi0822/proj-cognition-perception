import pandas as pd
import numpy as np
import os

def getSpeech(code3File, saveDatafilePath, rawDatafilePath):
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
    print('get Speech data from participant ' + f2)
    
    os.makedirs(saveDatafilePath+'cleanSpeechForRating', exist_ok=True )
    ### NEXT TASK: SCORE SPEECH ###
    
    #get all speech Data
    speechDat = dat.dropna(subset=['Original_Word_List'])
    speechDat = speechDat.reset_index()
    speechDat = speechDat[['Original_Word_List','noiseLevelCode','conditionCodes','getAnswer.text']]
    #print(speechDat)
    
    #StoreData For each PS for hand-rating
    wordAKey = list()
    wordAVKey=list()
    wordAPs = list()
    wordAVPs = list()
    overallAScoring1 = list()
    overallAVScoring1 = list()
    
    #subset further by noise level (sum w/in noise level is the goal)
    for iNoise in range(1,7):
        nLevel = float(iNoise)
        speechDatAll = speechDat[speechDat['noiseLevelCode']==nLevel]
        speechDatAV = speechDatAll[speechDatAll['conditionCodes']=='AV']
        speechDatA = speechDatAll[speechDatAll['conditionCodes']=='A']
        #print(speechDatA)
    

        #Score that word data
        wordHoldA = list()
        wordHoldAV = list()


        for wInd in range(len(speechDatA['Original_Word_List'])):

            keyWordA = speechDatA.iloc[wInd]['Original_Word_List']
            keyWordA = keyWordA.strip(' ').lower()
            
            #print(type(speechDat.iloc[wInd]['noiseLevelCode']))

            #skip practice trials
            if keyWordA == 'ash':
                continue
                
            #append word list with key word
            wordAKey.append(keyWordA)

            #clean ps answer up-- first extract each response...
            psAnsA = speechDatA.iloc[wInd]['getAnswer.text']
            #print(psAnsA)

            #...then make sure they wrote an answer *eye roll* ...
            if psAnsA!=psAnsA: 
                #print('a bad egg!')
                wordHoldA.append(0)
                wordAPs.append(' ')
                continue

            #...and finally clean up that answer    
            psAnsA = psAnsA.strip(' ').lower()
            psAnsA = psAnsA.strip('\n')
            
            #add ps ans to list
            wordAPs.append(psAnsA)

            #score that answer
            if keyWordA == psAnsA:
                wordHoldA.append(1)
            else:
                wordHoldA.append(0)
                
                
        for iAV in range(len(speechDatAV['Original_Word_List'])):
            keyWordAV = speechDatAV.iloc[iAV]['Original_Word_List']
            keyWordAV = keyWordAV.strip(' ').lower()
            #print(keyWordAV)
            #print(type(speechDat.iloc[wInd]['noiseLevelCode']))
        

            if keyWordAV == 'ash':
                continue
            #add word to a list for storage
            
            #get word for key
            wordAVKey.append(keyWordAV)
            
            
            psAnsAV = speechDatAV.iloc[iAV]['getAnswer.text']
            
            if psAnsAV!=psAnsAV:
                wordHoldAV.append(0)
                wordAVPs.append(' ')
                continue
            
            psAnsAV = psAnsAV.strip(' ').lower()
            psAnsAV = psAnsAV.strip('\n')
            
            #get ps answer txt
            wordAVPs.append(psAnsAV)
            
            if keyWordAV == psAnsAV:
                wordHoldAV.append(1)
            else:
                wordHoldAV.append(0)
        
        #print(wordHoldA)
        #print(wordHoldAV)
        overallAScoring1 = overallAScoring1+wordHoldA
        overallAVScoring1= overallAVScoring1+wordHoldAV
        
    #Create rating file for hand-rating for this data  
    toScoreDict1 = {'key1': wordAVKey,\
                    'psAnswer1': wordAVPs,\
                    'accuracyScore':overallAVScoring1}
    toScoreDict2 = {'key2': wordAKey,\
                    'psAnswer2':wordAPs,\
                    'accuracyScore':overallAScoring1}
    toScoreDf = pd.DataFrame(toScoreDict1)
    toScoreDf.to_csv(saveDatafilePath+'cleanSpeechForRating/'+f2+'_speechAcc_1_clean.csv',index=False)
    toScoreDf = pd.DataFrame(toScoreDict2)
    toScoreDf.to_csv(saveDatafilePath+'cleanSpeechForRating/'+f2+'_speechAcc_2_clean.csv',index=False)
    
    return int(f2), sum(wordHoldA)/len(wordHoldA), sum(wordHoldAV)/len(wordHoldAV), iNoise