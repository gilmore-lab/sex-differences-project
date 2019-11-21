visualize_contr_sens_data <- function(this_fn_full, this_id) {
  rmarkdown::render("analysis/gather-clean-contrast-sensitivity.Rmd", 
                    output_format = "html_document", output_dir = "analysis/qa",
                    output_file = paste0(this_id, "-contr-sens.html"),
                    params = list(this_csv_fn = this_fn_full, this_sub_id = this_id))
}

visualize_motion_dur_data <- function(this_fn_full, this_id) {
  rmarkdown::render("analysis/gather-clean-motion-dur.Rmd", 
                    output_format = "html_document", output_dir = "analysis/qa",
                    output_file = paste0(this_id, "-motion-dur.html"),
                    params = list(this_csv_fn = this_fn_full, this_sub_id = this_id))
}

visualize_both_tasks_data <- function(this_contr_fn_full, this_motion_fn_full, this_id) {
  rmarkdown::render("analysis/gather-clean-both-tasks.Rmd", 
                    output_format = "html_document", output_dir = "analysis/qa",
                    output_file = paste0(this_id, "-both-tasks.html"),
                    params = list(this_contr_csv_fn = this_contr_fn_full,
                                  this_motion_dur_csv_fn = this_motion_fn_full,
                                  this_sub_id = this_id))
}

extract_ids_from_fns <- function(df_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/contrast_sensitivity_task_data") {
  fn_only <- list.files(paste0(df_path), pattern = "\\.csv$")
  stringr::str_sub(fn_only, 1, 14)
}

list_full_fns_in_path <- function(df_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/contrast_sensitivity_task_data") {
  fns <- list.files(paste0(df_path), pattern = "\\.csv$", full.names = TRUE)
  fns
}

visualize_all_contr_sens_data <- function(df_p = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/contrast_sensitivity_task_data") {
  fns <- list_full_fns_in_path(df_p)
  ids <- extract_ids_from_fns(df_p)
  mapply(visualize_contr_sens_data, fns, ids)
}

visualize_all_motion_dur_data <- function(df_p = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/motion_temporal_threshold_data") {
  fns <- list_full_fns_in_path(df_p)
  ids <- extract_ids_from_fns(df_p)
  mapply(visualize_motion_dur_data, fns, ids)
}

visualize_all_computer_task_data <- function(path_2_data = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data") {
  visualize_all_contr_sens_data(paste0(path_2_data, "/contrast_sensitivity_task_data"))
  visualize_all_motion_dur_data(paste0(path_2_data, "/motion_temporal_threshold_data"))
}

copy_qa_rpts_to_box <- function(path_2_data = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data") {
  qa_files <- list.files("analysis/qa", pattern = "\\.html$", full.names = TRUE)
  n_copied <- file.copy(from = qa_files, to = paste0(path_2_data, "/qa_rpts/."), overwrite = TRUE)
  message("Copied ", sum(n_copied), " files to Box.")
}

list_common_participant_ids <- function(contr_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/contrast_sensitivity_task_data", 
                                        motion_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/motion_temporal_threshold_data") {
  contr_ids <- extract_ids_from_fns(contr_path)
  motion_ids <- extract_ids_from_fns(motion_path)
  if (length(contr_ids) > length(motion_ids)) {
    shorter_list <- motion_ids
  } else if (length(contr_ids) < length(motion_ids)) {
    shorter_list <- contr_ids
  }
  selected_contr <- contr_ids[contr_ids %in% shorter_list]
  selected_motion <- motion_ids[motion_ids %in% shorter_list]
  
  ids_in_common <- (selected_contr == selected_motion)
  shorter_list[ids_in_common]
}

