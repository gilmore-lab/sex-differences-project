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
                     choices = list.files(data_dir, pattern = "motion",
                                          full.names = TRUE))
      ),
      
      # Show a plot
      mainPanel(
         textOutput(outputId = "filePlotted"),
         plotOutput(outputId = "scatterPlot")
      )
   )
)

# Define server logic
server <- function(input, output) {
   
   output$textOutput <- renderText({
      input$file_select
   })
   
   output$scatterPlot <- renderPlot({
      df <- read_clean_motion(input$file_select)
      #df <- ifelse(input$task_type == "motion",
                   # clean_motion_df(df),
                   # clean_contrast(df))
      
      plot_motion_staircase(df)
      #df <- clean_motion_df(df)
      # ifelse(input$task_type == "motion",
      #        plot_motion_staircase(df),
      #        plot_contrast_staircase(df))
   })
}

# Run the application 
shinyApp(ui = ui, server = server)
