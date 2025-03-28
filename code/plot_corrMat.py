
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') # 直接保存图片，不显示
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
from scipy.stats import linregress
import statsmodels.api as sm
from matplotlib.colors import LinearSegmentedColormap
sns.set()

def compute_RAC(observed_rho, max_rho):
    """
    Compute Attenuation-Corrected Correlation (RAC)
    RAC = observed correlation / max possible correlation
    
    :param observed_rho: Observed item-score Pearson correlation
    :param max_rho: Maximum possible correlation in the dataset
    :return: Attenuation-Corrected Correlation (RAC)
    """
    return observed_rho / max_rho if max_rho != 0 else 0  # Avoid division by zero

def compute_ACER_alpha(data):
    """
    Compute Attenuation-Corrected Cronbach’s Alpha (ACER Alpha)
    
    Formula:
    α_RAC = (k / (k - 1)) * (1 - (sum(σ²_i) / (sum(σ_i * RAC_i))²))
    
    :param data: A 2D numpy array where rows are participants and columns are test items
    :return: ACER Alpha value
    """
    k = data.shape[1]  # Number of items in the test
    item_variances = np.var(data, axis=0, ddof=1)  # Compute variance for each item (unbiased estimate)
    total_variance = np.var(np.sum(data, axis=1), ddof=1)  # Compute total score variance

    # Compute item-total correlations (Pearson correlation between each item and total score)
    item_score_corr = np.array([
        np.corrcoef(data[:, i], np.sum(data, axis=1))[0, 1] for i in range(k)
    ])

    # Determine the maximum possible correlation in the dataset
    max_rho = np.max(item_score_corr)  # Approximate max correlation (can be refined)

    # Compute RAC for each item
    RAC = np.array([compute_RAC(r, max_rho) for r in item_score_corr])

    # Compute ACER Alpha using the formula
    acer_alpha = (k / (k - 1)) * (1 - np.sum(item_variances) / (np.sum(np.sqrt(item_variances) * RAC) ** 2))

    return acer_alpha  # Return the ACER Alpha estimate

# SIFI_Bi_A and SIFI_Bi_V are not included in the current data
# PerceptualTask = ['SIFI_Uni_A', 'SIFI_Uni_V', 'SIFI_Bi_A','SIFI_Bi_V',
#                   'Pitch', 'RhythmV', 'RhythmA', 'SRT_A', 'SRT_V', 'SRT_B', 'LocalizationA', 'LocalizationV',
#                   'SpeechA', 'SpeechAV', 'AuditoryScore', 'VisualScore', 'PerceptualScore']
# PerceptualTask = ['SIFI_Uni_A', 'SIFI_Uni_V', 'SIFI_Bi_A','SIFI_Bi_V',
#                   'Pitch', 'SRT_A', 'SRT_V', 'SRT_B',
#                   'SpeechA', 'SpeechAV', 'AuditoryScore', 'VisualScore', 'PerceptualScore']
PerceptualTask = ['TNJ_Uni_A', 'TNJ_Uni_V', 'TNJ_Bi_A','TNJ_Bi_V', 'TNJ_Bi',
                  'Pitch', 'RhythmV', 'RhythmA', 'SRT_A', 'SRT_V', 'SRT_B', 'LocalizationA', 'LocalizationV',
                  'SpeechA', 'SpeechAV', 'AuditoryScore', 'VisualScore', 'PerceptualScore', 'Pcommon', 'sigmaU', 'sigmaD']
CognitiveTask = ['Corsi', 'LetterNumberSpan', 'Cancellation', 'Raven', 'WordMemory', 'Trail', 'CognitiveScore']

path = '/Users/lijialin/Desktop/Research/proj-cognition-perception/data/clean data/'

### Modify Here!!!
savefig_path = '/Users/lijialin/Desktop/Research/proj-cognition-perception/Figure/Correlation/'
os.makedirs(savefig_path, exist_ok=True)
savefig_path2 = '/Users/lijialin/Desktop/Research/proj-cognition-perception/Figure/LinearRegression/'
os.makedirs(savefig_path2, exist_ok=True)

