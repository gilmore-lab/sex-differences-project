library(shiny)
source("helpers.R")
data_dir <- "~/Box Sync/Project_Sex_difference_on_Motion_Perception/data/passed_qa/"

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Sex Diffs Viz"),
   
   # Sidebar 
   sidebarLayout(
      sidebarPanel(
         radioButtons("task_type", "Task Type", 
                      choices = list("motion", "contrast"),
                      selected = "motion"),
         selectInput("file_select", label = "Data Files",
                     choices = list.files(data_dir, pattern = input$task_type))
      ),
      
      # Show a plot
      mainPanel(
        plotOutput(outputId = "scatterPlot")
      )
   )
)

# Define server logic
server <- function(input, output) {
   output$scatterPlot <- renderPlot({
      df <- readr::read_csv(paste0(data_dir, input$file_select))
      
      df <- ifelse(input$task_type == "motion",
                   clean_motion_df(df),
                   clean_contrast(df))
      ifelse(input$task_type == "motion",
             plot_motion_staircase(df),
             plot_contrast_staircase(df))
   })
}

# Run the application 
shinyApp(ui = ui, server = server)

# # Helper functions ----------------------------------------------
# clean_motion_df <- function(df) {
#    require(tidyverse)
#    if (!is.data.frame(df)) stop("Not a valid data frame.")
#    
#    df_clean <- df %>%
#       dplyr::mutate(., run = run_n + 1) %>%
#       dplyr::rename(., corr = correct,
#                     dur_s = FWHM)
#    
#    df_clean <- df_clean %>%
#       dplyr::select(.,
#                     run,
#                     trial_n,
#                     dur_s,
#                     corr,
#                     rt) %>%
#       dplyr::mutate(., run = ordered(run))
#    df_clean
# }
# 
# plot_motion_staircase <- function(df) {
#    if (!is.data.frame(df)) stop("Not a valid data frame.")
#    require(ggplot2)
#    
#    ggplot(data = df) +
#       aes(x = trial_n, y = dur_s, color = run) +
#       geom_smooth() +
#       geom_point() +
#       ggtitle("Duration across trials and runs") +
#       theme(legend.position = "bottom")
# }
# 
# generate_motion_fl <- function(data_dir) {
#    list.files(data_dir, pattern = "motion", full.names = TRUE)
# }
# 
# read_sex_diff_file <- function(fn) {
#    if (!file.exists(fn)) stop(paste0("File '", fn, "' not found."))
#    readr::read_csv(fn)
# }
