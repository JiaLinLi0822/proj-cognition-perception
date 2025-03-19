
### main
import os
import glob
import pandas as pd
import numpy as np

from getSIFI import getSIFI
from getPD import getPD
from getRaven import getRaven
from getRhythm import getRhythm
from getSRT import getSRT
from getSpeech import getSpeech
from getLocalization import getLocalization
from getTrail import getTrail
from getApp import getApp
from getWM import getWM

# Set up file paths
dataPath = '/Users/lijialin/Downloads/Cognition Project/data/' # change this to your own path
keyPath = '/Users/lijialin/Downloads/Cognition Project/code/keys/' # change this to your own path

rawDatafilePath1 = dataPath + 'Perceptual Task/'
rawDatafilePath2 = dataPath + 'Cognition Task/'
rawDatafilePath3 = dataPath + 'Speech Task/'
rawDatafilePath4 = dataPath + 'Trail Making Task/'
rawDatafilePath5 = dataPath + 'App Task/'
saveDatafilePath = dataPath + 'cleanedData/'

if os.path.exists(saveDatafilePath) == False:
    os.makedirs(saveDatafilePath)

#Read all SIFI data files from the same file path above. 
code1Files = glob.glob((rawDatafilePath1 + '*_SIFI_RandomRespOrder_AttemptGratingBackto3Beeps_111022_MERGINGFINAL_*.csv'))
code2Files = glob.glob((rawDatafilePath2 +'*_Cognition2_FullCode1_*.csv'))
code3Files = glob.glob((rawDatafilePath3 +'*_SpeechDraft1Carolyn_lessNoise_*.csv'))
code4Files = glob.glob((rawDatafilePath4 +'*_trailMaking_*.csv'))
code5Files = glob.glob((rawDatafilePath5 +'*_Summary*.json'))

def extract_number_from_filename(file_path):
    file_name = file_path.split("/")[-1]  # extract file name
    number_str = file_name.split("_")[0]  # extract number string
    return int(number_str)  # convert string to integer

code1Files = sorted(code1Files, key=lambda x: extract_number_from_filename(x))
code2Files = sorted(code2Files, key=lambda x: extract_number_from_filename(x))
code3Files = sorted(code3Files, key=lambda x: extract_number_from_filename(x))
code4Files = sorted(code4Files, key=lambda x: extract_number_from_filename(x))
code5Files = sorted(code5Files, key=lambda x: extract_number_from_filename(x))

### LOAD IN KEYS FOR A FEW TASKS ###

# get the Raven scoring master list
ravPath1 = keyPath+'ravenKey.csv'
ravKey = pd.read_csv(ravPath1)
#print(ravKey)

#word master list!
wordKeyPath1 = keyPath + 'wordListForMemory.csv'
wordKey = pd.read_csv(wordKeyPath1)

#make it a list (this'll just make stuff easier.)
wordKey= wordKey['wordList'].values.tolist()

#get rid of spaces, uppercase...
for m in range(len(wordKey)):
    wordKey[m] = wordKey[m].lower().strip()
    
#get localization key
locPath1 = keyPath+'LocalizationKeyPosition.csv'
locKey = pd.read_csv(locPath1)

# Sheet for each task
psNum = 200 # number of participants
psIDList = np.arange(0, psNum)
SIFISummary = np.ones([psNum, 5]) * -999
pitchSummaryAcc = np.ones([psNum, 1]) * -999
ravenSummaryAcc = np.ones([psNum, 1]) * -999
rhythmSummaryAcc = np.ones([psNum, 2]) * -999
SRTSummary = np.ones([psNum, 6]) * -999
SpeechSummary = np.ones([psNum, 3]) * -999
LocalizationSummary = np.ones([psNum, 2]) * -999
TrialSummary = np.ones([psNum, 3]) * -999
CorsiSummary = np.ones([psNum, 1]) * -999
LNSSummary = np.ones([psNum, 4]) * -999
D2Summary = np.ones([psNum, 7]) * -999
WMSummary = np.ones([psNum, 1]) * -999

# Get SIFI, PD, Raven data
for i in range(len(code1Files)):
    code1File = code1Files[i]
    ps, SIFI_A_Acc, SIFI_V_Acc, SIFI_B_A_Acc, SIFI_B_V_Acc, SIFI_B_Acc = getSIFI(code1File, saveDatafilePath, rawDatafilePath1)
    if ps != -999:
        SIFISummary[ps][:] = SIFI_A_Acc, SIFI_V_Acc, SIFI_B_A_Acc, SIFI_B_V_Acc, SIFI_B_Acc
    
    ps, PDAcc = getPD(code1File, saveDatafilePath, rawDatafilePath1)
    if ps != -999:
        pitchSummaryAcc[ps] = PDAcc

    ps, ravAcc = getRaven(code1File, saveDatafilePath, rawDatafilePath1, ravKey)
    if ps != -999:
        ravenSummaryAcc[ps] = ravAcc

