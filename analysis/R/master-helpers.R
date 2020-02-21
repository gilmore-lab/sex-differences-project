# R Markdown reports -----------------------------------------------------------------------------------

list_full_fns_in_path <- function(df_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/raw_data/contrast_sensitivity_task_data") {
  
  assertthat::is.string(df_path)
  assertthat::is.dir(df_path)
  
  fns <- list.files(paste0(df_path), pattern = "\\.csv$", full.names = TRUE)
  fns
}

extract_ids_from_fns <- function(df_path = "~/Box\ Sync/Project_Sex_difference_on_Motion_Perception/data/raw_data/contrast_sensitivity_task_data") {
  
  assertthat::is.string(df_path)
  assertthat::is.dir(df_path)
  
  fn_only <- list.files(paste0(df_path), pattern = "\\.csv$")
  stringr::str_sub(fn_only, 1, 14)
}

# Visualize contrast sensitivity data for individual sub
visualize_contr_sens_data <- function(this_fn_full) {
  this_id <- extract_sub_id_from_fn(this_fn_full)
  
  rmarkdown::render("analysis/gather-clean-contrast-sensitivity.Rmd", 
                    output_format = "html_document", output_dir = "analysis/qa",
                    output_file = paste0(this_id, "-contr-sens.html"),
                    params = list(this_csv_fn = this_fn_full))
}

# Visualize motion task data for individual sub
visualize_motion_dur_data <- function(this_fn_full) {
  this_id <- extract_sub_id_from_fn(this_fn_full)
  
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

copy_qa_rpts_to_box <- function(box_path = "~/Box Sync", 
                                data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  
  qa_files <- list.files("analysis/qa", pattern = "\\.html$", full.names = TRUE)
  n_copied <- file.copy(from = qa_files, to = paste0(box_path, data_path, "/qa_rpts/."), overwrite = TRUE)
  message("Copied ", sum(n_copied), " files to Box.")
}

# Plotting data, making figs ---------------------------------------------------------------------------------

generate_motion_fl <- function(data_dir) {
  list.files(data_dir, pattern = "motion", full.names = TRUE)
}

generate_contr_fl <- function(data_dir) {
  list.files(data_dir, pattern = "contrast", full.names = TRUE)
}

plot_motion_staircase <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  
  ggplot(data = df) +
    aes(x = trial_n, y = dur_s, color = run) +
    geom_smooth() +
    geom_point() +
    ggtitle("Duration across trials and runs") +
    theme(legend.position = "bottom")
}

plot_contr_staircase <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  
  ggplot(data = df) +
    aes(x = trial_n, y = contr, color = run) +
    geom_smooth() +
    geom_point() +
    ggtitle("Contrast across trials and runs") +
    theme(legend.position = "bottom")
}

plot_motion_cum_perf <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  require(dplyr)
  
  df <- df %>%
    dplyr::group_by(., run) %>%
    dplyr::arrange(., dur_s) %>%
    dplyr::mutate(., cum_sum = cumsum(corr),
                  cum_p = cum_sum/n())
  
  ggplot(df) +
    aes(x = dur_s, y = cum_p, color = run) +
    geom_point() +
    geom_smooth(se = FALSE)  +
    ggtitle("p(corr) by duration across runs") +
    theme(legend.position = "bottom")
}

plot_contr_cum_perf <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  require(dplyr)
  
  df <- df %>%
    dplyr::group_by(., run) %>%
    dplyr::arrange(., contr) %>%
    dplyr::mutate(., cum_sum = cumsum(corr),
                  cum_p = cum_sum/n())
  
  ggplot(df) +
    aes(x = contr, y = cum_p, color = run) +
    geom_point() +
    geom_smooth(se = FALSE) +
    ggtitle("p(corr) by contrast across runs") +
    theme(legend.position = "bottom")
}

plot_motion_rt_across_trials <- function(df){
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  ggplot(df) +
    aes(x = trial_n, y = rt, color = run) +
    geom_point() +
    geom_smooth() +
    ggtitle("RT across trials and runs") +
    theme(legend.position = "bottom")
}

plot_motion_rt_by_dur <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  ggplot(df) +
    aes(x = dur_s, y = rt, color = run) +
    geom_point() +
    geom_smooth() +
    ggtitle("RT by duration across runs") +
    theme(legend.position = "bottom")
}

plot_contr_rt_across_trials <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  ggplot(df) +
    aes(x = trial_n, y = rt, color = run) +
    geom_point() +
    geom_smooth() +
    ggtitle("RT across trials and runs") +
    theme(legend.position = "bottom")
}

plot_contr_rt_by_contr <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  ggplot(df) +
    aes(x = contr, y = rt, color = run) +
    geom_point() +
    geom_smooth() +
    ggtitle("RT by contrast across runs") +
    theme(legend.position = "bottom")
}

generate_plot_fn <- function(data_fn, plot_type = "none") {
  if (!file.exists(data_fn)) stop(paste0("File '", data_fn, "' not found."))
  
  sub_id <- extract_sub_id_from_fn(data_fn)
  task_type <- extract_task_type_from_fn(data_fn)
  paste0(sub_id, "-", task_type, "-", plot_type)
}

