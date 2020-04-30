# Functions to aid in the visualization of the sex differences project vision tasks

read_sex_diff_file <- function(fn) {
  if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
  readr::read_csv(fn)
}

extract_sub_id_from_fn <- function(fn) {
  if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
  stringr::str_extract(fn, "[0-9-]+")
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

clean_motion_df <- function(df) {
  require(tidyverse)
  if (!is.data.frame(df)) stop("Not a valid data frame.")

  df_clean <- df %>%
    mutate(., run = run_n + 1) %>%
    rename(., corr = correct,
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

# Functiions to create ioslides_presentations that summarize the computer task data

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

# plot_dur_by_trial_run <- function(df) {
#   ggplot2::ggplot(df) +
#     ggplot2::aes(x = trial_n, y = dur_s, color = run) +
#     ggplot2::geom_smooth() +
#     ggplot2::geom_point() +
#     ggplot2::facet_wrap(~ p_id, ncol = 3) +
#     ggplot2::ggtitle("Duration across trials and runs") 
# }
# 
# source_local_funcs <- function(deck_fn = "slides.R", source_fn) {
#   cat("#' \x60\x60\x60{r}\n", file = deck_fn, append = TRUE)
#   cat("#'", "source('analysis/R/slide_helpers.R')\n", file = deck_fn, append = TRUE)
#   cat("#' \x60\x60\x60\n", file = deck_fn, append = TRUE)
#   cat("#'\n", file = deck_fn, append = TRUE)
# }
# 
# make_a_slide <- function(df, deck_fn = "slides.R",
#                          plot_func = plot_dur_by_trial_run) {
#   # Slide header
#   cat("#'\n", file = deck_fn, append = TRUE)
#   cat("#' ## Participant ", unique(df$p_id), "\n", file = deck_fn, append = TRUE)
#   
#   # Generate plot
#   cat("#' \x60\x60\x60{r}\n", file = deck_fn, append = TRUE)
#   cat("#' plot_dur_by_trial_run(df)\n", file = deck_fn, append = TRUE)
#   cat("#' \x60\x60\x60\n", file = deck_fn, append = TRUE)
#   cat("#'\n", file = deck_fn, append = TRUE)
# }

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

#------------------------------------------------------------
# Functions to regenerate from scratch all plot files
make_passed_qa_path <- function(box_path = "~/Box Sync",
                                data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  paste0(box_path, data_path, "/passed_qa")
}

make_figs_path <- function(box_path = "~/Box Sync",
                           data_path = "/Project_Sex_difference_on_Motion_Perception/data") {
  paste0(box_path, data_path, "/figs")
}

plot_save_motion_all_subs <- function(fd = make_passed_qa_path()) {
  fl <- generate_motion_fl(fd)
  purrr::map(fl, plot_save_motion_task)
}

plot_save_contr_all_subs <- function(fd = make_passed_qa_path()) {
  fl <- generate_contr_fl(fd)
  purrr::map(fl, plot_save_contr_task)
}

regenerate_all_plots_all_subs <- function(fd = make_passed_qa_path()) {
  plot_save_motion_all_subs()
  plot_save_contr_all_subs()
}

generate_motion_fl <- function(data_dir) {
  list.files(data_dir, pattern = "motion", full.names = TRUE)
}

generate_contr_fl <- function(data_dir) {
  list.files(data_dir, pattern = "contrast", full.names = TRUE)
}

copy_figs_to_box <- function(path_2_data = make_figs_path()) {
  
  assertthat::is.string(path_2_data)
  assertthat::is.dir(path_2_data)
  
  fig_files <- list.files("analysis/figs", pattern = "\\.png$", full.names = TRUE)
  n_copied <- file.copy(from = fig_files, to = paste0(path_2_data, "/."), overwrite = TRUE)
  message("Copied ", sum(n_copied), " files to Box.")
}

# 1. Batch QA on both computer tasks
# 2. QA on Qualtrics
# 3. Regenerate figs
# 4. Regenerate HTML slides

#----------------------------------------------
# Test functions
passed_qa_dir <- "~/Box Sync/Project_Sex_difference_on_Motion_Perception/data/passed_qa"

test_motion_plot <- function(fd) {
  message("Testing motion duration task plotting functions.")
  fl <- generate_motion_fl(fd)
  
  plot_save_motion_task(fl[1])
}

test_contr_plot <- function(fd) {
  message("Testing contrast threshold task plotting functions.")
  fl <- generate_contr_fl(fd)
  
  plot_save_contr_task(fl[1])
}