# The following function does not work as of 2019-11-19
# The issue concerns how to handle differences in filenames and ids between the tasks 
# 
# visualize_all_combined_tasks <- function(path_2_data = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data") {
#   
#   # paths to data files
#   contr_path <- paste0(path_2_data, "/contrast_sensitivity_task_data")
#   motion_path <- paste0(path_2_data, "/motion_temporal_threshold_data")
#   
#   # Extract IDs
#   contr_ids <- extract_ids_from_fns(contr_path)
#   motion_ids <- extract_ids_from_fns(motion_path)
#   
#   if (length(contr_ids) != length(contr_path)) {
#     message("Different number of CSV files for both tasks.")
#     ids_in_common <- list_common_participant_ids(contr_path, motion_path)
#     contr_fn <- list_full_fns_in_path(ids_in_common)
#     motion_fn <- list_full_fns_in_path(ids_in_common)
#   } else if (length(contr_ids) == length(motion_ids)) {
#     message("Same number of CSV files available for both tasks.")
#     ids_identical <- (contr_ids == motion_ids)
#     if (sum(ids_identical) == length(ids_identical)) {
#       message("All subject IDs match.")
#       contr_fn <- list_full_fns_in_path(contr_path)
#       motion_fn <- list_full_fns_in_path(motion_path)
#     }
#   }
#   mapply(visualize_both_tasks_data, contr_fn, motion_fn, contr_ids)
# }


has_enough_trials <- function(data_df, n_trials = 4*30) {
  dim(data_df)[1] >= n_trials
}

observer_id_in_file <- function(data_df, task='contr') {
  if (task=='contr') {
    sum(!(is.na(data_df$Participant))) == length(data_df$Participant)
  } else {
    sum(!(is.na(data_df$observer))) == length(data_df$observer)
  }
}

gender_in_file <- function(data_df, task = 'contr') {
  if (task == 'contr') {
    sum(!(is.na(data_df$Gender))) > 0    
  } else {
    sum(!(is.na(data_df$gender))) > 0 
  }
}

sub_id_matches_fn <- function(data_fn, task='contr') {
  data_df <- readr::read_csv(data_fn)
  if (task=='contr') {
    sub_id <- as.character(data_df$Participant)
  } else {
    sub_id <- as.character(data_df$observer)
  }
  sub_id_fn <- stringr::str_extract(basename(data_fn), "[0-9]+")
  sum(sub_id == sub_id_fn) == length(sub_id)
} 

essential_vars_in_file <- function(data_df, task = 'contr') {
  if (task == 'contr') {
    essential_vars <- c("correctAns", "loop_trial.intensity", "loop_trial.thisN",
                                            "Participant", "Gender", "resp.rt")
  } else {
    essential_vars <- c("run_n", "correct", "trial_n", "stim_secs", "correct", "rt",
                        "observer", "FWHM", "actual_frame")
  }
  (sum(essential_vars %in% names(data_df)) == length(essential_vars))
}

make_qa_df <- function(data_fn, task = 'contr') {
  fn <- basename(data_fn)
  data_df <- readr::read_csv(data_fn)
  data.frame(task = task, fn,
             id_matches_fn = sub_id_matches_fn(data_fn, task = task),
             id_in_file = observer_id_in_file(data_df, task = task),
             enough_trials = has_enough_trials(data_df),
             has_key_vars = essential_vars_in_file(data_df, task = task),
             gender_var = gender_in_file(data_df, task = task)
             )
}

run_session_qa_report <- function() {
  rmarkdown::render("analysis/session_qa.Rmd", 
                    output_format = "html_document", output_dir = "analysis/qa",
                    output_file = paste0(Sys.Date(), "-qa-report.html"),
                    params = list(data_path = "~/Box Sync/Project_Sex_difference_on_Motion_Perception/data",
                                  contrast_raw_path = "contrast_sensitivity_task_data",
                                  motion_raw_path = "motion_temporal_threshold_data",
                                  qualtrics_csv_dir = "qualtrics_survey_data/csv"))
  
}

generate_pid <- function(){
  paste0(lubridate::yday(Sys.Date()), format(Sys.time(), "%H%M%S"))
}