save_plot <- function(p, fn, file_type = "png") {
  message("Saving to '", paste0(fn, ".", file_type), "'.")
  ggsave(paste0(fn, ".", file_type), plot = p, device = file_type, path = "figs")
}

plot_save_motion_task <- function(fn) {
  if (!file.exists(fn)) stop("File '", fn, "' not found.")
  
  df <- read_sex_diff_file(fn)
  if (!is.data.frame(df)) stop("Not a data frame.")
  
  df_clean <- clean_motion_df(df)
  
  p1 <- plot_motion_staircase(df_clean)
  p2 <- plot_motion_cum_perf(df_clean)
  p3 <- plot_motion_rt_across_trials(df_clean)
  p4 <- plot_motion_rt_by_dur(df_clean)
  
  p1_nm <- generate_plot_fn(data_fn = fn, plot_type = "staircase")
  p2_nm <- generate_plot_fn(data_fn = fn, plot_type = "cum-perf")
  p3_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-trials")
  p4_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-by-dur")
  
  save_plot(p1, p1_nm)
  save_plot(p2, p2_nm)
  save_plot(p3, p3_nm)
  save_plot(p4, p4_nm)
}

plot_save_contr_task <- function(fn) {
  if (!file.exists(fn)) stop("File '", fn, "' not found.")
  
  df <- read_sex_diff_file(fn)
  if (!is.data.frame(df)) stop("Not a data frame.")
  
  df_clean <- clean_contrast_df(df)
  
  p1 <- plot_contr_staircase(df_clean)
  p2 <- plot_contr_cum_perf(df_clean)
  p3 <- plot_contr_rt_across_trials(df_clean)
  p4 <- plot_contr_rt_by_contr(df_clean)
  
  p1_nm <- generate_plot_fn(data_fn = fn, plot_type = "staircase")
  p2_nm <- generate_plot_fn(data_fn = fn, plot_type = "cum-perf")
  p3_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-trials")
  p4_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-by-contr")
  
  save_plot(p1, p1_nm)
  save_plot(p2, p2_nm)
  save_plot(p3, p3_nm)
  save_plot(p4, p4_nm)
}

plot_save_motion_all_subs <- function(fd = passed_qa_dir) {
  fl <- generate_motion_fl(fd)
  purrr::map(fl, plot_save_motion_task)
}

plot_save_contr_all_subs <- function(fd = passed_qa_dir) {
  fl <- generate_contr_fl(fd)
  purrr::map(fl, plot_save_contr_task)
}

make_passed_qa_path <- function(box_path = "~/Box Sync",
                                data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  paste0(box_path, data_path, "/passed_qa")
}

make_figs_path <- function(box_path = "~/Box Sync",
                           data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  paste0(box_path, data_path, "/figs")
}

copy_figs_to_box <- function(path_2_data = make_figs_path()) {
  
  assertthat::is.string(path_2_data)
  assertthat::is.dir(path_2_data)
  
  fig_files <- list.files("analysis/figs", pattern = "\\.png$", full.names = TRUE)
  n_copied <- file.copy(from = fig_files, to = paste0(path_2_data, "/."), overwrite = TRUE)
  message("Copied ", sum(n_copied), " files to Box.")
}

regenerate_all_plots_all_subs <- function(fd = make_passed_qa_path()) {
  plot_save_motion_all_subs()
  plot_save_contr_all_subs()
}

generate_save_all_plots_all_subs <- function(fd = make_passed_qa_path()) {
  regenerate_all_plots_all_subs(fd)
  copy_figs_to_box()
}

# ioslides_presentations-----------------------------------------------------------------------------------

write_slide_header <- function(deck_fn = "slides.R",
                               deck_title = "Sex Diffs Plots",
                               author = "Rick Gilmore",
                               output = "github_document",
                               overwrite = TRUE) {
  
  # Create file
  file.create(deck_fn)
  
  # Create YAML header
  cat("#' ---\n", file = deck_fn, append = TRUE)
  cat("#' title: '", deck_title, "'\n", file = deck_fn, append = TRUE)
  cat("#' author: '", author, "'\n", file = deck_fn, append = TRUE)
  cat("#' date: '`r Sys.time()`'\n", file = deck_fn, append = TRUE)
  cat("#' output:\n", file = deck_fn, append = TRUE)
  cat("#'   ioslides_presentation:\n", file = deck_fn, append = TRUE)
  cat("#'     widescreen: true\n", file = deck_fn, append = TRUE)
  cat("#'     smaller: true\n", file = deck_fn, append = TRUE)
  cat("#' ---\n", file = deck_fn, append = TRUE)
}

extract_sub_id_from_fn <- function(fn) {
  if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
  stringr::str_extract(fn, "[0-9-]+")
}

unique_sub_ids_from_fl <- function(fl) {
  unique(purrr::map_chr(fl, extract_sub_id_from_fn))
}

select_plots_for_sub_id <- function(s_id, fl) {
  this_sub_id <- stringr::str_detect(fl, paste0(s_id))
  fl[this_sub_id]
}

