# Import data

# Generate a list of files for the contrast threshold task
generate_contr_fl <- function(data_dir, task_filter = "motion") {
  list.files(data_dir, pattern = task_filter, full.names = TRUE)
}

generate_fl <- function(data_dir, task_filter = "motion") {
  list.files(data_dir, pattern = task_filter, full.names = TRUE)
}

clean_data <- function(df) {
  df <- dplyr::mutate(df, run = run_n + 1)
  df <- dplyr::rename(df, corr = correct,
                      dur_s = FWHM)
  df <- dplyr::select(df, run, trial_n, dur_s, corr, rt)
  df <- dplyr::mutate(df, run = ordered(run))
}

read_sex_diff_file <- function(fn) {
  #if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
  readr::read_csv(fn)
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

extract_sub_id_from_fn <- function(fn) {
  stringr::str_extract(fn, "[0-9]{3,12}")
}

plot_motion_staircase <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  
  ggplot(data = df) +
    aes(x = trial_n, y = dur_s, color = run) +
    geom_smooth() +
    geom_point() +
    #ggtitle("Duration across trials and runs") +
    theme(legend.position = "bottom")
}

plot_contr_staircase <- function(df) {
  if (!is.data.frame(df)) stop("Not a valid data frame.")
  require(ggplot2)
  
  ggplot(data = df) +
    aes(x = trial_n, y = contr, color = run) +
    geom_smooth() +
    geom_point() +
    #ggtitle("Contrast across trials and runs") +
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
    #ggtitle("p(corr) by duration across runs") +
    theme(legend.position = "bottom")
}

# Plot cumulative performance across contrast levels
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
    #ggtitle("p(corr) by contrast across runs") +
    theme(legend.position = "bottom")
}

# Plot reaction time across trials for the motion task 
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

# Plot reaction time by motion duration (difficulty)
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

# Plot reaction time across trials
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

# Plot reaction time by contrast (difficulty)
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

# Clean motion task data frame
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

# Clean contrast task data frame
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

read_clean_motion <- function(fn) {
  if (!file.exists(fn)) {
    stop("File '", fn, "' not found.")
  }
  df <- read_sex_diff_file(fn)
  if (!is.data.frame(df)) {
    stop("Data frame not read.")
  }
  clean_motion_df(df)
}

read_clean_contrast <- function(fn) {
  if (!file.exists(fn)) {
    stop("File '", fn, "' not found.")
  }
  df <- read_sex_diff_file(fn)
  if (!is.data.frame(df)) {
    stop("Data frame not read.")
  }
  clean_contrast_df(df)
}


