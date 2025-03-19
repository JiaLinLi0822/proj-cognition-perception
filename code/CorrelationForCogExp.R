library(Rmisc) #SummarySE
library(gplots) #heatmap
library(psych) #corr.test
library(RColorBrewer)
library(xlsx)
library(rstatix) # cor_mat, cor_pmat
# Loading Data

Data <- read.csv("/Users/lijialin/Downloads/Cognition Project/data/clean data/Summary.csv")

modelfitting <- read.csv('/Users/lijialin/Downloads/Cognition Project/estimatedparas.csv')
modelfitting$ps <- as.numeric(gsub(".*_(\\d+)_.*", "\\1", modelfitting$File.Name))
Data <- merge(Data, modelfitting, by = 'ps')

# Data <- Data[, !(names(Data) == 'psID')]
# SelectedData<- Data[,c(1,2,3,4,5,6,7,8,10,11,12,14,16,36,37,34,35,18,19,30,9,18,33)]
Data <- Data[, c(1,2,3,4,5,6,7,9,10,14,15,16,20,21,17,18,25,29,36,8,37,24,39,40,41)]

# DFcolnames <- c('psID', 'SIFI_Uni_A', 'SIFI_Uni_V', 'SIFI_Bi_A','SIFI_Bi_V',
#                 'Pitch', 'RhythmV', 'RhythmA', 'SRT_A', 'SRT_V', 'SRT_B', 'LocalizationV', 'LocalizationA',
#                 'SpeechA', 'SpeechAV', 'Corsi', 'LetterNumberSpan', 'Cancellation', 'Raven', 'WordMemory', 'Trail')
DFcolnames <- c('psID', 'TNJ_Uni_A', 'TNJ_Uni_V', 'TNJ_Bi_A','TNJ_Bi_V', 'TNJ_Bi',
                'Pitch', 'RhythmV', 'RhythmA', 'SRT_A', 'SRT_V', 'SRT_B', 'LocalizationV', 'LocalizationA',
                'SpeechA', 'SpeechAV', 'Corsi', 'LetterNumberSpan', 'Cancellation', 'Raven', 'WordMemory', 'Trail',
                'Pcommon', 'sigmaU', 'sigmaD')
colnames(Data) <- DFcolnames
Data <- Data[, !(names(Data) == 'psID')]
Data <- na.omit(Data)

Data$SRT_A <- 1/Data$SRT_A
Data$SRT_V <- 1/Data$SRT_V
Data$SRT_B <- 1/Data$SRT_B
Data$LocalizationA <- 1/Data$LocalizationA
Data$LocalizationV <- 1/Data$LocalizationV
Data$Trail <- 1/Data$Trail

# 计算均值和标准差
means <- colMeans(Data, na.rm = TRUE)
std_devs <- apply(Data, 2, sd, na.rm = TRUE)

# 删除超过3个标准差的数据，仅对数值型列操作
for (i in 1:ncol(Data)) {
  if (is.numeric(Data[, i])) {
    lower_bound <- means[i] - 3 * std_devs[i]
    upper_bound <- means[i] + 3 * std_devs[i]
    Data[, i][Data[, i] < lower_bound | Data[, i] > upper_bound] <- NA
  }
}


# Z score all data
# Data <- as.data.frame(scale(Data))
exclude_columns <- c("Pcommon", "sigmaU", "sigmaD") # 不需要标准化的列
Data_scaled <- Data # 创建副本

# 找出需要标准化的列
columns_to_scale <- setdiff(names(Data), exclude_columns)

# 对指定列进行标准化
Data_scaled[columns_to_scale] <- scale(Data[columns_to_scale])
Data <- Data_scaled

Data$AuditoryScore <- rowSums(Data[,c(1,3,6,8,9,13)], na.rm = TRUE)
Data$VisualScore <- rowSums(Data[,c(2,4,7,10,12)], na.rm = TRUE)
Data$PerceptualScore <- rowSums(Data[,c(1,3,6,8,9,13,2,4,7,10,12,5,11)], na.rm = TRUE)
Data$CognitiveScore <- rowSums(Data[,c(15,16,17,18,19,20)], na.rm = TRUE)

# library(zoo) # na.aggregate
# Data_zscore <- na.omit(Data_zscore)
# Data_zscore <- na.aggregate(Data_zscore, FUN = mean, na.rm = TRUE)
# Data_zscore$PerceptualScore <- rowSums(Data_zscore[,c(1:16)], na.rm = TRUE)
# Data_zscore$CognitiveScore <- rowSums(Data_zscore[,c(16:22)], na.rm = TRUE)

# Data_zscore$PerceptualScore <- as.data.frame(scale(Data_zscore$PerceptualScore))
# Data_zscore$CognitiveScore <- as.data.frame(scale(Data_zscore$CognitiveScore))

# CorMat_p <- cor_pmat(SelectedData)
# CorMat_rr <- cor_mat(CleanData)
CorMat <- corr.test(Data, alpha = 0.05)
# CorMat <- corr.test(SelectedData, alpha = 0.05)
CorMat_r_zScore <- as.matrix(round(CorMat$r, 3))
# CorMat_p <- as.matrix(round(CorMat$p, 3))
CorMat_p <- cor_pmat(Data)
# CorMat_p <- cor_pmat(SelectedData)
CorMat_p_zScore <- CorMat_p[, -which(names(CorMat_p) == "rowname")]

# dir.create('/Users/lijialin/Downloads/Cognition Project/data/clean data/summary')
write.csv(Data, "/Users/lijialin/Downloads/Cognition Project/data/clean data/summary/rawData.csv")
write.csv(CorMat_r_zScore, "/Users/lijialin/Downloads/Cognition Project/data/clean data/summary/CorMat_rValue.csv", row.names = FALSE)
write.csv(CorMat_p_zScore, "/Users/lijialin/Downloads/Cognition Project/data/clean data/summary/CorMat_pValue.csv", row.names = FALSE)

