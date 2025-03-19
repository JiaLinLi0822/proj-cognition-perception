# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:04:22 2023

@author: sauli
"""

import os
import glob
import pandas as pd
import statistics
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt
import csv

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
#Here we have to define where the files are located and source them.

filePath1 = '/Users/camurray/Downloads/data4/' #Path where files are
summaryList1 = glob.glob((filePath1+'*_trailMaking_2023*.csv')) #WhatI am sourcing
fileDestination = '/Users/camurray/Downloads/data4/cleanTrail/' #Where to save files that are finished


##THIS SECTION IS FOR CLEANING THE DATA *************

#THIS LOOP IS FOR EXTRACTING THE COLUMNS
for i in range(len(summaryList1)): #repeat this the total number of files that we have!
    f = summaryList1[i]
    
    psFile = f.replace(filePath1,"")    #get ps ID from the file name to put in the new file name
    place = psFile.find('_')
    name = str(psFile[0:place])
    
    #Here I need to convert the file into a xlsx file instead of a csv

    dat = pd.read_csv(f) #data ='s each csv being read. 
    print(name+' '+str(len(dat.index))) #To double check, lets print out the ID and how many rows
   
    #Now I need a way to only save the needed rows
    
    #Problem = some files have extra rows
    #Therefore, the rows in which the values we need are different per file. 
    #So I will select the needed rows by the number of rows in each file. 
    
    indices35 = [6,13,20,27,34]
    indices20 = [3,7,11,15,19]
    indices16 = [3,7,11,15]
    indices24 = [7,11,15,19,23]
    indices26 = [7,11,16,21,25]

    #The reason for the different indices is
    #The files are extremely messy
    #Each file may have different number of rows :(
    if len(dat.index) == 35:
        dat = dat.loc[indices35]
    elif len(dat.index) ==16:
        dat = dat.loc[indices16]
    elif len(dat.index) ==24:
        dat = dat.loc[indices24]
    elif len(dat.index) ==26:
        dat = dat.loc[indices26]
    else:
        dat = dat.loc[indices20]
        
    #This seems to be working...
    #NOW we can get rid of the NaNs.
    
    #Take out NaNs
    dat = dat.apply(lambda x: pd.Series(x.dropna().values))
    dat = dat.fillna('')
    
    #Clean the data more (remove any string elements)
    dat = dat.replace('"', '', regex = True)
    dat = dat.replace(']', '',regex = True)
    dat = dat.replace(' ', '',regex = True)

    
    #It looks like removing the NaNs reformats it so that the top row
    #is the longest one...
    #Maybe I can remove the last 15 columns each time, then save the last value!
    RTs = []
    nan_value = float("NaN")
    
    #Drop NaNs one more time here
    #Replace Empty Spaces with NaN
    dat.replace("", nan_value, inplace=True)
    #Drop all the NaNs
    dat.dropna(how='all', axis=1, inplace=True)
    
    #This loop will extract the correct values!
    #Currently, we are eating into some decimal miliseconds
    #But we don't need THAT level of precision necessarily
    for i in range(len(dat)):
                for i in range(36):
                    dat.drop(dat.columns[len(dat.columns)-1], axis=1, inplace=True)
                #Save last cell value each loop
                RTs.append(float(dat.iloc[0,-1:]))
                #delete the row
                dat = dat.drop(labels=0, axis=0)
                #Reset Index
                dat = dat.reset_index(drop = True)
                #Replace Empty Spaces with NaN
                dat.replace("", nan_value, inplace=True)
                #Drop all the NaNs
                dat.dropna(how='all', axis=1, inplace=True)
                print('Finished the Go')
    
    Trials = []
    Number = 0
    for i in range(len(RTs)):
        Number = Number+1
        Trials.append(Number)
    
    #Save each number in the RTs list in a new dictionary/Dataframe
    Trial_Data = {'Trial':Trials,
                  'RT':RTs}
    Trial_Data = pd.DataFrame(Trial_Data)
    Trial_Data.to_csv(fileDestination+name+'TrailClean.csv', index=False) 
    print('FINISH ID '+name)

#THIS SECTION IS FOR ANALYZING THE DATA*************
TrailAnalysisSource = 'C:\\Users\sauli\Downloads\SQ_2_28_Analyses for MST\\Trail\\' #Where to save files that are finished
summaryList2 = glob.glob((TrailAnalysisSource+'*Trail*.csv')) #WhatI am sourcing

#List for later
Participant_IDs = []

AvgRT = [] #Excluding Trial 1 and participant 3 and 19
#THIS LOOP IS FOR EXTRACTING THE COLUMNS

for i in range(len(summaryList2)): #repeat this the total number of files that we have!
    f = summaryList2[i]
    
    psFile = f.replace(TrailAnalysisSource,"")    #get ps ID from the file name to put in the new file name
    place = psFile.find('Trail')
    name = str(psFile[0:place])

    #Here I need to convert the file into a xlsx file instead of a csv

    dat = pd.read_csv(f) #data ='s each csv being read. 
    
    if name == '3':
        print('nope this is 3')
    elif name == '19':
        print('nope this is 19')
    else: 
        print(name)
        #delete the first trial data
        dat = dat.drop(labels=0, axis=0)
        #Reset Index
        dat = dat.reset_index(drop = True)
        #Get the average of the RT
        TAverage = np.average(dat['RT'])
        AvgRT.append(TAverage)

Trial2 = []
Trial3 = []
Trial4 = []

for i in range(len(summaryList2)): #repeat this the total number of files that we have!
    f = summaryList2[i]
    
    psFile = f.replace(TrailAnalysisSource,"")    #get ps ID from the file name to put in the new file name
    place = psFile.find('Trail')
    name = str(psFile[0:place])

    #Here I need to convert the file into a xlsx file instead of a csv

    dat = pd.read_csv(f) #data ='s each csv being read. 
#Average across everyone for each trial (Avg trial 2,3,4)
    if name == '3':
        print('nope this is 3')
    elif name == '19':
        print('nope this is 19')
    else: 
        print(name)
        #delete the first trial data
        dat = dat.drop(labels=0, axis=0)
        #Reset Index
        dat = dat.reset_index(drop = True)
        #Get the average of the RT
        Trial2_Unit = dat['RT'][0]
        Trial2.append(Trial2_Unit)
        Trial3_Unit = dat['RT'][1]
        Trial3.append(Trial3_Unit)
        Trial4_Unit = dat['RT'][2]
        Trial4.append(Trial4_Unit)

#Make a list of all participant IDs)
Number= 0
for i in range(len(AvgRT)):
    Number = Number + 1
    Participant_IDs.append(Number)

#Make a Dataframe of all the data
Group_Data = {'ID':Participant_IDs,
              'AllTrialAvg':AvgRT,
              'Trial2':Trial2,
              'Trial3':Trial3,
              'Trial4':Trial4}

Group_Data = pd.DataFrame(Group_Data)


#THIS SECTION IS FOR MAKING GROUP FIGURES(Histograms w Grand Avg)

AvgPlotsFig = sea.histplot(data=Group_Data, x="AllTrialAvg", bins = 10,color = 'plum')

#Change labels
AvgPlotsFig.set(xlabel=' RT (s)',
       ylabel='Frequency',
       title='Average RT')
sea.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
AvgPlotsFig.axvline(Group_Data['AllTrialAvg'].mean(), color='k', linestyle='dashed', linewidth=1)

fig = AvgPlotsFig.get_figure()
fig.savefig((TrailAnalysisSource+'AverageRTDistribution.png'))


#THIS SECTION IS FOR MAKING INDIVIDUAL FIGURES~~~~~~~~~~~~~~~~~~~~~*********************

for i in range(len(summaryList2)): #repeat this the total number of files that we have!
    f = summaryList2[i]
    
    psFile = f.replace(TrailAnalysisSource,"")    #get ps ID from the file name to put in the new file name
    place = psFile.find('Trail')
    name = str(psFile[0:place])
    
    #Here I need to convert the file into a xlsx file instead of a csv

    dat = pd.read_csv(f) #data ='s each csv being read. 
    print(name+' '+str(len(dat.index)))
    
    #THIS PART OF THE CODE CREATES A BARPLOT FOR EACH INDIVIDUAL PERSON~~~~~~~~~~~~~~
    sea.set_theme(style='white')
    plt.figure() #THIS IS ALL I HAD TO ADD FOR IT TO WORK
    plot = sea.barplot(data = dat, x = "Trial", y = 'RT',
                      palette=['lightsteelblue', 'paleturquoise'],
                      linewidth=1,
                      edgecolor = '.2')
    plot.set(xlabel='Trial', ylabel='RT (s)', title=(name+" Trial by Trial TrailMaking RT"))
    plot.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plot.set(ylim=(0,50))
    plt.tight_layout()#it was cropping the image earlier... Now it works
    plot.figure.savefig((TrailAnalysisSource+name+'_TbT_TrailMakingBars.png'))

'''NOTES ABOUT DATA CLEANING
3/1/23
- All the trail files seem to be different lengths?
This is causing mayhem in the analysis script
- Also some of the data files had repeat values in them?
Like this is some trashhhhh
I trimmed 35 spots which is 17.35 would be 17

'''
