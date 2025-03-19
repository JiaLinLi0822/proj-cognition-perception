# proj-cognition-perception
This prooject is trying to investigate the relationship between cognition and perception. In the experiment, participants are required to complete a series of cognitive and perceptual tasks(For certain tasks we used, go to the illustration folder and clik the 'cognition experiment tasks.pdf' file, you will see the details of the task and what ability we tried to task in each task . By choosing certain measurements, we expect to see the connection behind the high-level cognition and low-level perception.



Here are some tips for running the codes to replicate the results we have so far:

### Preprocess the data

Let's say the data are stored in a certain folder, where each task data are saved in different subfolders(In our case, click the 'data' folder and you will see:

1. App Task
2. Cognition Task
3. Perceptual Task
4. Speech Task
5. Trial Task

When you click on a certain raw data in the folder above, you can see that the data is pretty messy and we can't get too much sense on what's going on. In this sense, we might need to summarize the data in some way. Click on the `main.py` in  the code folder and you can see in line 20-21:

```python
dataPath = '/Users/lijialin/Downloads/Cognition Project/data/' # change this to your own path
keyPath = '/Users/lijialin/Downloads/Cognition Project/code/keys/' # change this to your own path
```

Change these two paths to your own local path and simply run the script, you can get the `clean data` folder in the data folder. By running this script, you can also get the `Summary.csv`, in which each column is a measurement of specific task, each row is participant's performance acorss different task.



### Analyze the data

After preprocessing the data, we want to further analyze the data. 

If you want to reproduce the correlation matrix, running the `analyze_corr.R` and go to the `./data/clean data/summary`, you will get three files:

1. CorMat_pValue.csv save the p-value between two task
2. CorMat_rValue.csv save the correlation coefficient between two task
3. rawData.csv save some specific columns from the Summary.csv file above