### Modify Here!!!
data = pd.read_csv('/Users/lijialin/Desktop/Research/proj-cognition-perception/data/clean data/summary/rawData.csv')
# colors = ['rosybrown', 'lightcoral', 'indianred', 'brown', 'firebrick', 'maroon', 
#          'sage', 'deepskyblue', 'cadetblue', 'lightslategrey', 'darkslategrey', 'slategrey', 
#          'mediumslateblue', 'darkslateblue', 'fuchsia', 'magenta', 'black']

CorMat = np.zeros((len(PerceptualTask), len(CognitiveTask)))
CorMatp = np.zeros((len(PerceptualTask), len(CognitiveTask)))
CorMatn = np.zeros((len(PerceptualTask), len(CognitiveTask)))
acerMat = np.zeros((len(PerceptualTask), len(CognitiveTask)))
BetaMat = np.zeros((len(PerceptualTask), len(CognitiveTask)))
RegressMatp = np.zeros((len(PerceptualTask), len(CognitiveTask)))

# colormap for p value
colors = [(0, '#8B0000'),   # 红色，对应值 0
          (0.001, '#FF0000'),  # 深红色，对应值 0.001
          (0.01, '#FFC0CB'),  # 红色，对应值 0.0001
          (0.05, '#FFA07A'),   # 浅红色，对应值 0.01
          (0.1, '#FFFFFF'),   # 黄色，对应值 0.1
          (1, '#FFFFFF')]   # 白色，对应值 0.05
cmap = LinearSegmentedColormap.from_list("Custom", colors)
 
