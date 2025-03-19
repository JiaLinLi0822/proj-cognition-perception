import pandas as pd
import numpy as np

def getSRT(code2File, saveDatafilePath, rawDatafilePath):

    # print('Extracting Pitch Discrimination data...............')
    # print('find ' + str(len(code1Files)) + ' files')

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
    print('get SRT data from participant ' + f2)
       
        #hold data from all trials
    srtVhold = list()
    srtAhold = list()
    srtBhold = list()
    
    #get all SRT Data
    if 'yesHitIt.rt' in dat.columns:
        srtDat = dat.dropna(subset=['yesHitIt.rt'])
    else:
        return -999, -999, -999, -999, -999, -999, -999
    
    srtDat = srtDat.reset_index()
    srtDat = srtDat[['condFilePath','sensoryCond','stimStart','yesHitIt.keys','yesHitIt.rt']]
    #print(srtDat)
    
    
    #subset by block type
    srtADat = srtDat[srtDat['sensoryCond'].isin(list('A'))]
    srtADat = srtADat.reset_index()
    
    srtADat['yesHitIt.keys'] = srtADat['yesHitIt.keys'].astype('str')
    #print(srtADat)
    
    srtVDat = srtDat[srtDat['sensoryCond'].isin(list('V'))]
    srtVDat = srtVDat.reset_index()
    #print(srtVDat)
    
    srtBDat = srtDat[srtDat['sensoryCond'].isin(list('B'))]
    srtBDat = srtBDat.reset_index()
    #print(srtBDat)
    
    
    #Okay time to score this shit. 
    #BUT! There's a weird phenomenon with writing after the first data point? No idea why
    #Just know the first line is weird and every one after is bizarre for some reason. 
    
    #for each row...
    for sAInd in range(len(srtADat['sensoryCond'])): 
        #if the data is in the right place...
        if srtADat.iloc[sAInd]['yesHitIt.keys']=='space':
            srtAhold.append(float(srtADat.iloc[sAInd]['yesHitIt.rt']))
        #if it's not...
        else:
            srtAhold.append(float(srtADat.iloc[sAInd]['yesHitIt.keys']))
            
    #remove NANs and very long RTs. 
    cleansrtAhold = [x for x in srtAhold if str(x) != 'nan']
    # cleansrtAhold  = [float(x) for x in cleansrtAhold if float(x) < 30]
    cleansrtAhold.sort()
    #print(cleansrtAhold)
    
    #get median and mean, honestly. 
    # sRTSummaryAMedian.append(statistics.median(cleansrtAhold))
    # sRTSummaryAMean.append(sum(cleansrtAhold)/len(cleansrtAhold))
    
    #print(sRTSummaryAMedian)
    #print(sRTSummaryAMean)
    
    
    #Do the whole process again for Visual SRT trials
    for sVInd in range(len(srtVDat['sensoryCond'])):
        if srtVDat.iloc[sVInd]['yesHitIt.keys']=='space':
            srtVhold.append(float(srtVDat.iloc[sVInd]['yesHitIt.rt']))
        else:
            srtVhold.append(float(srtVDat.iloc[sVInd]['yesHitIt.keys']))
            
    cleansrtVhold = [x for x in srtVhold if str(x) != 'nan']
    # cleansrtVhold = [float(x) for x in cleansrtVhold if float(x) < 30]
    cleansrtVhold.sort()
    
    # sRTSummaryVMedian.append(statistics.median(cleansrtVhold))
    # sRTSummaryVMean.append(sum(cleansrtVhold)/len(cleansrtVhold))
    
    #print(sRTSummaryVMedian)
    #print(sRTSummaryVMean)
    
    
    #Now once more for AV (bisensory) SRT trials
    for sBInd in range(len(srtBDat['sensoryCond'])):
        if srtBDat.iloc[sBInd]['yesHitIt.keys']=='space':
            srtBhold.append(float(srtBDat.iloc[sBInd]['yesHitIt.rt']))
        else:
            srtBhold.append(float(srtBDat.iloc[sBInd]['yesHitIt.keys']))
            
    cleansrtBhold = [x for x in srtBhold if str(x) != 'nan']
    # cleansrtBhold = [float(x) for x in cleansrtBhold if float(x) < 30]
    cleansrtBhold.sort()
    
    # sRTSummaryBMedian.append(statistics.median(cleansrtBhold))
    # sRTSummaryBMean.append(sum(cleansrtBhold)/len(cleansrtBhold))
    
    #print(sRTSummaryBMedian)
    #print(sRTSummaryBMean)
    SRTA_median = np.where(len(cleansrtAhold) == 0, -999, np.median(cleansrtAhold))
    SRTV_median = np.where(len(cleansrtVhold) == 0, -999, np.median(cleansrtVhold))
    SRTB_median = np.where(len(cleansrtBhold) == 0, -999, np.median(cleansrtBhold))
    SRTA_mean = np.where(len(cleansrtAhold) == 0, -999, np.mean(cleansrtAhold))
    SRTV_mean = np.where(len(cleansrtVhold) == 0, -999, np.mean(cleansrtVhold))
    SRTB_mean = np.where(len(cleansrtBhold) == 0, -999, np.mean(cleansrtBhold))

    return int(f2), SRTA_median, SRTV_median, SRTB_median, SRTA_mean, SRTV_mean, SRTB_mean