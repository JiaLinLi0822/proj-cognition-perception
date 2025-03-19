#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Dec  6 14:45:46 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'pyo'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'SpeechDraft1Carolyn_lessNoise_PlusLocalization'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/shamslab/Desktop/CM_SpeechTask_Mach2_102422/SpeechDraft1Carolyn_lessNoise_PlusLocalization_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcomeSetup"
welcomeSetupClock = core.Clock()
'''
Speech task
This code will: 
    >read in all conditions
    >pick words for AV and A presentation
    >Assign each word a noise level
    >randomize the order of this all
    >write condition files for each ps. 

By: C Murray, 10-18-22



#IMPORT USEFUL PACKAGES
import pandas as pd
import os
import numpy as np
from numpy import random
import random


### SETUP ###
#get psID from PsychoPy
psIDStr = expInfo['participant']
psID = int(psIDStr)

#get overall list of items
path1= os.getcwd()
allPossibleTrials = pd.read_csv(path1+'/Audio_Condition_MERGED.csv')

#Set number of trials per condition
#Must be divisible by 7!!!
trialsPerCond = 70 #10 reps at each sound level
sensoryConds = ['A','AV'] 
sensoryNames = ['audio','audiovisual']

#get condition for each trial
fullCondList = sensoryConds*trialsPerCond
fullCondList.sort() #alphabetize-- All A come before AV

#set up noise levels-- match to Saul's original coding. 
protoNoiseLevels = list(range(1,8))
shuffNoiseA = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))
shuffNoiseAV = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))

#randomize the noise orders separately
random.shuffle(shuffNoiseA)
random.shuffle(shuffNoiseAV)

#org pink noise files to match proto noise levels
pinkList1 = ['Pink_Noise_1_1.wav','Pink_Noise_2_1.wav','Pink_Noise_3_1.wav',\
'Pink_Noise_4_1.wav','Pink_Noise_5_1.wav','Pink_Noise_6_1.wav','Pink_Noise_7_1.wav']
pinkList2 = ['Pink_Noise_1_2.wav','Pink_Noise_2_2.wav','Pink_Noise_3_2.wav',\
'Pink_Noise_4_2.wav','Pink_Noise_5_2.wav','Pink_Noise_6_2.wav','Pink_Noise_7_2.wav']

#Pick some words randomly for each condition. 
#(Pro: they'll also come out in a random order)
randomWordOrder = np.random.permutation(len(allPossibleTrials))
audioIndices = randomWordOrder[0:trialsPerCond]
audioVisualIndices = randomWordOrder[trialsPerCond:(len(sensoryConds)*trialsPerCond)]

#get subset of pandas df for each condition. 
audioDF = allPossibleTrials.iloc[audioIndices,]
audVisDF = allPossibleTrials.iloc[audioVisualIndices,]

#reset indices-- it should make merging a bit easier. 
audioDF=audioDF.reset_index(drop=True)
audVisDF = audVisDF.reset_index(drop=True)

#add noise level column 
audioDF['noiseLevelCode'] = shuffNoiseA
audVisDF['noiseLevelCode']= shuffNoiseAV

#concatenate for one major overall file
fullTrialList = pd.concat([audioDF,audVisDF],ignore_index=True)
fullTrialList['conditionCodes'] = fullCondList

#add pink noise columns
fullTrialList['noiseLevelFile1'] = ['i']*len(fullTrialList)
fullTrialList['noiseLevelFile2'] = ['i']*len(fullTrialList)

#for item in range(1,8): 
for item in range(1,8):
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile1'] = pinkList1[item-1]
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile2'] = pinkList2[item-1]

#it's ready to go!
#new file path
subjCondFilePath  = path1+'/'+psIDStr+'_speechCondFile.csv'

#Write out that pandas df
fullTrialList.to_csv(os.path.normpath(subjCondFilePath),index=False)

userFile = os.path.normpath(subjCondFilePath)
'''
letsGoAlready = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press space to begin',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Welcome to the experiment! \n\nYou will now be asked to listen to audio, which may or may not be accompanied by a video, and try your best to report what word is being spoken. All of the words you will be hearing are words in standard English. \n\nAfter each presentation, please type the word you heard.\n\nPress space to see examples ',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "conditionTellAll"
conditionTellAllClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "setupTrialCross"
setupTrialCrossClock = core.Clock()
fixCross = visual.TextStim(win=win, name='fixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "playTrial"
playTrialClock = core.Clock()
fixCross2 = visual.TextStim(win=win, name='fixCross2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "typeResponse"
typeResponseClock = core.Clock()
answerPrompt = visual.TextStim(win=win, name='answerPrompt',
    text='Type the word you heard:',
    font='Open Sans',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
getAnswer = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.025,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='getAnswer',
     autoLog=True,
)
goToNext = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
stretchBreakTxrt = visual.TextStim(win=win, name='stretchBreakTxrt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "setupTrialCross"
setupTrialCrossClock = core.Clock()
fixCross = visual.TextStim(win=win, name='fixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "playTrial"
playTrialClock = core.Clock()
fixCross2 = visual.TextStim(win=win, name='fixCross2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "typeResponse"
typeResponseClock = core.Clock()
answerPrompt = visual.TextStim(win=win, name='answerPrompt',
    text='Type the word you heard:',
    font='Open Sans',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
getAnswer = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.025,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='getAnswer',
     autoLog=True,
)
goToNext = keyboard.Keyboard()

# Initialize components for Routine "welcom_AudLocal"
welcom_AudLocalClock = core.Clock()
'''
Speech task
This code will: 
    >read in all conditions
    >pick words for AV and A presentation
    >Assign each word a noise level
    >randomize the order of this all
    >write condition files for each ps. 

By: C Murray, 10-18-22



#IMPORT USEFUL PACKAGES
import pandas as pd
import os
import numpy as np
from numpy import random
import random


### SETUP ###
#get psID from PsychoPy
psIDStr = expInfo['participant']
psID = int(psIDStr)

#get overall list of items
path1= os.getcwd()
allPossibleTrials = pd.read_csv(path1+'/Audio_Condition_MERGED.csv')

#Set number of trials per condition
#Must be divisible by 7!!!
trialsPerCond = 70 #10 reps at each sound level
sensoryConds = ['A','AV'] 
sensoryNames = ['audio','audiovisual']

#get condition for each trial
fullCondList = sensoryConds*trialsPerCond
fullCondList.sort() #alphabetize-- All A come before AV

#set up noise levels-- match to Saul's original coding. 
protoNoiseLevels = list(range(1,8))
shuffNoiseA = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))
shuffNoiseAV = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))

#randomize the noise orders separately
random.shuffle(shuffNoiseA)
random.shuffle(shuffNoiseAV)

#org pink noise files to match proto noise levels
pinkList1 = ['Pink_Noise_1_1.wav','Pink_Noise_2_1.wav','Pink_Noise_3_1.wav',\
'Pink_Noise_4_1.wav','Pink_Noise_5_1.wav','Pink_Noise_6_1.wav','Pink_Noise_7_1.wav']
pinkList2 = ['Pink_Noise_1_2.wav','Pink_Noise_2_2.wav','Pink_Noise_3_2.wav',\
'Pink_Noise_4_2.wav','Pink_Noise_5_2.wav','Pink_Noise_6_2.wav','Pink_Noise_7_2.wav']

#Pick some words randomly for each condition. 
#(Pro: they'll also come out in a random order)
randomWordOrder = np.random.permutation(len(allPossibleTrials))
audioIndices = randomWordOrder[0:trialsPerCond]
audioVisualIndices = randomWordOrder[trialsPerCond:(len(sensoryConds)*trialsPerCond)]

#get subset of pandas df for each condition. 
audioDF = allPossibleTrials.iloc[audioIndices,]
audVisDF = allPossibleTrials.iloc[audioVisualIndices,]

#reset indices-- it should make merging a bit easier. 
audioDF=audioDF.reset_index(drop=True)
audVisDF = audVisDF.reset_index(drop=True)

#add noise level column 
audioDF['noiseLevelCode'] = shuffNoiseA
audVisDF['noiseLevelCode']= shuffNoiseAV

#concatenate for one major overall file
fullTrialList = pd.concat([audioDF,audVisDF],ignore_index=True)
fullTrialList['conditionCodes'] = fullCondList

#add pink noise columns
fullTrialList['noiseLevelFile1'] = ['i']*len(fullTrialList)
fullTrialList['noiseLevelFile2'] = ['i']*len(fullTrialList)

#for item in range(1,8): 
for item in range(1,8):
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile1'] = pinkList1[item-1]
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile2'] = pinkList2[item-1]

#it's ready to go!
#new file path
subjCondFilePath  = path1+'/'+psIDStr+'_speechCondFile.csv'

#Write out that pandas df
fullTrialList.to_csv(os.path.normpath(subjCondFilePath),index=False)

userFile = os.path.normpath(subjCondFilePath)
'''
letsGoLocal = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='In a new task, you will be hearing a series of beeps. After each beep, you will be given a brief pause, then you will be asked to report where the sound came from, using a mouse to pick a location on a slider bar. \n\nKeep your eyes on the plus sign while you listen!(Participants do better on this task when they look at the plus sign.)\n\nPress space when you are ready to begin.',
    font='Open Sans',
    pos=(0, -.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "prepFixCross"
prepFixCrossClock = core.Clock()
prepFixTxt = visual.TextStim(win=win, name='prepFixTxt',
    text='+',
    font='Open Sans',
    pos=(0, -0.15), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "audLocalizationTrial"
audLocalizationTrialClock = core.Clock()
prepFixTxt_2 = visual.TextStim(win=win, name='prepFixTxt_2',
    text='+',
    font='Open Sans',
    pos=(0, -0.15), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "getLocalResponse"
getLocalResponseClock = core.Clock()
respPromptLocal = visual.TextStim(win=win, name='respPromptLocal',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.75, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1,2), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='white', fillColor='Red', borderColor='darkgrey', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "visSetup"
visSetupClock = core.Clock()
letsGoLocal_2 = keyboard.Keyboard()
text_7 = visual.TextStim(win=win, name='text_7',
    text='In a new task, you will be see a series of flashes. After each flash, you will be given a brief pause, then you will be asked to report where approximately you think the flash appeared, using a mouse to pick a location on a slider bar. \n\nKeep your eyes on the plus sign!(Participants do better on this task when they look at the plus sign.)\n\nPress space when you are ready to begin.',
    font='Open Sans',
    pos=(0, -.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "prepFixCross"
prepFixCrossClock = core.Clock()
prepFixTxt = visual.TextStim(win=win, name='prepFixTxt',
    text='+',
    font='Open Sans',
    pos=(0, -0.15), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "visLocalizationTrial"
visLocalizationTrialClock = core.Clock()
prepFixTxt_3 = visual.TextStim(win=win, name='prepFixTxt_3',
    text='+',
    font='Open Sans',
    pos=(0, -0.15), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
grating = visual.GratingStim(
    win=win, name='grating',units='pix', 
    tex='sin', mask='gauss',
    ori=0.0, pos=[0,0], size=(50, 50), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "getLocalResponse"
getLocalResponseClock = core.Clock()
respPromptLocal = visual.TextStim(win=win, name='respPromptLocal',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.75, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1,2), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='white', fillColor='Red', borderColor='darkgrey', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "ByeByeTime"
ByeByeTimeClock = core.Clock()
exitTxt = visual.TextStim(win=win, name='exitTxt',
    text='Thank you! You have now completed the experiment. \n\nPlease let you experimenter know you’re done. ',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcomeSetup"-------
continueRoutine = True
# update component parameters for each repeat
'''
Speech task
This code will: 
    >read in all conditions
    >pick words for AV and A presentation
    >Assign each word a noise level
    >randomize the order of this all
    >write condition files for each ps. 

By: C Murray, 10-18-22

'''

#IMPORT USEFUL PACKAGES
import pandas as pd
import os
import numpy as np
from numpy import random
import random


#get psID from PsychoPy
psIDStr = expInfo['participant']
psID = int(psIDStr)

#get overall list of items
path1= os.getcwd()
allPossibleTrials = pd.read_csv(path1+'/Audio_Condition_MERGED.csv')

#Set number of trials per condition
#Must be divisible by 6!!!
trialsPerCond = 60 #10 reps at each sound level
sensoryConds = ['A','AV'] 
sensoryNames = ['audio','audiovisual']

#get condition for each trial
fullCondList = sensoryConds*trialsPerCond
fullCondList.sort() #alphabetize-- All A come before AV

#set up noise levels-- match to Saul's original coding. 
protoNoiseLevels = list(range(1,7))
shuffNoiseA = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))
shuffNoiseAV = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))

#randomize the noise orders separately
random.shuffle(shuffNoiseA)
random.shuffle(shuffNoiseAV)

#org pink noise files to match proto noise levels
pinkList1 = ['Pink_Noise_1_1.wav','Pink_Noise_2_1.wav','Pink_Noise_3_1.wav',\
'Pink_Noise_4_1.wav','Pink_Noise_5_1.wav','Pink_Noise_6_1.wav']
pinkList2 = ['Pink_Noise_1_2.wav','Pink_Noise_2_2.wav','Pink_Noise_3_2.wav',\
'Pink_Noise_4_2.wav','Pink_Noise_5_2.wav','Pink_Noise_6_2.wav']

#Pick some words randomly for each condition. 
#(Pro: they'll also come out in a random order)
randomWordOrder = np.random.permutation(len(allPossibleTrials))
audioIndices = randomWordOrder[0:trialsPerCond]
audioVisualIndices = randomWordOrder[trialsPerCond:(len(sensoryConds)*trialsPerCond)]

#get subset of pandas df for each condition. 
audioDF = allPossibleTrials.iloc[audioIndices,]
audVisDF = allPossibleTrials.iloc[audioVisualIndices,]

#reset indices-- it should make merging a bit easier. 
audioDF=audioDF.reset_index(drop=True)
audVisDF = audVisDF.reset_index(drop=True)

#add noise level column 
audioDF['noiseLevelCode'] = shuffNoiseA
audVisDF['noiseLevelCode']= shuffNoiseAV

#concatenate for one major overall file
fullTrialList = pd.concat([audioDF,audVisDF],ignore_index=True)
fullTrialList['conditionCodes'] = fullCondList

#add pink noise columns
fullTrialList['noiseLevelFile1'] = ['i']*len(fullTrialList)
fullTrialList['noiseLevelFile2'] = ['i']*len(fullTrialList)

#for item in range(1,8): 
for item in range(1,7):
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile1'] = pinkList1[item-1]
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile2'] = pinkList2[item-1]

#it's ready to go!
#new file path
subjCondFilePath  = path1+'/'+psIDStr+'_speechCondFileFewerNoise.csv'

#Write out that pandas df
fullTrialList.to_csv(os.path.normpath(subjCondFilePath),index=False)

userFile = os.path.normpath(subjCondFilePath)
## CODE FROM SAUL TO GET PIC N PLAY ##
from pyo import * #tried originally for controlling the sound. Using import "*" imports everything
#import sounddevice as sd #see if this'll run without this line

#First I need to initialize the pyo server. This opens audio interfaces and
#allows setup of the sounddriver properties. Duples = 0 means only OUTPUT. 
#Here is where we define the number of channels. Buffersize of 256 is default
s = Server(sr=44100, nchnls=8,
buffersize=512, duplex=0).boot()
s.start()
s.stop()

#Now to the CRAZY STUFF
#pyo has a class called SfPlayer which is soundfile players
#it reads audio data from a file using one of several available interpolation types
#sampling rate matching to the server is done by default


#So here I create a PyoObject/SfPlayer instance using the (path and the list of sounds from earlier
#The reason I set for i in range 2 is to initialize it for two audio files

#sf = [SfPlayer(folder_path+list_of_sounds[0]) for i in range(2)]
sf = [SfPlayer(path1+'/'+pinkList1[0]) for i in range(2)]
#Now to define a function for playing multiple sounds in different channels
#I found this useful script/function written by someone else online a while back
# source= https://groups.google.com/g/pyo-discuss/c/ZB4gyuagtcM

'''
- voice = audio object. 
- sound = sound file
- channel = specific audio channel from the available one in your output device

This function just sets up a quick pathway using pyo sfPlayers
to play multiple sounds simuiltaneously. Theoretically, 
you could add [voice+2],sound3, channel3, to play more than two sounds
'''
'''
def pick_and_play(voice, sound1, sound2, channel1, channel2):
    sf[voice].path = folder_path + list_of_sounds[sound1]
    sf[voice+1].path = folder_path + list_of_sounds[sound2]
    sf[voice].out(channel1)
    sf[voice+1].out(channel2)
    '''
def pick_and_play(voice, sound1, sound2, channel1, channel2):
    sf[voice].path = path1+'/'+sound1
    sf[voice+1].path = path1+'/'+sound2
    sf[voice].out(channel1)
    sf[voice+1].out(channel2)

#count loops
loopCounter = 0

#del(fullTrialList, fullCondList,shuffNoiseA,shuffNoiseAV)
#del(randomWordOrder,audioIndices,audioVisualIndices,audioDF,audVisDF)

letsGoAlready.keys = []
letsGoAlready.rt = []
_letsGoAlready_allKeys = []
# keep track of which components have finished
welcomeSetupComponents = [letsGoAlready, text_2]
for thisComponent in welcomeSetupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeSetupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcomeSetup"-------
while continueRoutine:
    # get current time
    t = welcomeSetupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeSetupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *letsGoAlready* updates
    waitOnFlip = False
    if letsGoAlready.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        letsGoAlready.frameNStart = frameN  # exact frame index
        letsGoAlready.tStart = t  # local t and not account for scr refresh
        letsGoAlready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(letsGoAlready, 'tStartRefresh')  # time at next scr refresh
        letsGoAlready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(letsGoAlready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(letsGoAlready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if letsGoAlready.status == STARTED and not waitOnFlip:
        theseKeys = letsGoAlready.getKeys(keyList=['space'], waitRelease=False)
        _letsGoAlready_allKeys.extend(theseKeys)
        if len(_letsGoAlready_allKeys):
            letsGoAlready.keys = _letsGoAlready_allKeys[-1].name  # just the last key pressed
            letsGoAlready.rt = _letsGoAlready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeSetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcomeSetup"-------
for thisComponent in welcomeSetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#Now to define a function for playing multiple sounds in different channels
#I found this useful script/function written by someone else online a while back
# source= https://groups.google.com/g/pyo-discuss/c/ZB4gyuagtcM

'''
- voice = audio object. 
- sound = sound file
- channel = specific audio channel from the available one in your output device

This function just sets up a quick pathway using pyo sfPlayers
to play multiple sounds simuiltaneously. Theoretically, 
you could add [voice+2],sound3, channel3, to play more than two sounds
'''
'''
def pick_and_play(voice, sound1, sound2, channel1, channel2):
    sf[voice].path = folder_path + list_of_sounds[sound1]
    sf[voice+1].path = folder_path + list_of_sounds[sound2]
    sf[voice].out(channel1)
    sf[voice+1].out(channel2)
    
def pick_and_play(voice, sound1, sound2, channel1, channel2):
    sf[voice].path = path1+'/'+sound1
    sf[voice+1].path = path1+'/'+sound2
    sf[voice].out(channel1)
    sf[voice+1].out(channel2)

#count loops
loopCounter = 0

del(fullTrialList)
'''

del(fullTrialList, fullCondList,shuffNoiseA,shuffNoiseAV)
del(randomWordOrder,audioIndices,audioVisualIndices,audioDF,audVisDF)


#set up speech channel
s.start()
pick_and_play(0,'silence_testingAudFile.wav','noiseLevelFile2',4,5)
#Finally I stop the server after each trial
s.stop()

# check responses
if letsGoAlready.keys in ['', [], None]:  # No response was made
    letsGoAlready.keys = None
thisExp.addData('letsGoAlready.keys',letsGoAlready.keys)
if letsGoAlready.keys != None:  # we had a response
    thisExp.addData('letsGoAlready.rt', letsGoAlready.rt)
thisExp.addData('letsGoAlready.started', letsGoAlready.tStartRefresh)
thisExp.addData('letsGoAlready.stopped', letsGoAlready.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "welcomeSetup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instructions1Components = [text_3, key_resp_2]
for thisComponent in instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practiceForSpeech_CM_102722.xlsx'),
    seed=None, name='practiceTrials')
thisExp.addLoop(practiceTrials)  # add the loop to the experiment
thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial:
        exec('{} = thisPracticeTrial[paramName]'.format(paramName))

for thisPracticeTrial in practiceTrials:
    currentLoop = practiceTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "conditionTellAll"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_5.setText(InstrTextVar)
    # keep track of which components have finished
    conditionTellAllComponents = [text_5]
    for thisComponent in conditionTellAllComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    conditionTellAllClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "conditionTellAll"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = conditionTellAllClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=conditionTellAllClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in conditionTellAllComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "conditionTellAll"-------
    for thisComponent in conditionTellAllComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('text_5.started', text_5.tStartRefresh)
    practiceTrials.addData('text_5.stopped', text_5.tStopRefresh)
    
    # ------Prepare to start Routine "setupTrialCross"-------
    continueRoutine = True
    routineTimer.add(1.250000)
    # update component parameters for each repeat
    ''' 
    This code is here to get the trial setup
    for each condition.
    
    Author: C Murray, 10-18-22
    '''
    #Based on conditions, change visuals: 
    if conditionCodes=='A': #audio trials
        setVidSize=(0,0)
        setOpac=1
        #setVidSize = (360,240)
        #setOpac = 0
    else:
        setVidSize=(360,240)
        setOpac=0
        #setOpac = 1
    
    win.mouseVisible=False
    # keep track of which components have finished
    setupTrialCrossComponents = [fixCross]
    for thisComponent in setupTrialCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    setupTrialCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "setupTrialCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = setupTrialCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=setupTrialCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixCross* updates
        if fixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixCross.frameNStart = frameN  # exact frame index
            fixCross.tStart = t  # local t and not account for scr refresh
            fixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCross, 'tStartRefresh')  # time at next scr refresh
            fixCross.setAutoDraw(True)
        if fixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixCross.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                fixCross.tStop = t  # not accounting for scr refresh
                fixCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixCross, 'tStopRefresh')  # time at next scr refresh
                fixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setupTrialCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setupTrialCross"-------
    for thisComponent in setupTrialCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #start audio player in advance?
    #s.start()
    practiceTrials.addData('fixCross.started', fixCross.tStartRefresh)
    practiceTrials.addData('fixCross.stopped', fixCross.tStopRefresh)
    
    # ------Prepare to start Routine "playTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    movieToShow = visual.MovieStim3(
        win=win, name='movieToShow',
        noAudio = False,
        filename=Video_Files,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False,
        size=setVidSize,
        depth=0.0,
        )
    #PUT YOUR PICK N' PLAY HERE
    s.start()
    #play from the specified channels (2 and 4 are the flanking channels)
    #Channel 2 is on the left and Channel 4 on the Right
    #pick_and_play(0,noiseLevelFile1,noiseLevelFile2,2,4)
    #print("if we made it this far, you have executed up to pick and play")
    pick_and_play(0,noiseLevelFile1,noiseLevelFile2,4,5)
    #print(noiseLevelFile1)
    #print(noiseLevelFile2)
    #print(loopCounter)
    
    win.mouseVisible=False
    fixCross2.setOpacity(setOpac)
    # keep track of which components have finished
    playTrialComponents = [movieToShow, fixCross2]
    for thisComponent in playTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    playTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "playTrial"-------
    while continueRoutine:
        # get current time
        t = playTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=playTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movieToShow* updates
        if movieToShow.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            movieToShow.frameNStart = frameN  # exact frame index
            movieToShow.tStart = t  # local t and not account for scr refresh
            movieToShow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movieToShow, 'tStartRefresh')  # time at next scr refresh
            movieToShow.setAutoDraw(True)
        if movieToShow.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # *fixCross2* updates
        if fixCross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixCross2.frameNStart = frameN  # exact frame index
            fixCross2.tStart = t  # local t and not account for scr refresh
            fixCross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCross2, 'tStartRefresh')  # time at next scr refresh
            fixCross2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in playTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "playTrial"-------
    for thisComponent in playTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movieToShow.stop()
    #Finally I stop the server after each trial
    s.stop()
    
    #update loop counter
    loopCounter+=1
    practiceTrials.addData('fixCross2.started', fixCross2.tStartRefresh)
    practiceTrials.addData('fixCross2.stopped', fixCross2.tStopRefresh)
    # the Routine "playTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "typeResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    getAnswer.reset()
    goToNext.keys = []
    goToNext.rt = []
    _goToNext_allKeys = []
    # keep track of which components have finished
    typeResponseComponents = [answerPrompt, getAnswer, goToNext]
    for thisComponent in typeResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    typeResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "typeResponse"-------
    while continueRoutine:
        # get current time
        t = typeResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=typeResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *answerPrompt* updates
        if answerPrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answerPrompt.frameNStart = frameN  # exact frame index
            answerPrompt.tStart = t  # local t and not account for scr refresh
            answerPrompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answerPrompt, 'tStartRefresh')  # time at next scr refresh
            answerPrompt.setAutoDraw(True)
        
        # *getAnswer* updates
        if getAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            getAnswer.frameNStart = frameN  # exact frame index
            getAnswer.tStart = t  # local t and not account for scr refresh
            getAnswer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(getAnswer, 'tStartRefresh')  # time at next scr refresh
            getAnswer.setAutoDraw(True)
        
        # *goToNext* updates
        waitOnFlip = False
        if goToNext.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            goToNext.frameNStart = frameN  # exact frame index
            goToNext.tStart = t  # local t and not account for scr refresh
            goToNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goToNext, 'tStartRefresh')  # time at next scr refresh
            goToNext.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goToNext.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goToNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goToNext.status == STARTED and not waitOnFlip:
            theseKeys = goToNext.getKeys(keyList=['return'], waitRelease=False)
            _goToNext_allKeys.extend(theseKeys)
            if len(_goToNext_allKeys):
                goToNext.keys = _goToNext_allKeys[-1].name  # just the last key pressed
                goToNext.rt = _goToNext_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in typeResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "typeResponse"-------
    for thisComponent in typeResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('answerPrompt.started', answerPrompt.tStartRefresh)
    practiceTrials.addData('answerPrompt.stopped', answerPrompt.tStopRefresh)
    practiceTrials.addData('getAnswer.text',getAnswer.text)
    practiceTrials.addData('getAnswer.started', getAnswer.tStartRefresh)
    practiceTrials.addData('getAnswer.stopped', getAnswer.tStopRefresh)
    # check responses
    if goToNext.keys in ['', [], None]:  # No response was made
        goToNext.keys = None
    practiceTrials.addData('goToNext.keys',goToNext.keys)
    if goToNext.keys != None:  # we had a response
        practiceTrials.addData('goToNext.rt', goToNext.rt)
    practiceTrials.addData('goToNext.started', goToNext.tStartRefresh)
    practiceTrials.addData('goToNext.stopped', goToNext.tStopRefresh)
    # the Routine "typeResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practiceTrials'


# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
stretchBreakTxrt.setText('The rest of the task will be similar to this! It will take approximately 15 minutes to complete, so please take a break to stretch now.\n\nPress space when you are ready to begin.')
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instructions2Components = [stretchBreakTxrt, key_resp_3]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stretchBreakTxrt* updates
    if stretchBreakTxrt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stretchBreakTxrt.frameNStart = frameN  # exact frame index
        stretchBreakTxrt.tStart = t  # local t and not account for scr refresh
        stretchBreakTxrt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stretchBreakTxrt, 'tStartRefresh')  # time at next scr refresh
        stretchBreakTxrt.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stretchBreakTxrt.started', stretchBreakTxrt.tStartRefresh)
thisExp.addData('stretchBreakTxrt.stopped', stretchBreakTxrt.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(os.path.normpath(subjCondFilePath)),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "setupTrialCross"-------
    continueRoutine = True
    routineTimer.add(1.250000)
    # update component parameters for each repeat
    ''' 
    This code is here to get the trial setup
    for each condition.
    
    Author: C Murray, 10-18-22
    '''
    #Based on conditions, change visuals: 
    if conditionCodes=='A': #audio trials
        setVidSize=(0,0)
        setOpac=1
        #setVidSize = (360,240)
        #setOpac = 0
    else:
        setVidSize=(360,240)
        setOpac=0
        #setOpac = 1
    
    win.mouseVisible=False
    # keep track of which components have finished
    setupTrialCrossComponents = [fixCross]
    for thisComponent in setupTrialCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    setupTrialCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "setupTrialCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = setupTrialCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=setupTrialCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixCross* updates
        if fixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixCross.frameNStart = frameN  # exact frame index
            fixCross.tStart = t  # local t and not account for scr refresh
            fixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCross, 'tStartRefresh')  # time at next scr refresh
            fixCross.setAutoDraw(True)
        if fixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixCross.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                fixCross.tStop = t  # not accounting for scr refresh
                fixCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixCross, 'tStopRefresh')  # time at next scr refresh
                fixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setupTrialCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setupTrialCross"-------
    for thisComponent in setupTrialCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #start audio player in advance?
    #s.start()
    trials.addData('fixCross.started', fixCross.tStartRefresh)
    trials.addData('fixCross.stopped', fixCross.tStopRefresh)
    
    # ------Prepare to start Routine "playTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    movieToShow = visual.MovieStim3(
        win=win, name='movieToShow',
        noAudio = False,
        filename=Video_Files,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False,
        size=setVidSize,
        depth=0.0,
        )
    #PUT YOUR PICK N' PLAY HERE
    s.start()
    #play from the specified channels (2 and 4 are the flanking channels)
    #Channel 2 is on the left and Channel 4 on the Right
    #pick_and_play(0,noiseLevelFile1,noiseLevelFile2,2,4)
    #print("if we made it this far, you have executed up to pick and play")
    pick_and_play(0,noiseLevelFile1,noiseLevelFile2,4,5)
    #print(noiseLevelFile1)
    #print(noiseLevelFile2)
    #print(loopCounter)
    
    win.mouseVisible=False
    fixCross2.setOpacity(setOpac)
    # keep track of which components have finished
    playTrialComponents = [movieToShow, fixCross2]
    for thisComponent in playTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    playTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "playTrial"-------
    while continueRoutine:
        # get current time
        t = playTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=playTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movieToShow* updates
        if movieToShow.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            movieToShow.frameNStart = frameN  # exact frame index
            movieToShow.tStart = t  # local t and not account for scr refresh
            movieToShow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movieToShow, 'tStartRefresh')  # time at next scr refresh
            movieToShow.setAutoDraw(True)
        if movieToShow.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # *fixCross2* updates
        if fixCross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixCross2.frameNStart = frameN  # exact frame index
            fixCross2.tStart = t  # local t and not account for scr refresh
            fixCross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCross2, 'tStartRefresh')  # time at next scr refresh
            fixCross2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in playTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "playTrial"-------
    for thisComponent in playTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movieToShow.stop()
    #Finally I stop the server after each trial
    s.stop()
    
    #update loop counter
    loopCounter+=1
    trials.addData('fixCross2.started', fixCross2.tStartRefresh)
    trials.addData('fixCross2.stopped', fixCross2.tStopRefresh)
    # the Routine "playTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "typeResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    getAnswer.reset()
    goToNext.keys = []
    goToNext.rt = []
    _goToNext_allKeys = []
    # keep track of which components have finished
    typeResponseComponents = [answerPrompt, getAnswer, goToNext]
    for thisComponent in typeResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    typeResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "typeResponse"-------
    while continueRoutine:
        # get current time
        t = typeResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=typeResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *answerPrompt* updates
        if answerPrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answerPrompt.frameNStart = frameN  # exact frame index
            answerPrompt.tStart = t  # local t and not account for scr refresh
            answerPrompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answerPrompt, 'tStartRefresh')  # time at next scr refresh
            answerPrompt.setAutoDraw(True)
        
        # *getAnswer* updates
        if getAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            getAnswer.frameNStart = frameN  # exact frame index
            getAnswer.tStart = t  # local t and not account for scr refresh
            getAnswer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(getAnswer, 'tStartRefresh')  # time at next scr refresh
            getAnswer.setAutoDraw(True)
        
        # *goToNext* updates
        waitOnFlip = False
        if goToNext.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            goToNext.frameNStart = frameN  # exact frame index
            goToNext.tStart = t  # local t and not account for scr refresh
            goToNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goToNext, 'tStartRefresh')  # time at next scr refresh
            goToNext.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goToNext.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goToNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goToNext.status == STARTED and not waitOnFlip:
            theseKeys = goToNext.getKeys(keyList=['return'], waitRelease=False)
            _goToNext_allKeys.extend(theseKeys)
            if len(_goToNext_allKeys):
                goToNext.keys = _goToNext_allKeys[-1].name  # just the last key pressed
                goToNext.rt = _goToNext_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in typeResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "typeResponse"-------
    for thisComponent in typeResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('answerPrompt.started', answerPrompt.tStartRefresh)
    trials.addData('answerPrompt.stopped', answerPrompt.tStopRefresh)
    trials.addData('getAnswer.text',getAnswer.text)
    trials.addData('getAnswer.started', getAnswer.tStartRefresh)
    trials.addData('getAnswer.stopped', getAnswer.tStopRefresh)
    # check responses
    if goToNext.keys in ['', [], None]:  # No response was made
        goToNext.keys = None
    trials.addData('goToNext.keys',goToNext.keys)
    if goToNext.keys != None:  # we had a response
        trials.addData('goToNext.rt', goToNext.rt)
    trials.addData('goToNext.started', goToNext.tStartRefresh)
    trials.addData('goToNext.stopped', goToNext.tStopRefresh)
    # the Routine "typeResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "welcom_AudLocal"-------
