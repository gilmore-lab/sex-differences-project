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

extract_task_type_from_fn <- function(fn) {
  if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
  motion_task <- stringr::str_detect(fn, "motion")
  contr_task <- stringr::str_detect(fn, "contrast")
  if (motion_task) {
    "motion"
  } else if (contr_task) {
    "contrast"
  } else {
    "unknown-task"
  }
}

generate_plot_fn <- function(data_fn, plot_type = "none") {
  if (!file.exists(data_fn)) stop(paste0("File '", data_fn, "' not found."))
  
  sub_id <- extract_sub_id_from_fn(data_fn)
  task_type <- extract_task_type_from_fn(data_fn)
  paste0("analysis/figs/", sub_id, "-", task_type, "-", plot_type)
}

save_plot <- function(p, fn, file_type = "png") {
  message("Saving to '", paste0(fn, ".", file_type), "'.")
  ggsave(paste0(fn, ".", file_type), plot = p, device = file_type, path = ".")
}

read_sex_diff_file <- function(fn) {
  if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
  readr::read_csv(fn)
}

clean_motion_df <- function(df) {
  require(tidyverse)
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  
  df_clean <- df %>%
    dplyr::mutate(., run = run_n + 1) %>%
    dplyr::rename(., corr = correct,
           dur_s = FWHM)
  
  df_clean <- df_clean %>%
    dplyr::select(.,
                  run,
                  trial_n,
                  dur_s,
                  corr,
                  rt) %>%
    dplyr::mutate(., run = ordered(run))
  df_clean
}

clean_contrast_df <- function(df) {
  require(tidyverse)
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  
  df_clean <- df %>%
    mutate(., correctAns = stringr::str_extract(correctAns, "left|down|right|up")) %>%
    mutate(., corr = if_else(resp == correctAns, 1, 0)) %>%
    rename(., contr = loop_trial.intensity,
           trial_n = loop_trial.thisN,
           rt = resp.rt) %>%
    mutate(., trial_n = trial_n + 1)
  
  df_clean <- df_clean %>%
    dplyr::select(., Participant, Gender,
                  trial_n,
                  contr,
                  correctAns,
                  resp,
                  corr,
                  rt) %>%
    dplyr::filter(., trial_n >= 0) %>%
    dplyr::mutate(., run = rep(1:4, each=30)) %>%
    dplyr::mutate(., run = ordered(run))
  
  df_clean
}

plot_save_motion_task <- function(fn) {
  if (!file.exists(fn)) stop("File '", fn, "' not found.")
  
  df <- read_sex_diff_file(fn)
  if (!is.data.frame(df)) stop("Not a data frame.")
  
  df_clean <- clean_motion_df(df)
  
  # p1 <- plot_motion_staircase(df_clean)
  # p2 <- plot_motion_cum_perf(df_clean)
  # p3 <- plot_motion_rt_across_trials(df_clean)
  # p4 <- plot_motion_rt_by_dur(df_clean)
  
  p1_nm <- generate_plot_fn(data_fn = fn, plot_type = "staircase")
  p2_nm <- generate_plot_fn(data_fn = fn, plot_type = "cum-perf")
  p3_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-trials")
  p4_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-by-dur")
  
  # save_plot(p1, p1_nm)
  # save_plot(p2, p2_nm)
  # save_plot(p3, p3_nm)
  # save_plot(p4, p4_nm)
  
  if (!file.exists(paste0(p1_nm, ".png"))) {
    p1 <- plot_motion_staircase(df_clean)
    save_plot(p1, p1_nm)
  }
  if (!file.exists(paste0(p2_nm, ".png"))) {
    p2 <- plot_motion_cum_perf(df_clean)
    save_plot(p2, p2_nm)
  }  
  if (!file.exists(paste0(p3_nm, ".png"))) {
    p3 <- plot_motion_rt_across_trials(df_clean)
    save_plot(p3, p3_nm)
  }
  if (!file.exists(paste0(p4_nm, ".png"))) {
    p4 <- plot_contr_rt_by_contr(df_clean)
    save_plot(p4, p4_nm)
  }
}

plot_save_contr_task <- function(fn) {
  if (!file.exists(fn)) stop("File '", fn, "' not found.")
  
  df <- read_sex_diff_file(fn)
  if (!is.data.frame(df)) stop("Not a data frame.")
  
  df_clean <- clean_contrast_df(df)
  
  p1_nm <- generate_plot_fn(data_fn = fn, plot_type = "staircase")
  p2_nm <- generate_plot_fn(data_fn = fn, plot_type = "cum-perf")
  p3_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-trials")
  p4_nm <- generate_plot_fn(data_fn = fn, plot_type = "rt-by-contr")
  
  full_path_2_figs <- paste0("analysis/figs/")
  
  if (!file.exists(paste0(p1_nm, ".png"))) {
    p1 <- plot_contr_staircase(df_clean)
    save_plot(p1, p1_nm)
  }
  if (!file.exists(paste0(p2_nm, ".png"))) {
    p2 <- plot_contr_cum_perf(df_clean)
    save_plot(p2, p2_nm)
  }  
  if (!file.exists(paste0(p3_nm, ".png"))) {
    p3 <- plot_contr_rt_across_trials(df_clean)
    save_plot(p3, p3_nm)
  }
  if (!file.exists(paste0(p4_nm, ".png"))) {
    p4 <- plot_contr_rt_by_contr(df_clean)
    save_plot(p4, p4_nm)
  }
}

plot_save_motion_all_subs <- function(fd = make_passed_qa_path()) {
  fl <- generate_motion_fl(fd)
  purrr::map(fl, plot_save_motion_task)
}

plot_save_contr_all_subs <- function(fd = make_passed_qa_path()) {
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
