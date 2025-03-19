import os
import glob
import pandas as pd

def getSIFI(code1File, saveDatafilePath, rawDatafilePath):
    ### DATA EXTRACTION: PER TASK, STARTING W/ SIFI EXTRACTION ###
    # print('Extracting SIFI data...............')
    # print('find ' + str(len(code1Files)) + ' files')
    os.makedirs(saveDatafilePath + 'CleanData_SIFI/', exist_ok=True)

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
    print('get SIFI data from participant ' + f2)
    
    #remove non-SIFI trials
    if 'condition' in dat.columns:
        datSF = dat.dropna(subset=['condition'])  #get only sifi
    else:
        return -999, -999, -999, -999, -999
    datSF = datSF[datSF['trialType'].isna()]  #remove practice
    #print(dat)
    #print(len(dat['session']))
    
    
    
    ### split A, V, AV blocks ###
    
    #flashRespNum is NaN--> beep only (A block)
    datAblocks = datSF[datSF['flashRespNum'].isna()]
    datAblocks = datAblocks.reset_index()
    #print(datAblocks)
    #print(len(datAblocks))
    
    #beepRespNum is NaN--> flash only (V block)
    datVblocks = datSF[datSF['beepRespNum'].isna()]
    datVblocks = datVblocks.reset_index()
    #print(datVblocks)
    #print(len(datVblocks))
    
    #Neither is NaN--> AV block
    datBblocks = datSF[~datSF['beepRespNum'].isna() & ~datSF['flashRespNum'].isna()]
    datBblocks = datBblocks.reset_index()
    #print(datBblocks)
    #print(len(datBblocks))
    
    
    ### A BLOCK: SCORE & SAVE ### 
    #score accuracy
    blockAScore = list()
    blockAAltScore = list()
    for item in range(len(datAblocks['condition'])):
        if int(datAblocks.iloc[item]['corrBeeps']) == int(datAblocks.iloc[item]['beepRespNum']): 
            blockAScore.append(1)
        else:
            blockAScore.append(0)
            
        #provide alt score
        if (int(datAblocks.iloc[item]['corrBeeps']) >= int(3)):
            #print('4 beep cond!/n')
            if (int(datAblocks.iloc[item]['beepRespNum'])>=int(3)):
                #print('4 beep is close enough/n!')
                blockAAltScore.append(1)
            else: 
                blockAAltScore.append(0)
        elif int(datAblocks.iloc[item]['corrBeeps']) == int(datAblocks.iloc[item]['beepRespNum']):
            blockAAltScore.append(1)
        else:
            blockAAltScore.append(0)
    #print(blockAScore)
    
    #add on accuracy
    datAblocks['accuracy']=blockAScore
    
    #add on alt accuracy
    datAblocks['altAccuracy']=blockAAltScore
    
    #subset data
    datAblocks = datAblocks[['condition','conditionCode','corrFlash','corrBeeps','flashRespNum','beepRespNum','accuracy','altAccuracy']]
    #print(datAblocks)
    
    #file name + path for new file
    aPath = saveDatafilePath + 'CleanData_SIFI/'+ f2 + '_SIFI_ABlock_clean.csv'
    
    #save file
    datAblocks.to_csv(aPath, index=False)
    
    
    
    ### V BLOCK: SCORE & SAVE ###
    
    #score accuracy
    blockVScore = list()
    blockVAltScore = list()
    for itemV in range(len(datVblocks['condition'])):
        if int(datVblocks.iloc[itemV]['corrFlash']) == int(datVblocks.iloc[itemV]['flashRespNum']):
            blockVScore.append(1)
        else:
            blockVScore.append(0)
            
        #provide alt score
        if (int(datVblocks.iloc[itemV]['corrFlash']) >= 3.0):
            #print('4 beep cond!/n')
            if (int(datVblocks.iloc[itemV]['flashRespNum'])>= 3.0):
                #print('4 beep is close enough/n!')
                blockVAltScore.append(1)
            else: 
                blockVAltScore.append(0)
        elif int(datVblocks.iloc[itemV]['corrFlash']) == int(datVblocks.iloc[itemV]['flashRespNum']):
            blockVAltScore.append(1)
        else: 
            blockVAltScore.append(0)

            
    #print(blockVScore)
    #add on accuracy
    datVblocks['accuracy']=blockVScore
    
    #add on alt accuracy
    datVblocks['altAccuracy']=blockVAltScore
    
    #subset data
    datVblocks = datVblocks[['condition','conditionCode','corrFlash','corrBeeps','flashRespNum','beepRespNum','accuracy', 'altAccuracy']]
    #print(datVblocks)
    
    #file name + path for new file
    vPath = saveDatafilePath + 'CleanData_SIFI/'+ f2 + '_SIFI_VisBlock_clean.csv'
    
    #save file
    datVblocks.to_csv(vPath, index=False)
    
    
    
    ### AV BLOCK: SCORE ###
    blockBScore = list()
    for itemB in range(len(datBblocks['condition'])):
        #print(int(datBblocks.iloc[itemB]['corrFlash']))
        #print(int(datBblocks.iloc[itemB]['flashRespNum']))
        #print(int(datBblocks.iloc[itemB]['corrBeeps']))
        #print(int(datBblocks.iloc[itemB]['beepRespNum']))
        if(int(datBblocks.iloc[itemB]['corrFlash']) == int(datBblocks.iloc[itemB]['flashRespNum'])) & (int(datBblocks.iloc[itemB]['corrBeeps']) == int(datBblocks.iloc[itemB]['beepRespNum'])):
            blockBScore.append(1)
            #print('yes!')
        else:
            blockBScore.append(0)
            #print(':(')
    #print(blockBScore)
    datBblocks['accuracy'] = blockBScore
    
    #subset data
    datBblocks = datBblocks[['condition','conditionCode','corrFlash','corrBeeps','flashRespNum','beepRespNum','accuracy']]
    #print(datBblocks)
    
    #file name + path for new file
    bPath = saveDatafilePath + 'CleanData_SIFI/'+ f2 + '_SIFI_BisenBlock_clean.csv'
    
    #save file
    datBblocks.to_csv(bPath, index=False)

    datBblocks_AOnly = datBblocks[datBblocks['conditionCode'].isin([1,2,3])]
    datBblocks_VOnly = datBblocks[datBblocks['conditionCode'].isin([5,10,15])]
    
    return int(f2), datAblocks['altAccuracy'].mean(), datVblocks['altAccuracy'].mean(), datBblocks_AOnly['accuracy'].mean(), datBblocks_VOnly['accuracy'].mean(), datBblocks['accuracy'].mean()