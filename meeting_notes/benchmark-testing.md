---
title: "Benchmark Testing"
author: "Andrea Seisler"
date: "2019-10-30 11:10:54"
output:
  html_document:
    keep_md: true
    toc: true
    toc_depth: 3
    toc_float: true
    code_folding: hide
---



## PsychoPy Benchmark Testing
### Instructions

#### Set Display Resolution
- Open **Display Settings**
- Scroll down to **Resolution** and pick the appropriate resolution from the drop down menu
- Select **Apply** to keep the new resolution


#### Set Display Refresh Rate
- Open **Display Settings**
- Scroll to **Advanced display settings**
- Click **Display adapter properties for Display 1**
  - A new window will open
- In the new window
  - Choose **monitor** tab
  - select desired refresh rate from the drop down menu
  - **Apply**
      
#### Run PsychoPy3 Benchmark Wizard

- Open **PsychoPy3** from the start menu
- Choose the **Tools** tab
- Then choose **Benchmark Wizard**
- Select **OK** to begin the wizard
    - It takes ~30 seconds for the wizard to run then a new window opens
- Select **OK** to view the log results file
- Log the pertinent information in the tables below

###  Screen Resolution and Aspect Ratios

| Resolution | Pixel Aspect Ratio | Display Aspect Ratio | 
|---|---|---
|1600 x 1200 | 1:1                | 4:3                  |
|1280 x 1024 | 1:1                | 5:4                  |
|1024 x 768  | 1:1                | 4:3                  |
|800 x 600   | 1:1                | 4:3                  |

### MIPI Monitor
#### Loud Fan


|  Resolution  | Refresh Rate (Hz) | Vis Sync ( ms/frame) | Refresh Stability (SD)(ms) T1 |T2|T3|T4|T5|T6|T7|T8|T9|T10| Total Dropped Frames| Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1600 x 1200 | 75  |13.33|1.09|1.2|1.3|.49|.32|.26|.42|1.03|.86|.68|0||
| 1600 x 1200 | 85  ||||||||||||| Available, but didn't work |
| 1600 x 1200 | 100 |||||||||||||Available, but didn't work|
| 1600 x 1200 | 120 |||||||||||||Not Available |
|1280 x 1024 | 75  |13.33|.75|.28|.67|.04|.13|.63|.53|.12|.04|.15|0||
|1280 x 1024 | 85  |11.76|.71|.72|.83|.68|.65|.74|.28|.52|.93|.34|0||
|1280 x 1024 | 100 |||||||||||||Available, but didn't work|
|1280 x 1024 | 120 |||||||||||||Not Available|
|1024 x 768  | 75  |13.33|.78|.56|.37|.52|.14|.50|.53|.63|.61|.50|0||
|1024 x 768  | 85  |11.77|.74|.24|.16|4.94|.49|.13|.28|.57|.66|.40|0||
|1024 x 768  | 100 |10.00|.02|.42|.02|.76|.43|.34|.25|.54|.70|.58|0||
|1024 x 768  | 120 |||||||||||||Available, but didn't work|
|800 x 600   | 85  |11.76|.49|.37|.62|.67|.23|.29|.77|.44|.19|.42|1||
|800 x 600   | 100 |10.00|4.89|.28|.38|.82|.21|.26|.05|.33|.03|.65|0||
|800 x 600   | 120 |8.33|.43|.39|.71|.56|.34|.26|4.77|.22|.39|4.79|0|Screen Shifted Left|



### Mitsubishi Monitor - USE THIS MONITOR
##### Quiet Monitor


| Resolution | Refresh Rate (Hz) | Vis Sync ( ms/frame) | Refresh Stability (SD)(ms) T1 |T2|T3|T4|T5|T6|T7|T8|T9|T10| Total Dropped Frames| Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1600 x 1200 | 85 | 11.76 |1.24|.41|.81|.90|1.08|1.17|1.37|.30|.94|1.16|0||
|800 x 600   | 72 | 13.85 |.48|.33|.27|.43|.18|.46|.46|.40|.35|.27|0||
|800 x 600   | 85 | 11.76 |.54|.41|.20|.19|.32|.46|.36|.25|.41|.24|0|USE THIS SETTING|

