trim_yyyymmddhhmmss_names <- function(fn) {
  if (!is.character(fn)) {
    stop(paste0("'fn' must be a string"))
  }
  stringr::str_detect(fn, "20191[12].*\\.csv$")
}

detect_2019mm <- function(fn) {
  if (!is.character(fn)) {
    stop(paste0("'fn' must be a string"))
  }
  stringr::str_detect(fn, "20191[12].*\\.csv$")
}

replace_2019mm <- function(fn) {
  new_fn <- stringr::str_replace(fn, "201911", paste0("2019-11-"))
  stringr::str_replace(new_fn, "201912", paste0("2019-12-"))
}

add_time_dash <- function(fn) {
  rs <- paste0(stringr::str_extract_all(fn, 
                                  pattern = "1[12]-([0-3])([0-9])"), "-")
  stringr::str_replace(fn, pattern = "1[12]-([0-3])([0-9])", rs)
}

extract_mtime <- function(fn){
  if (!is.character(fn)) {
    stop(paste0("'fn' must be a string"))
  }
  finfo <- file.info(fn)
  finfo$mtime
}

make_new_names_from_info <- function(fn) {
  fn_files <- fn[file.exists(fn) && !dir.exists(fn)]
  finf <- file.info(fn_files)
  f_base <- basename(fn_files)
  f_ext <- stringr::str_extract(fn_files, "\\.[a-z]+")
  f_dir <- dirname(fn_files)
  new_f_base <- finf$ctime
  paste0(f_dir, "/", new_f_base, f_ext)
}

replace_odd_chars <- function(fn) {
  stringr::str_replace_all(fn, "[ :]", "-")
}

new_file_names <- function(fdir) {
  fl <- list.files(fdir, full.names = TRUE)
  new_fn <- make_new_names_from_info(fl)
  replace_odd_chars(new_fn)
}

purrr::map_chr(fl, make_new_names_from_info)