continueRoutine = True
# update component parameters for each repeat
'''
Speech task
This code will: 
    >read in all conditions
    >pick words for AV and A presentation
    >Assign each word a noise level
    >randomize the order of this all
    >write condition files for each ps. 

By: C Murray, 10-18-22

'''

#IMPORT USEFUL PACKAGES
#import pandas as pd
#import os
#import numpy as np
#from numpy import random
#import random


#get psID from PsychoPy
psIDStr = expInfo['participant']
psID = int(psIDStr)

#get overall list of items
path1= os.getcwd()
allPossibleTrials = pd.read_csv(path1+'/localizationExp_baseConditions.csv')
'''
#Set number of trials per condition
#Must be divisible by 6!!!
trialsPerCond = 60 #10 reps at each sound level
sensoryConds = ['A','AV'] 
sensoryNames = ['audio','audiovisual']

#get condition for each trial
fullCondList = sensoryConds*trialsPerCond
fullCondList.sort() #alphabetize-- All A come before AV

#set up noise levels-- match to Saul's original coding. 
protoNoiseLevels = list(range(1,7))
shuffNoiseA = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))
shuffNoiseAV = protoNoiseLevels*int(trialsPerCond/len(protoNoiseLevels))

#randomize the noise orders separately
random.shuffle(shuffNoiseA)
random.shuffle(shuffNoiseAV)

#org pink noise files to match proto noise levels
pinkList1 = ['Pink_Noise_1_1.wav','Pink_Noise_2_1.wav','Pink_Noise_3_1.wav',\
'Pink_Noise_4_1.wav','Pink_Noise_5_1.wav','Pink_Noise_6_1.wav']
pinkList2 = ['Pink_Noise_1_2.wav','Pink_Noise_2_2.wav','Pink_Noise_3_2.wav',\
'Pink_Noise_4_2.wav','Pink_Noise_5_2.wav','Pink_Noise_6_2.wav']

#Pick some words randomly for each condition. 
#(Pro: they'll also come out in a random order)
randomWordOrder = np.random.permutation(len(allPossibleTrials))
audioIndices = randomWordOrder[0:trialsPerCond]
audioVisualIndices = randomWordOrder[trialsPerCond:(len(sensoryConds)*trialsPerCond)]

#get subset of pandas df for each condition. 
audioDF = allPossibleTrials.iloc[audioIndices,]
audVisDF = allPossibleTrials.iloc[audioVisualIndices,]

#reset indices-- it should make merging a bit easier. 
audioDF=audioDF.reset_index(drop=True)
audVisDF = audVisDF.reset_index(drop=True)

#add noise level column 
audioDF['noiseLevelCode'] = shuffNoiseA
audVisDF['noiseLevelCode']= shuffNoiseAV

#concatenate for one major overall file
fullTrialList = pd.concat([audioDF,audVisDF],ignore_index=True)
fullTrialList['conditionCodes'] = fullCondList

#add pink noise columns
fullTrialList['noiseLevelFile1'] = ['i']*len(fullTrialList)
fullTrialList['noiseLevelFile2'] = ['i']*len(fullTrialList)

#for item in range(1,8): 
for item in range(1,7):
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile1'] = pinkList1[item-1]
    fullTrialList.loc[(fullTrialList.noiseLevelCode==item),'noiseLevelFile2'] = pinkList2[item-1]

#it's ready to go!
#new file path
subjCondFilePath  = path1+'/'+psIDStr+'_speechCondFileFewerNoise.csv'

#Write out that pandas df
fullTrialList.to_csv(os.path.normpath(subjCondFilePath),index=False)

userFile = os.path.normpath(subjCondFilePath)
'''
## CODE FROM SAUL TO GET PIC N PLAY ##
#from pyo import * #tried originally for controlling the sound. Using import "*" imports everything
#import sounddevice as sd #see if this'll run without this line

