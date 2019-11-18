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

extract_ids_from_fns <- function(df_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/contrast_sensitivity_task_data") {
  fn_only <- list.files(paste0(df_path), pattern = "\\.csv$")
  stringr::str_sub(fn_only, 1, 16)
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
  file.copy(from = qa_files, to = paste0(path_2_data, "/qa_rpts/."))
}

