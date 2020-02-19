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

plot_save_motion_all_subs <- function(fd) {
  fl <- generate_motion_fl(fd)
  purrr::map(fl, plot_save_motion_task)
}

plot_save_contr_all_subs <- function(fd) {
  fl <- generate_contr_fl(fd)
  purrr::map(fl, plot_save_contr_task)
}

regenerate_all_plots_all_subs <- function(fd) {
  plot_save_motion_all_subs()
  plot_save_contr_all_subs()
}