make_slide_of_plot <- function(plot_fn, deck_fn) {
  #sub_id <- extract_sub_id_from_fn(plot_fn)
  sub_id <- plot_fn
  
  cat("#'\n", file = deck_fn, append = TRUE)
  cat("#'----\n", file = deck_fn, append = TRUE)
  cat("#'\n", file = deck_fn, append = TRUE)  
  
  cat("#' ", file = deck_fn, append = TRUE)
  cat('<div class="centered">\n', file = deck_fn, append = TRUE)
  
  cat("#'", plot_fn, "\n", file = deck_fn, append = TRUE)
  cat("#'\n", file = deck_fn, append = TRUE)
  
  cat("#' ", file = deck_fn, append = TRUE)
  cat('<img src=', file = deck_fn, append = TRUE)
  cat('"', plot_fn, '"', file = deck_fn, append = TRUE)
  cat('height="500px"/>\n', file = deck_fn, append = TRUE)
  
  cat("#'", '</div>\n', file = deck_fn, append = TRUE)
  # cat("#'\n", file = deck_fn, append = TRUE)
}

make_decks_path <- function(box_path = "~/Box Sync",
                           data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  paste0(box_path, data_path, "/slide_decks")
}

make_plots_for_sub <- function(s_id, fl, deck_fn) {
  these_plots <- select_plots_for_sub_id(s_id, fl)
  purrr::map(these_plots, make_slide_of_plot, deck_fn)
}

make_plots_for_task <- function(fns, deck_fn) {
  purrr::map(fns, make_slide_of_plot, deck_fn)
}

choose_plot_task_type <- function(fl, task_type = "motion",
                                  plot_type = "staircase") {
  these_files <- (stringr::str_detect(fl, task_type)) & (stringr::str_detect(fl, plot_type))
  fl[these_files]              
}

make_deck <- function(deck_fn,
                      deck_title,
                      task_type,
                      plot_type) {
  
  write_slide_header(deck_fn, deck_title)
  
  fl <- list.files("figs", full.names = TRUE)
  u_ids <- unique_sub_ids_from_fl(fl)
  pl_fns <- choose_plot_task_type(fl, task_type, plot_type)
  
  purrr::map(pl_fns, make_plots_for_task, deck_fn)
  rmarkdown::render(input = deck_fn, output_format = "ioslides_presentation")
}

make_all_decks <- function() {
  make_deck(deck_fn = "motion-staircase-plots.R",
            deck_title = "Motion: Staircase",
            task_type = "motion",
            plot_type = "staircase")
  
  make_deck(deck_fn = "contrast-staircase-plots.R",
            deck_title = "Contrast: Staircase",
            task_type = "contrast",
            plot_type = "staircase")
  
  make_deck(deck_fn = "motion-cum-perf-plots.R",
            deck_title = "Motion: Cumulative Perf",
            task_type = "motion",
            plot_type = "cum-perf")
  
  make_deck(deck_fn = "contrast-cum-perf-plots.R",
            deck_title = "Contrast: Cumulative Perf",
            task_type = "contrast",
            plot_type = "cum-perf")
  
  make_deck(deck_fn = "motion-rt-trials-plots.R",
            deck_title = "Motion: RT by trial",
            task_type = "motion",
            plot_type = "rt-trials")
  
  make_deck(deck_fn = "contrast-rt-trials-plots.R",
            deck_title = "Contrast: RT by trial",
            task_type = "contrast",
            plot_type = "rt-trials")
  
  make_deck(deck_fn = "motion-rt-by-cond-plots.R",
            deck_title = "Motion: RT by condition",
            task_type = "motion",
            plot_type = "rt-by-dur")
  
  make_deck(deck_fn = "contrast-rt-by-cond-plots.R",
            deck_title = "Contrast: RT by condition",
            task_type = "motion",
            plot_type = "rt-by-contr")
}

copy_decks_to_box <- function(path_2_decks = make_decks_path()) {
  
  assertthat::is.string(path_2_decks)
  assertthat::is.dir(path_2_decks)
  
  deck_files <- list.files(path = "analysis", pattern = "-plots.html", full.names = TRUE)
  n_copied <- file.copy(from = deck_files, to = paste0(path_2_decks, "/."), overwrite = TRUE)
  message("Copied ", sum(n_copied), " files to Box.")
}

# Full QA/plotting scheme ------------------------------------------------------------------------

update_all_qa_plots_decks <- function() {
  # QA reports
  run_session_qa_report()
  run_qualtrics_qa_report()
  
  # R Markdown visualizations for each participant and task that passed QA
  files_pass_qa_dir <- make_passed_qa_path()
  motion_files <- generate_motion_fl(files_pass_qa_dir)
  contr_files <- generate_contr_fl(files_pass_qa_dir)
    
  visualize_all_motion_dur_data(motion_files)
  visualize_all_contr_sens_data(contr_files)
  
  # Copy reports to Box
  copy_qa_rpts_to_box()
  
  # Make plots of data that pass QA
  regenerate_all_plots_all_subs()
  copy_figs_to_box()
  
  # Make ioslides_presentation decks for inspection
  make_all_decks()
  copy_decks_to_box()
}
