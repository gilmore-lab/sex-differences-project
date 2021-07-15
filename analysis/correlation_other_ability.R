# test the correlation of mtt/csv to spatial/verbal ability
# Yiming Qian
# Dec 5, 2019

# load data
library(openxlsx)
library(dplyr)
install.packages("Hmisc")
library(Hmisc)
MyData <- read.xlsx("analysis/processed_data.xlsx")

# clean data
MyData$pBest_cst.b1[MyData$pBest_cst.t1<0] <- NA 
MyData$pBest_cst.b2[MyData$pBest_cst.t2<0] <- NA 
MyData$pBest_cst.b3[MyData$pBest_cst.t3<0] <- NA 
MyData$pBest_cst.b4[MyData$pBest_cst.t4<0] <- NA 
MyData$pBest_mtt.b1[MyData$pBest_mtt.t1<0] <- NA 
MyData$pBest_mtt.b2[MyData$pBest_mtt.t2<0] <- NA 
MyData$pBest_mtt.b3[MyData$pBest_mtt.t3<0] <- NA 
MyData$pBest_mtt.b4[MyData$pBest_mtt.t4<0] <- NA
# MyData[,18:21]<-as.numeric(unlist(MyData[,18:21]))
# MyData[,30:33]<-as.numeric(unlist(MyData[,30:33]))
MyData[,14:17]<-as.numeric(unlist(MyData[,14:17]))
MyData[,26:29]<-as.numeric(unlist(MyData[,26:29]))

# calculate the mean slope
MyData %>%
  select(starts_with("pBest_cst.t")%>%
  mutate(slope_cst_mean = rowMeans(),na.rm=TRUE))

            slope_mtt_mean = rowMeans(pBest_mtt.t1:pBest_mtt.t4,na.rm=TRUE)
            
# calculate the correlation coefficient
MyData %>%
  filter(Q1==2) %>% 
  select(starts_with("advoc_"),starts_with("MRT_"),starts_with("threshold_"))->Mydata_f
cor<-rcorr(as.matrix(Mydata_f))
# flattenCorrMatrix(cor$r, cor$P)
symnum(cor$P, cutpoints = c(0.05,0.01,0.005),
       symbols = c("* ", "**", "***"),
       abbr.colnames = TRUE)