# ReadME

These are the codes used to extract the useful data from the raw data for each participant. In order to be eaiser to use, I write several modules used to extract different task results from raw data. To use the codes, you only need to do several steps below:

1. Open the main.py
2. Modify the paths. To be specific
   1. rawDatafilePath is used to get clean data from raw data for SIFI, Pitch Discrimination and Raven Task
   2. rawDatafilePath2 is used to get clean data from raw data for Rhythm and Simple Reaction Time(SRT) Task
   3. rawDatafilePath3 is used to get clean data from raw data for Speech and Localization Task
   4. saveDatafilePath is used to save the CleanData for some of the tasks, like SIFI, Pitch Discrimination, Speech and Localization. These clean data can be used to further sophisticated analysis
   5. keyPath is used to compare the response and correct answer for some of the tasks like Raven, WordMemory and Localization task. Make sure that these .csv files are existed in the path you assign.

3. There are some trash files for some of participants which either has blank sheet or missing value in the data. Thus,  when you run the codes, it might have runTime error. The way to solve this is put these trash files away and re-run it again.
4. When you run it successfully, you will get a summary for all task score. You can use this sheet to do the analysis you want.

