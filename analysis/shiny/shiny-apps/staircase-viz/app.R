library(shiny)
source("helpers.R")
data_dir <- "~/Box Sync/Project_Sex_difference_on_Motion_Perception/data/passed_qa"

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Sex Differences in Visual Perception"),
   
   # Sidebar 
   sidebarLayout(
      sidebarPanel(
         radioButtons("task_type", "Task Type", 
                      choices = list("motion", "contrast"),
                      selected = "motion"),
         radioButtons("measure_type", "Measure Type",
                      choices = list("corr_incorr", "rt"),
                      selected = "corr_incorr"),
         selectInput("p_id", label = "Participant ID",
                     choices = extract_sub_id_from_fn(list.files(data_dir, 
                                                                 pattern = "[0-9]+")))
      ),
      
      # Show a plot
      mainPanel(
         tabsetPanel(type = "tabs",
                     tabPanel("By Trial", 
                              plotOutput(outputId = "motionStaircasePlot")),
                     tabPanel("By Difficulty", plotOutput(outputId = "motionCumPerfPlot"))
         )
      )
   )
)

# Define server logic
server <- function(input, output) {
   
   data_fn <- reactive({
      fn_match <- list.files(data_dir, pattern = paste0(input$p_id, "_", input$task_type))
      fn_prefix <- paste0(data_dir, "/", fn_match)
      ifelse(input$task_type == "motion",
             fn_suffix <- "motion_temporal_threshold.csv",
             fn_suffix <- "contrast_sensitivity_task.csv")
      paste0(fn_prefix, fn_suffix)
      paste0(fn_prefix)
   })
   
   get_df <- reactive({
      if (input$task_type == "motion") {
         read_clean_motion(data_fn())
      } else {
         read_clean_contrast(data_fn())
      }
   })
   
   output$motionStaircasePlot <- renderPlot({
      
      if (input$task_type == "motion") {
         if (input$measure_type == "corr_incorr") {
            plot_motion_staircase(get_df())
         } else {
            plot_motion_rt_across_trials(get_df()) 
         }
      } else {
         if (input$measure_type == "corr_incorr") {
            plot_contr_staircase(get_df())             
         } else {
            plot_contr_rt_across_trials(get_df())
         }
      }
   })
   
   output$motionCumPerfPlot <- renderPlot({
      ifelse(input$task_type == "motion",
             df <- read_clean_motion(data_fn()),
             df <- read_clean_contrast(data_fn()))
      
      if (input$task_type == "motion") {
         if (input$measure_type == "corr_incorr") {
            plot_motion_cum_perf(df)            
         } else {
            plot_motion_rt_by_dur(df)
         }
      } else {
         if (input$measure_type == "corr_incorr") {
            plot_contr_cum_perf(df)             
         } else {
            plot_contr_rt_by_contr(df)  
         }
      }
   })
}

# Run the application 
shinyApp(ui = ui, server = server)