#First I need to initialize the pyo server. This opens audio interfaces and
#allows setup of the sounddriver properties. Duples = 0 means only OUTPUT. 
#Here is where we define the number of channels. Buffersize of 256 is default
#s = Server(sr=44100, nchnls=8,
#buffersize=256, duplex=0).boot()
#s.start()
#s.stop()

#Now to the CRAZY STUFF
#pyo has a class called SfPlayer which is soundfile players
#it reads audio data from a file using one of several available interpolation types
#sampling rate matching to the server is done by default


#So here I create a PyoObject/SfPlayer instance using the (path and the list of sounds from earlier
#The reason I set for i in range 2 is to initialize it for two audio files

#sf = [SfPlayer(folder_path+list_of_sounds[0]) for i in range(2)]
#sf = [SfPlayer(path1+'/'+'ch2Sound_localizationTask.wav') for i in range(2)]
#Now to define a function for playing multiple sounds in different channels
#I found this useful script/function written by someone else online a while back
# source= https://groups.google.com/g/pyo-discuss/c/ZB4gyuagtcM

'''
- voice = audio object. 
- sound = sound file
- channel = specific audio channel from the available one in your output device

This function just sets up a quick pathway using pyo sfPlayers
to play multiple sounds simuiltaneously. Theoretically, 
you could add [voice+2],sound3, channel3, to play more than two sounds
'''
'''
def pick_and_play(voice, sound1, sound2, channel1, channel2):
    sf[voice].path = folder_path + list_of_sounds[sound1]
    sf[voice+1].path = folder_path + list_of_sounds[sound2]
    sf[voice].out(channel1)
    sf[voice+1].out(channel2)
    '''
