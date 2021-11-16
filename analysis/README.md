# Sex differences in vision analysis

The files in this directory reflect the data processing and visualization pipelines for this project.

The raw data files are stored either in other directories or in directories not synched to GitHub. This is to protect participant privacy.

However, a de-identified dataset is available in `csv/qian-berenbaum-gilmore-data.csv`.

## Qian, Berenbaum, & Gilmore manuscript

Files related to a manuscript prepared by Qian, Berenbaum, & Gilmore are as follows:

- `qian-berenbaum-gilmore.Rmd`: Code to reproduce analyses and figures in the paper.
- `qian-berenbaum-gilmore-plots.Rmd`: Code specifically to generate the figures.
- `qian-berenbaum-gilmore-relative-weight-analysis.Rmd`: Code to reproduce this analysis.

## Other folders of note

## VSS 2021 poster

The folder `/qian-gilmore-vss-2021` contains code related to this poster.

- `visualization_VSS.Rmd` generates plots for 

Qian, Y. & Gilmore, R.O. (2021, May). Sex differences in visual processing: Does it relate to cognition or other behaviors? Poster presented at the Virtual Vision Sciences Society (V-VSS) 2021 meeting.

## Presentation for workshop at the University of Rochester (cancelled)

Files related to a cancelled presentation at the University of Rochester can be found in `/qian-gilmore-rochester-2020`.

## Berenbaum, Qian, & Gilmore paper

- `berenbaum-qian-gilmore.Rmd` documents the data cleaning, visualization, and analyses for the paper by Qian, Berenbaum, and Gilmore.
    - The data used in this document were first cleaned and exported from raw files using commands found in `import-clean-raw-data.Rmd`.

## Quality assurance (QA) and by participant visualizations

The `R/master-helpers.R` file contains functions that do most of the work.

Start by entering `source("analysis/R/master-helpers.R")` from the project root directory.

Running `update_all_qa_plots_decks()` function will update everything in about 5 mins.