# Get Rhythm, SRT data
for i in range(len(code2Files)):
    code2File = code2Files[i]
    ps, RhythmVAcc, RhythmAAcc = getRhythm(code2File, saveDatafilePath, rawDatafilePath2)
    rhythmSummaryAcc[ps][:] = RhythmVAcc, RhythmAAcc

    ps, SRTA_median, SRTV_median, SRTB_median, SRTA_mean, SRTV_mean, SRTB_mean = getSRT(code2File, saveDatafilePath, rawDatafilePath2)
    if ps != -999:
        SRTSummary[ps][:] = SRTA_median, SRTV_median, SRTB_median, SRTA_mean, SRTV_mean, SRTB_mean

    ps, WordMemoryAcc = getWM(code2File, saveDatafilePath, rawDatafilePath2, wordKey)
    if ps != -999:
        WMSummary[ps] = WordMemoryAcc

# Get Speech, Localization data
for i in range(len(code3Files)):
    code3File = code3Files[i]
    ps, SpeechAAcc, SpeechAVAcc, Noise = getSpeech(code3File, saveDatafilePath, rawDatafilePath3)
    if ps != -999:
        SpeechSummary[ps][:] = SpeechAAcc, SpeechAVAcc, Noise

    ps, localizationDistV, localizationDistA = getLocalization(code3File, saveDatafilePath, rawDatafilePath3, locKey)
    if ps != -999:
        LocalizationSummary[ps][:] = localizationDistV, localizationDistA

# Get Trail Making data
for i in range(len(code4Files)):
    code4File = code4Files[i]
    ps, minRT, meanRT, medianRT = getTrail(code4File, saveDatafilePath, rawDatafilePath4)
    if ps != -999:
        TrialSummary[ps][:] = minRT, meanRT, medianRT

# Get App data
for i in range(len(code5Files)):
    code5File = code5Files[i]
    result = getApp(code5File, saveDatafilePath, rawDatafilePath5)
    if result == None:
        continue
    CorsiSummary[result[0][0]] = result[1][0]
    LNSSummary[result[0][0]] = result[2][0], result[2][1], result[2][2], result[2][3]
    D2Summary[result[0][0]] = result[3][0], result[3][1], result[3][2], result[3][3], result[3][4], result[3][5], result[3][6]

# bind all data together
Summary =  {'ps': psIDList,
            'SIFI_A_Acc': SIFISummary[:, 0], 'SIFI_V_Acc': SIFISummary[:, 1], 
            'SIFI_B_A_Acc': SIFISummary[:, 2], 'SIFI_B_V_Acc': SIFISummary[:, 3], 'SIFI_B_Acc': SIFISummary[:, 4],
            'pitchSummaryAcc': pitchSummaryAcc[:, 0], 
            'ravenSummaryAcc': ravenSummaryAcc[:, 0], 
            'RhythmVAcc': rhythmSummaryAcc[:, 0], 'RhythmAAcc': rhythmSummaryAcc[:, 1], 
            'SRTA_median': SRTSummary[:, 0], 'SRTV_median': SRTSummary[:, 1], 'SRTB_median': SRTSummary[:, 2], 
            'SRTA_mean': SRTSummary[:, 3], 'SRTV_mean': SRTSummary[:, 4], 'SRTB_mean': SRTSummary[:, 5], 
            'SpeechAAcc': SpeechSummary[:, 0], 'SpeechAVAcc': SpeechSummary[:, 1], 
            'Noise': SpeechSummary[:, 2], 
            'localizationDistV': LocalizationSummary[:, 0], 'localizationDistA': LocalizationSummary[:, 1],
            'minRT': TrialSummary[:, 0], 'meanRT': TrialSummary[:, 1], 'medianRT': TrialSummary[:, 2],
            'Corsi': CorsiSummary[:, 0],
            'lns_length': LNSSummary[:, 0], 'lns_hit': LNSSummary[:, 1], 'lns_miss': LNSSummary[:, 2], 'lns_hitRate': LNSSummary[:, 3],
            'd2_hit': D2Summary[:, 0], 'd2_miss': D2Summary[:, 1], 'd2_FA': D2Summary[:, 2], 'd2_CR': D2Summary[:, 3], 
            'd2_hitRate': D2Summary[:, 4], 'd2_faRate': D2Summary[:, 5], 'd2_adjHitR': D2Summary[:, 6],
            'WordMemoryAcc': WMSummary[:, 0]}

Summary = pd.DataFrame(Summary)
Summary.replace(-999, np.nan, inplace=True)
Summary = Summary.drop(Summary.index[0])
# save data
Summary.to_csv(saveDatafilePath + 'Summary.csv', index=False)
