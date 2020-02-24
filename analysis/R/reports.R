# Functions to generate R Markdown reports --------------------

# Functions to work with files --------------------------------

# Generate list of data files for motion duration task
generate_motion_fl <- function(data_dir) {
  list.files(data_dir, pattern = "motion", full.names = TRUE)
}

# Generate list of files for contrast task
generate_contr_fl <- function(data_dir) {
  list.files(data_dir, pattern = "contrast", full.names = TRUE)
}

# Extract Sub ID from file name
extract_sub_id_from_fn <- function(fn) {
  if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
  stringr::str_extract(fn, "[0-9-]+")
}

# List CSV data files in data file path
list_full_fns_in_path <- function(df_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/raw_data/contrast_sensitivity_task_data") {
  
  assertthat::is.string(df_path)
  assertthat::is.dir(df_path)
  
  fns <- list.files(paste0(df_path), pattern = "\\.csv$", full.names = TRUE)
  fns
}

# Extract participant IDs from data file names
extract_ids_from_fns <- function(df_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/raw_data/contrast_sensitivity_task_data") {
  
  assertthat::is.string(df_path)
  assertthat::is.dir(df_path)
  
  fn_only <- list.files(paste0(df_path), pattern = "\\.csv$")
  stringr::str_sub(fn_only, 1, 14)
}

# Render R Markdown reports ------------------------------------

# Visualize contrast sensitivity data for individual sub
visualize_contr_sens_data <- function(this_fn_full, regenerate = FALSE) {
  this_id <- extract_sub_id_from_fn(this_fn_full)
  out_fn <- paste0("analysis/qa/", this_id, "-contr-sens.html")
  
  if (file.exists(out_fn)) {
    if (regenerate == FALSE) {
      return(NULL)
    }
  }
  
  rmarkdown::render("analysis/gather-clean-contrast-sensitivity.Rmd", 
                    output_format = "html_document", output_dir = "analysis/qa",
                    output_file = paste0(this_id, "-contr-sens.html"),
                    params = list(this_csv_fn = this_fn_full))
}

# Visualize motion task data for individual sub
visualize_motion_dur_data <- function(this_fn_full, regenerate = FALSE) {
  this_id <- extract_sub_id_from_fn(this_fn_full)
  out_fn <- paste0("analysis/qa/", this_id, "-motion-dur.html")
  
  if (file.exists(out_fn)) {
    if (regenerate == FALSE) {
      return(NULL)
    }
  }
  
  rmarkdown::render("analysis/gather-clean-motion-dur.Rmd", 
                    output_format = "html_document", output_dir = "analysis/qa",
                    output_file = paste0(this_id, "-motion-dur.html"),
                    params = list(this_csv_fn = this_fn_full))
}

# Generate reports for all contrast sensitivity subs
visualize_all_contr_sens_data <- function(contr_fns) {
  purrr::map(contr_fns, visualize_contr_sens_data)
}

# Generate reports for all motion contrast task subs
visualize_all_motion_dur_data <- function(motion_fns) {
  purrr::map(motion_fns, visualize_motion_dur_data)
}

# Summary QA on individual computer task data files, also copies 
run_session_qa_report <- function() {
  rmarkdown::render("analysis/session-qa.Rmd", 
                    output_format = "html_document", 
                    output_dir = "analysis/qa",
                    output_file = paste0(format(Sys.time(), "%Y-%m-%d-%H%M"), "-qa-report.html"),
                    params = list(box_path = "~/Box Sync", 
                                  data_path = "/Project_Sex_difference_on_Motion_Perception/data",
                                  contrast_raw_path = "/raw_data/contrast_sensitivity_task_data",
                                  motion_raw_path = "/raw_data/motion_temporal_threshold_data",
                                  passed_qa_path = "/passed_qa", failed_qa_path = "/failed_qa")
  )
}

# Summary report on Qualtrics
run_qualtrics_qa_report <- function() {
  rmarkdown::render("analysis/gather-clean-qualtrics.Rmd", 
                    output_format = "html_document", 
                    output_dir = "analysis/qa",
                    output_file = paste0(format(Sys.time(), "%Y-%m-%d-%H%M"), "-qualtrics-qa-report.html"),
                    params = list(box_path = "~/Box Sync",
                                  data_path = "/Project_Sex_difference_on_Motion_Perception/data",
                                  qualtrics_raw_path = "/raw_data/qualtrics_survey_data/csv",
                                  old_survey_fn = "survey_REV_2019-11-11.csv",
                                  new_survey_fn = "survey_REV_2019-11-18.csv",
                                  update_raw = TRUE,
                                  reimport_raw = TRUE)
  )
}

# Copy generated QA reports to Box
copy_qa_rpts_to_box <- function(box_path = "~/Box Sync", 
                                data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  
  qa_files <- list.files("analysis/qa", pattern = "\\.html$", full.names = TRUE)
  n_copied <- file.copy(from = qa_files, to = paste0(box_path, data_path, "/qa_rpts/."), overwrite = TRUE)
  message("Copied ", sum(n_copied), " files to Box.")
}


generate_computer_task_qa_rpts <- function(box_path = "~/Box Sync", 
                                           data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  # R Markdown visualizations for each participant and task that passed QA
  files_pass_qa_dir <- paste0(box_path, data_path, "/passed_qa")
  motion_files <- generate_motion_fl(files_pass_qa_dir)
  contr_files <- generate_contr_fl(files_pass_qa_dir)
  
  visualize_all_motion_dur_data(motion_files)
  visualize_all_contr_sens_data(contr_files)
}
