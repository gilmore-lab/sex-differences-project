# ioslides_presentations-----------------------------------------------------------------------------------

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
  
  message("Wrote slide deck header info to '", deck_fn, "'.")
}

make_slide_of_plot <- function(plot_fn, deck_fn, plot_path_fr_deck = "figs/") {
  
  cat("#'\n", file = deck_fn, append = TRUE)
  cat("#'----\n", file = deck_fn, append = TRUE)
  cat("#'\n", file = deck_fn, append = TRUE)  
  
  cat("#' ", file = deck_fn, append = TRUE)
  cat('<div class="centered">\n', file = deck_fn, append = TRUE)
  
  cat("#'", paste0(plot_path_fr_deck, plot_fn), "\n", file = deck_fn, append = TRUE)
  cat("#'\n", file = deck_fn, append = TRUE)
  
  cat("#' ", file = deck_fn, append = TRUE)
  cat('<img src=', file = deck_fn, append = TRUE)
  cat('"', paste0(plot_path_fr_deck, plot_fn), '"', file = deck_fn, append = TRUE)
  cat(' height="500px"/>\n', file = deck_fn, append = TRUE)
  
  cat("#'", '</div>\n', file = deck_fn, append = TRUE)
  # cat("#'\n", file = deck_fn, append = TRUE)
}

make_box_decks_path <- function(box_path = "~/Box Sync",
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
  
  # Make plots for this task 
  fl <- list.files("analysis/figs", pattern = "\\.png$")
  pl_fns <- choose_plot_task_type(fl, task_type, plot_type)
  purrr::map(pl_fns, make_plots_for_task, deck_fn)
  
  # Render report
  rmarkdown::render(input = deck_fn, output_format = "ioslides_presentation")
}

make_all_decks <- function(path_2_decks = "analysis") {
  make_deck(deck_fn = paste0(path_2_decks,"/motion-staircase-plots.R"),
            deck_title = "Motion: Staircase",
            task_type = "motion",
            plot_type = "staircase")
  
  make_deck(deck_fn = paste0(path_2_decks, "/contrast-staircase-plots.R"),
            deck_title = "Contrast: Staircase",
            task_type = "contrast",
            plot_type = "staircase")
  
  make_deck(deck_fn = paste0(path_2_decks, "/motion-cum-perf-plots.R"),
            deck_title = "Motion: Cumulative Perf",
            task_type = "motion",
            plot_type = "cum-perf")
  
  make_deck(deck_fn = paste0(path_2_decks, "/contrast-cum-perf-plots.R"),
            deck_title = "Contrast: Cumulative Perf",
            task_type = "contrast",
            plot_type = "cum-perf")
  
  make_deck(deck_fn = paste0(path_2_decks, "/motion-rt-trials-plots.R"),
            deck_title = "Motion: RT by trial",
            task_type = "motion",
            plot_type = "rt-trials")
  
  make_deck(deck_fn = paste0(path_2_decks, "/contrast-rt-trials-plots.R"),
            deck_title = "Contrast: RT by trial",
            task_type = "contrast",
            plot_type = "rt-trials")
  
  make_deck(deck_fn = paste0(path_2_decks, "/motion-rt-by-cond-plots.R"),
            deck_title = "Motion: RT by condition",
            task_type = "motion",
            plot_type = "rt-by-dur")
  
  make_deck(deck_fn = paste0(path_2_decks, "/motion-rt-by-cond-plots.R"),
            deck_title = "Contrast: RT by condition",
            task_type = "motion",
            plot_type = "rt-by-contr")
}

copy_decks_to_box <- function(path_2_box_decks = make_box_decks_path(),
                              path_2_decks = "analysis") {
  
  assertthat::is.string(path_2_box_decks)
  assertthat::is.dir(path_2_box_decks)
  assertthat::is.string(path_2_decks)
  assertthat::is.dir(path_2_decks)
  
  deck_files <- list.files(path = "analysis", pattern = "-plots.html", full.names = TRUE)
  n_copied <- file.copy(from = deck_files, to = paste0(path_2_box_decks, "/."), overwrite = TRUE)
  message("Copied ", sum(n_copied), " *.html files to Box.")
  
  file.copy(from = "analysis/figs", 
                        to = paste0(path_2_box_decks, "/."), 
                        overwrite = TRUE,
                        recursive = TRUE)
  message("Copied *.png files to Box.")
}
