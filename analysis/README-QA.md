# Sex Differences QA & plotting procedure

## Session-level quality assurance report

This report evaluates all data and generates a report in `analysis/session-qa.html`.

From the R console, execute `rmarkdown::render("analysis/session_qa.Rmd", params = list(box_path = "<YOUR_BOX_PATH>"))`, substituting the path to your Box folder on your local machine.
On Mac OS the default is "~/Box".

## Session-level visualization plots

1. To generate plots
  - `source('analysis/R/plots.R')`
  - Then `generate_save_all_plots_all_subs()`.
  
This will make a set of plot visualizations for each subject where there are no current files and copy them to Box.

2. To regenerate plots

  - `source('analysis/R/plots.R')`
  - Then `regenerate_save_all_plots_all_subs()`.
  
This will regenerate plots for all participants.