def pick_and_play(voice, sound1, channel1):
    sf[voice].path = path1+'/'+sound1
    #sf[voice+1].path = path1+'/'+sound2
    sf[voice].out(channel1)
    #sf[voice+1].out(channel2)

#count loops
loopCounter = 0

#del(fullTrialList)
letsGoLocal.keys = []
letsGoLocal.rt = []
_letsGoLocal_allKeys = []
# keep track of which components have finished
welcom_AudLocalComponents = [letsGoLocal, text_4]
for thisComponent in welcom_AudLocalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcom_AudLocalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcom_AudLocal"-------
while continueRoutine:
    # get current time
    t = welcom_AudLocalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcom_AudLocalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *letsGoLocal* updates
    waitOnFlip = False
    if letsGoLocal.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        letsGoLocal.frameNStart = frameN  # exact frame index
        letsGoLocal.tStart = t  # local t and not account for scr refresh
        letsGoLocal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(letsGoLocal, 'tStartRefresh')  # time at next scr refresh
        letsGoLocal.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(letsGoLocal.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(letsGoLocal.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if letsGoLocal.status == STARTED and not waitOnFlip:
        theseKeys = letsGoLocal.getKeys(keyList=['space'], waitRelease=False)
        _letsGoLocal_allKeys.extend(theseKeys)
        if len(_letsGoLocal_allKeys):
            letsGoLocal.keys = _letsGoLocal_allKeys[-1].name  # just the last key pressed
            letsGoLocal.rt = _letsGoLocal_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcom_AudLocalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcom_AudLocal"-------
for thisComponent in welcom_AudLocalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#Now to define a function for playing multiple sounds in different channels
#I found this useful script/function written by someone else online a while back
# source= https://groups.google.com/g/pyo-discuss/c/ZB4gyuagtcM

'''
- voice = audio object. 
- sound = sound file
- channel = specific audio channel from the available one in your output device

This function just sets up a quick pathway using pyo sfPlayers
to play multiple sounds simuiltaneously. Theoretically, 
you could add [voice+2],sound3, channel3, to play more than two sounds
'''
'''
def pick_and_play(voice, sound1, sound2, channel1, channel2):
    sf[voice].path = folder_path + list_of_sounds[sound1]
    sf[voice+1].path = folder_path + list_of_sounds[sound2]
    sf[voice].out(channel1)
    sf[voice+1].out(channel2)
    
def pick_and_play(voice, sound1, sound2, channel1, channel2):
    sf[voice].path = path1+'/'+sound1
    sf[voice+1].path = path1+'/'+sound2
    sf[voice].out(channel1)
    sf[voice+1].out(channel2)

#count loops
loopCounter = 0

del(fullTrialList)
'''

conditionTxt = 'Where was the sound?'

win.mouseVisible=False
# check responses
if letsGoLocal.keys in ['', [], None]:  # No response was made
    letsGoLocal.keys = None
thisExp.addData('letsGoLocal.keys',letsGoLocal.keys)
if letsGoLocal.keys != None:  # we had a response
    thisExp.addData('letsGoLocal.rt', letsGoLocal.rt)
thisExp.addData('letsGoLocal.started', letsGoLocal.tStartRefresh)
thisExp.addData('letsGoLocal.stopped', letsGoLocal.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "welcom_AudLocal" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
audLocalLoop = data.TrialHandler(nReps=8.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('localizationExp_baseConditionsOneChannel.csv'),
    seed=None, name='audLocalLoop')
thisExp.addLoop(audLocalLoop)  # add the loop to the experiment
thisAudLocalLoop = audLocalLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAudLocalLoop.rgb)
if thisAudLocalLoop != None:
    for paramName in thisAudLocalLoop:
        exec('{} = thisAudLocalLoop[paramName]'.format(paramName))

for thisAudLocalLoop in audLocalLoop:
    currentLoop = audLocalLoop
    # abbreviate parameter names if possible (e.g. rgb = thisAudLocalLoop.rgb)
    if thisAudLocalLoop != None:
        for paramName in thisAudLocalLoop:
            exec('{} = thisAudLocalLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "prepFixCross"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    visPos = (visStimW, visStimH)
    win.mouseVisible=False
    # keep track of which components have finished
    prepFixCrossComponents = [prepFixTxt]
    for thisComponent in prepFixCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prepFixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prepFixCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prepFixCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prepFixCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prepFixTxt* updates
        if prepFixTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prepFixTxt.frameNStart = frameN  # exact frame index
            prepFixTxt.tStart = t  # local t and not account for scr refresh
            prepFixTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prepFixTxt, 'tStartRefresh')  # time at next scr refresh
            prepFixTxt.setAutoDraw(True)
        if prepFixTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prepFixTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                prepFixTxt.tStop = t  # not accounting for scr refresh
                prepFixTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prepFixTxt, 'tStopRefresh')  # time at next scr refresh
                prepFixTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepFixCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prepFixCross"-------
    for thisComponent in prepFixCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    audLocalLoop.addData('prepFixTxt.started', prepFixTxt.tStartRefresh)
    audLocalLoop.addData('prepFixTxt.stopped', prepFixTxt.tStopRefresh)
    win.mouseVisible=False
    
    # ------Prepare to start Routine "audLocalizationTrial"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    #get integer for Pick N' Play
    chnNo1 = int(targetSpkrChannel)
    #chnNo2 = int(partnerSpkrChannel)
    
    #PUT YOUR PICK N' PLAY HERE
    s.start()
    #play from the specified channels (2 and 4 are the flanking channels)
    #Channel 2 is on the left and Channel 4 on the Right
    #pick_and_play(0,noiseLevelFile1,noiseLevelFile2,2,4)
    #print("if we made it this far, you have executed up to pick and play")
    pick_and_play(0,targetSpkrSound,chnNo1)
    #print(noiseLevelFile1)
    #print(noiseLevelFile2)
    #print(loopCounter)
    
    # keep track of which components have finished
    audLocalizationTrialComponents = [prepFixTxt_2]
    for thisComponent in audLocalizationTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    audLocalizationTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "audLocalizationTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = audLocalizationTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=audLocalizationTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prepFixTxt_2* updates
        if prepFixTxt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prepFixTxt_2.frameNStart = frameN  # exact frame index
            prepFixTxt_2.tStart = t  # local t and not account for scr refresh
            prepFixTxt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prepFixTxt_2, 'tStartRefresh')  # time at next scr refresh
            prepFixTxt_2.setAutoDraw(True)
        if prepFixTxt_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prepFixTxt_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                prepFixTxt_2.tStop = t  # not accounting for scr refresh
                prepFixTxt_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prepFixTxt_2, 'tStopRefresh')  # time at next scr refresh
                prepFixTxt_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in audLocalizationTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "audLocalizationTrial"-------
    for thisComponent in audLocalizationTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #Finally I stop the server after each trial
    s.stop()
    
    #update loop counter
    #loopCounter+=1
    
    
    
    audLocalLoop.addData('prepFixTxt_2.started', prepFixTxt_2.tStartRefresh)
    audLocalLoop.addData('prepFixTxt_2.stopped', prepFixTxt_2.tStopRefresh)
    
    # ------Prepare to start Routine "getLocalResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    respPromptLocal.setText(conditionTxt)
    slider.reset()
    win.mouseVisible=True
    # keep track of which components have finished
    getLocalResponseComponents = [respPromptLocal, slider]
    for thisComponent in getLocalResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    getLocalResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "getLocalResponse"-------
    while continueRoutine:
        # get current time
        t = getLocalResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=getLocalResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *respPromptLocal* updates
        if respPromptLocal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respPromptLocal.frameNStart = frameN  # exact frame index
            respPromptLocal.tStart = t  # local t and not account for scr refresh
            respPromptLocal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respPromptLocal, 'tStartRefresh')  # time at next scr refresh
            respPromptLocal.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in getLocalResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "getLocalResponse"-------
    for thisComponent in getLocalResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    audLocalLoop.addData('respPromptLocal.started', respPromptLocal.tStartRefresh)
    audLocalLoop.addData('respPromptLocal.stopped', respPromptLocal.tStopRefresh)
    audLocalLoop.addData('slider.response', slider.getRating())
    audLocalLoop.addData('slider.rt', slider.getRT())
    audLocalLoop.addData('slider.started', slider.tStartRefresh)
    audLocalLoop.addData('slider.stopped', slider.tStopRefresh)
    win.mouseVisible=False
    # the Routine "getLocalResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'audLocalLoop'


