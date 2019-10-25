---
title: "Benchmark Testing"
author: "Andrea Seisler"
date: "2019-10-25 13:23:06"
output:
  html_document:
    keep_md: true
    toc: true
    toc_depth: 3
    toc_float: true
    code_folding: hide
---



## PsychoPy Benchmark Testing
###  Screen Resolution and Aspect Ratios

| Resolution | Pixel Aspect Ratio | Display Aspect Ratio | 
|1600 x 1200 | 1:1                | 4:3                  |
|1280 x 1024 | 1:1                | 5:4                  |
|1024 x 768  | 1:1                | 4:3                  |
|800 x 600   | 1:1                | 4:3                  |

### MIPI Monitor

| Resolution | Refresh Rate (Hz) | Vis Sync ( ms/frame) | Refresh Stability (SD)(ms) T1 |T2|T3|T4|T5|T6|T7|T8|T9|T10| Average Refresh Stability | Dropped Frames| Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1600 x 1200 | 75  |13.33|1.09|1.2|1.3|.49|.32|   |  |  | | |0| |
|1600 x 1200 | 85  |  |  |  |||||||||||| Available, but didn't work |
|1600 x 1200 | 100 |  |  |  | ||||||||||Available, but didn't work|
|1600 x 1200 | 120 |  |  |  | ||||||||||Not Available |
|1280 x 1024 | 75  |  |  |  ||||||||||||
|1280 x 1024 | 85  |  |  |  ||||||||||||
|1280 x 1024 | 120 |  |  |  |||||||||||Not Available|
|1024 x 768  | 75  |  |  |  ||||||||||||
|1024 x 768  | 85  |  |  |  ||||||||||||
|1024 x 768  | 120 |  |  |  |  |  |  ||||||| ||Available, but didn't work|
|800 x 600   | 75  |  |  |  ||||||||||||
|800 x 600   | 85  |  |  |  ||||||||||||
|800 x 600   | 120 |8.33|.43|.39|.71|.56|.34|.26|4.77|.22|.39|4.79|  |0|Screen Shifted Left|


### Mitsubishi Monitor
| Resolution | Refresh Rate (Hz) | Vis Sync ( ms/frame) | Refresh Stability (SD)(ms) T1 |T2|T3|T4|T5|T6|T7|T8|T9|T10|Average Refresh Stability | Dropped Frames| Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1600 x 1200 | 85  | 11.76 | 1.24 |.41  |.81  |.90  |1.08  |1.17|1.37|.30|.94|1.16||0 ||
|800 x 600   | 72 | 13.85 | .48 |.33  |.27  |.43  |.18  |.46|.46|.40|.35|.27||0||