for folder_name in PerceptualTask:
    folder_path = os.path.join(savefig_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

for folder_name in CognitiveTask:
    folder_path = os.path.join(savefig_path2, folder_name)
    os.makedirs(folder_path, exist_ok=True)

for i in range(len(PerceptualTask)):
    for j in range(len(CognitiveTask)):
        x = data[PerceptualTask[i]]
        y = data[CognitiveTask[j]]
        df = pd.DataFrame({'x': x, 'y': y})
        df.dropna(inplace=True, axis= 0)
        correlation_coefficient, p_value = stats.pearsonr(df['x'], df['y'])
        acer = compute_ACER_alpha(np.concatenate((df['x'].values.reshape(-1, 1), df['y'].values.reshape(-1, 1)), axis=1))
        acerMat[i, j] = acer
        CorMat[i, j] = correlation_coefficient
        CorMatp[i, j] = p_value
        CorMatn[i, j] = df.shape[0]
        slope, intercept, r_value, p_value, std_err = linregress(df['x'], df['y'])
        BetaMat[i, j] = slope
        RegressMatp[i, j] = p_value
        fit_line = slope * df['x'] + intercept
        plt.figure()
        plt.scatter(df['x'], df['y'], color = 'mediumslateblue', alpha = 0.75, label='Data')
        plt.plot(df['x'], fit_line, color='lightcoral', label='Linear Regression')
        plt.title(str(PerceptualTask[i]) + ' and ' + str(CognitiveTask[j]))
        plt.xlabel(str(PerceptualTask[i]))
        plt.ylabel(str(CognitiveTask[j]))
        plt.text(0.05, 0.95, 'r = ' + str(round(correlation_coefficient, 3)) + '\n' + 'p = ' + str(round(p_value, 4)) + '\n' + 'n = ' + str(len(df['x'])), ha='left', va='top', transform=plt.gca().transAxes)
        plt.savefig(savefig_path + '/' + str(PerceptualTask[i]) + '/' + str(PerceptualTask[i]) + ' and ' + str(CognitiveTask[j]) + '.png', dpi=300)
        plt.close()

plt.figure(figsize=(15, 10))
sns.heatmap(CorMat, cmap="coolwarm", annot=True, fmt=".3f", annot_kws={"size": 10}, xticklabels=CognitiveTask, yticklabels=PerceptualTask)
plt.title('Correlation Matrix')
plt.savefig(savefig_path + '/' + 'Correlation Matrix.png', dpi=300)
plt.close()

fig, ax = plt.subplots(figsize=(15, 10))  # 修改这里，使用plt.subplots()

sns.heatmap(CorMatp, cmap=cmap, xticklabels=CognitiveTask, yticklabels=PerceptualTask)
plt.title('p-value Matrix')

for i in range(len(CorMat)):
    for j in range(len(CorMat[i])):
        r_value = CorMat[i, j]
        p_value = CorMatp[i, j]
        ax.annotate(f"r={r_value:.3f}\np={p_value:.3f}",
                    xy=(j + 0.5, i + 0.5),  # 修改xy坐标，将文本放在单元格中央
                    horizontalalignment='center',
                    verticalalignment='center',
                    color='black', fontsize=10)

plt.savefig(savefig_path + '/' + 'Correlation p-value Matrix.png', dpi=300)
plt.close()

plt.figure(figsize=(15, 10))
sns.heatmap(CorMatn, cmap="coolwarm", annot=True, fmt=".0f", annot_kws={"size": 10}, xticklabels=CognitiveTask, yticklabels=PerceptualTask)
plt.title('Sample Size Matrix')
plt.savefig(savefig_path + '/' + 'Sample Size Matrix.png', dpi=300)

plt.figure(figsize=(15, 10))
sns.heatmap(BetaMat, cmap="coolwarm", annot=True, fmt=".3f", annot_kws={"size": 10}, xticklabels=CognitiveTask, yticklabels=PerceptualTask)
plt.title('Beta Matrix')
plt.savefig(savefig_path2 + '/' + 'Beta Matrix.png', dpi=300)
plt.close()

plt.figure(figsize=(15, 10))
sns.heatmap(RegressMatp, cmap= cmap, annot=True, fmt=".4f", annot_kws={"size": 10}, xticklabels=CognitiveTask, yticklabels=PerceptualTask)
plt.title('p-value Matrix')
plt.savefig(savefig_path2 + '/' + 'Regress p-value Matrix.png', dpi=300)
plt.close()

plt.figure(figsize=(15, 10))
sns.heatmap(acerMat, cmap="coolwarm", annot=True, fmt=".3f", annot_kws={"size": 10}, xticklabels=CognitiveTask, yticklabels=PerceptualTask)
plt.title('ACER Alpha Matrix')
plt.savefig(savefig_path + '/' + 'ACER Alpha Matrix.png', dpi=300)
plt.close()

# for i in range(len(CognitiveTask)):
#     x = data.iloc[:, 1:16]
#     y = data[CognitiveTask[i]]
#     model = sm.OLS(y, x)
#     results = model.fit()
#     with open(savefig_path2 + '/' + str(CognitiveTask[i]) + '/' + CognitiveTask[i] + '.txt', 'w') as fh:
#         fh.write(results.summary().as_text())
    
#     plt.figure()
#     plt.scatter(y, results.fittedvalues)
#     plt.xlabel('Actual Values')
#     plt.ylabel('Predicted Values')
#     plt.title(str(CognitiveTask[i]))
#     plt.savefig(savefig_path2 + '/' + str(CognitiveTask[i]) + '/' + str(CognitiveTask[i]) + '.png', dpi=300)
#     plt.close()

#     plt.figure()
#     residuals = results.resid
#     plt.scatter(results.fittedvalues, residuals)
#     plt.xlabel('Predicted Values')
#     plt.ylabel('Residuals')
#     plt.title('Residual Plot (Multiple Linear Regression)')
#     plt.axhline(y=0, color='red', linestyle='dashed')  # 添加水平参考线
#     plt.savefig(savefig_path2 + '/' + str(CognitiveTask[i]) + '/' + str(CognitiveTask[i]) + ' Residual Plot.png', dpi=300)

print('-' * 50)
print('Done!')