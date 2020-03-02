#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application 
ui <- fluidPage(
   # Application title
   titlePanel("Hello, World!"),
   
   # Sidebar two drop-down menus for friendName and punctuation 
   sidebarLayout(
      sidebarPanel(
        selectInput(inputId = "friendName",
                    label = "Friend:", 
                    choices = c("World", "Teresa", "Lou", "Chaz")
        ),
        selectInput(inputId = "punctuation",
                    label = "Punctuation:",
                    choices = c("!", "?", "."))
      ),
      
      # Show the text
      mainPanel(
         textOutput(outputId = "greetingText")
      )
   )
)

# Define server logic required to draw text
server <- function(input, output) {
   output$greetingText <- renderText({
     paste("Hello, ", input$friendName, input$punctuation, sep="")
   })
}

# Run the application 
shinyApp(ui = ui, server = server)