# ------Prepare to start Routine "visSetup"-------
continueRoutine = True
# update component parameters for each repeat
letsGoLocal_2.keys = []
letsGoLocal_2.rt = []
_letsGoLocal_2_allKeys = []
conditionTxt = 'Where was the flash?'
# keep track of which components have finished
visSetupComponents = [letsGoLocal_2, text_7]
for thisComponent in visSetupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
visSetupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "visSetup"-------
while continueRoutine:
    # get current time
    t = visSetupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=visSetupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *letsGoLocal_2* updates
    waitOnFlip = False
    if letsGoLocal_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        letsGoLocal_2.frameNStart = frameN  # exact frame index
        letsGoLocal_2.tStart = t  # local t and not account for scr refresh
        letsGoLocal_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(letsGoLocal_2, 'tStartRefresh')  # time at next scr refresh
        letsGoLocal_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(letsGoLocal_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(letsGoLocal_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if letsGoLocal_2.status == STARTED and not waitOnFlip:
        theseKeys = letsGoLocal_2.getKeys(keyList=['space'], waitRelease=False)
        _letsGoLocal_2_allKeys.extend(theseKeys)
        if len(_letsGoLocal_2_allKeys):
            letsGoLocal_2.keys = _letsGoLocal_2_allKeys[-1].name  # just the last key pressed
            letsGoLocal_2.rt = _letsGoLocal_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in visSetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "visSetup"-------
for thisComponent in visSetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if letsGoLocal_2.keys in ['', [], None]:  # No response was made
    letsGoLocal_2.keys = None
thisExp.addData('letsGoLocal_2.keys',letsGoLocal_2.keys)
if letsGoLocal_2.keys != None:  # we had a response
    thisExp.addData('letsGoLocal_2.rt', letsGoLocal_2.rt)
thisExp.addData('letsGoLocal_2.started', letsGoLocal_2.tStartRefresh)
thisExp.addData('letsGoLocal_2.stopped', letsGoLocal_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "visSetup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
visualLocalLoop = data.TrialHandler(nReps=8.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('localizationExp_baseConditionsOneChannel.csv'),
    seed=None, name='visualLocalLoop')
thisExp.addLoop(visualLocalLoop)  # add the loop to the experiment
thisVisualLocalLoop = visualLocalLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVisualLocalLoop.rgb)
if thisVisualLocalLoop != None:
    for paramName in thisVisualLocalLoop:
        exec('{} = thisVisualLocalLoop[paramName]'.format(paramName))

for thisVisualLocalLoop in visualLocalLoop:
    currentLoop = visualLocalLoop
    # abbreviate parameter names if possible (e.g. rgb = thisVisualLocalLoop.rgb)
    if thisVisualLocalLoop != None:
        for paramName in thisVisualLocalLoop:
            exec('{} = thisVisualLocalLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "prepFixCross"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    visPos = (visStimW, visStimH)
    win.mouseVisible=False
    # keep track of which components have finished
    prepFixCrossComponents = [prepFixTxt]
    for thisComponent in prepFixCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prepFixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prepFixCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prepFixCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prepFixCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prepFixTxt* updates
        if prepFixTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prepFixTxt.frameNStart = frameN  # exact frame index
            prepFixTxt.tStart = t  # local t and not account for scr refresh
            prepFixTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prepFixTxt, 'tStartRefresh')  # time at next scr refresh
            prepFixTxt.setAutoDraw(True)
        if prepFixTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prepFixTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                prepFixTxt.tStop = t  # not accounting for scr refresh
                prepFixTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prepFixTxt, 'tStopRefresh')  # time at next scr refresh
                prepFixTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepFixCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prepFixCross"-------
    for thisComponent in prepFixCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    visualLocalLoop.addData('prepFixTxt.started', prepFixTxt.tStartRefresh)
    visualLocalLoop.addData('prepFixTxt.stopped', prepFixTxt.tStopRefresh)
    win.mouseVisible=False
    
    # ------Prepare to start Routine "visLocalizationTrial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    grating.setPos(visPos)
    # keep track of which components have finished
    visLocalizationTrialComponents = [prepFixTxt_3, grating]
    for thisComponent in visLocalizationTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    visLocalizationTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "visLocalizationTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = visLocalizationTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=visLocalizationTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prepFixTxt_3* updates
        if prepFixTxt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prepFixTxt_3.frameNStart = frameN  # exact frame index
            prepFixTxt_3.tStart = t  # local t and not account for scr refresh
            prepFixTxt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prepFixTxt_3, 'tStartRefresh')  # time at next scr refresh
            prepFixTxt_3.setAutoDraw(True)
        if prepFixTxt_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prepFixTxt_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                prepFixTxt_3.tStop = t  # not accounting for scr refresh
                prepFixTxt_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prepFixTxt_3, 'tStopRefresh')  # time at next scr refresh
                prepFixTxt_3.setAutoDraw(False)
        
        # *grating* updates
        if grating.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            grating.setAutoDraw(True)
        if grating.status == STARTED:
            if frameN >= (grating.frameNStart + 1.0):
                # keep track of stop time/frame for later
                grating.tStop = t  # not accounting for scr refresh
                grating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(grating, 'tStopRefresh')  # time at next scr refresh
                grating.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visLocalizationTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "visLocalizationTrial"-------
    for thisComponent in visLocalizationTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    visualLocalLoop.addData('prepFixTxt_3.started', prepFixTxt_3.tStartRefresh)
    visualLocalLoop.addData('prepFixTxt_3.stopped', prepFixTxt_3.tStopRefresh)
    visualLocalLoop.addData('grating.started', grating.tStartRefresh)
    visualLocalLoop.addData('grating.stopped', grating.tStopRefresh)
    
    # ------Prepare to start Routine "getLocalResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    respPromptLocal.setText(conditionTxt)
    slider.reset()
    win.mouseVisible=True
    # keep track of which components have finished
    getLocalResponseComponents = [respPromptLocal, slider]
    for thisComponent in getLocalResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    getLocalResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "getLocalResponse"-------
    while continueRoutine:
        # get current time
        t = getLocalResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=getLocalResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *respPromptLocal* updates
        if respPromptLocal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respPromptLocal.frameNStart = frameN  # exact frame index
            respPromptLocal.tStart = t  # local t and not account for scr refresh
            respPromptLocal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respPromptLocal, 'tStartRefresh')  # time at next scr refresh
            respPromptLocal.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in getLocalResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "getLocalResponse"-------
    for thisComponent in getLocalResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    visualLocalLoop.addData('respPromptLocal.started', respPromptLocal.tStartRefresh)
    visualLocalLoop.addData('respPromptLocal.stopped', respPromptLocal.tStopRefresh)
    visualLocalLoop.addData('slider.response', slider.getRating())
    visualLocalLoop.addData('slider.rt', slider.getRT())
    visualLocalLoop.addData('slider.started', slider.tStartRefresh)
    visualLocalLoop.addData('slider.stopped', slider.tStopRefresh)
    win.mouseVisible=False
    # the Routine "getLocalResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'visualLocalLoop'


# ------Prepare to start Routine "ByeByeTime"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
ByeByeTimeComponents = [exitTxt, key_resp]
for thisComponent in ByeByeTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ByeByeTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ByeByeTime"-------
while continueRoutine:
    # get current time
    t = ByeByeTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ByeByeTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitTxt* updates
    if exitTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exitTxt.frameNStart = frameN  # exact frame index
        exitTxt.tStart = t  # local t and not account for scr refresh
        exitTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exitTxt, 'tStartRefresh')  # time at next scr refresh
        exitTxt.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['c'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ByeByeTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ByeByeTime"-------
for thisComponent in ByeByeTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('exitTxt.started', exitTxt.tStartRefresh)
thisExp.addData('exitTxt.stopped', exitTxt.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "ByeByeTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
