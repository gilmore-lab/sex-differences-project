---
title: "Testing session protocol"
author: "Yiming Qian, Andrea Seisler, & Rick Gilmore"
date: "2019-11-12 13:28:43"
output:
  pdf_document:
    toc: yes
    toc_depth: 3
  html_document:
    code_folding: hide
    keep_md: yes
    toc: yes
    toc_depth: 3
    toc_float: yes
knit:  rmarkdown::render('test-session-protocol.Rmd', output_format = 'all')
---

## Before participant arrives

- Check to see if there have been any cancellations.
- If the scheduled study is still on the books, proceed as follows.

### Set-up for Vision Screening  {.tabset}

#### Preparation

Materials for vision screening are stored on the table next to Andrea's office.

- Make sure the black tape is on the floor 10ft from the HOVT Snellen Acuity Chart which is on the door to 503B
- Place Stereo Acuity Test and Glasses on table
- Place Color Vision Test on table
- Place the Vision Screening Score Sheet on the table

#### Review vision screening procedures

The vision screening protocol may be reviewed at [this link](vision-screening-protocol.html)

### Set up for computer-based tasks {.tabset}

#### Stimuli Computer
- *Log into Data Collection Computer*
  - Turn on the power of the data collection computer
  - Turn on the CRT monitor in 503B
  - Log-in (Gilmore Lab)

- *Start Psychopy* 
  - Click **PsychoPy** icon on Task Bar
 ![PsychoPy_Logo](images/PsychoPy-1.PNG)  
- *Double-check monitor settings within Windows* 
  - Click Settings ('gear') icon on Task Bar
 ![Settings_Logo](images/DispSettings-1.PNG)  
  - Choose **System**  
 ![System](images/DS2.PNG)  
  - Choose **Display**  
 ![Display](images/ds3.PNG)  
  - Choose **Advanced display settings** (You may need to scroll down to see this)  
 ![Advanced Display](images/DS4.PNG)  
  - Make sure the window that appears has the following Settings  
 ![Monitor Settings](images/ds5.PNG)   
- *Double-check Brightness/Contrast of monitor*
  - Contrast:
  - Brightness:
  
  
  - Press any button on the monitor (except Signal A/B/OSD OFF and the Power button)
  - Navigate to the leftmost option in the settings menu (looks like a half moon)
  - Press the down button on the monitor 
  - Adjust the Contrast (leftmost option) to the required setting using the +/- buttons on the monitor 
  - Adjust the Brightness (second option from the left) to the required setting using the +/- buttons on the monitor 
  
- *Check monitor within PsychoPy*  
  - Go to **Monitor Settings**   
 ![Monitor Settings](images/pp2.png)  
  - View Settings, they should be as follows    
 ![Specific Settings](images/pp3.PNG)   
 
#### Survey Computer

- Log-in to survey computer
- Load page with surveys: <https://pennstate.qualtrics.com/jfe/form/SV_0Cad5AtrbQN0GKV>

### After participant arrives {.tabset}

#### Welcome participant

Say:

>"*Welcome to the brain, behavior, and development lab. Are you here for the study about individual difference of motion perception?*"

If the participant answers yes, say:

>"*Great. You can put your coat on the back of the door and your bag here.*"

- Store coat on back of main door and bags by the file/bookcase.

>"*Are you \<NAME OF PERSON ON SONA SYSTEMS SITE SCHEDULED FOR THIS SESSION\>?*"

- If the participant answers yes, say:

>"*Ok. We want to make sure that you get credit for participation. Please sit here for the first portion of the study.*"

- Have the person sit at the computer where the survey will be taken.

#### Begin the survey

- You will see the Participant ID on the top of implied consent. Take a note of this participant ID (only the numeric code without comma or hyphen).

Conduct the implied verbal consent.
You may say to the participant or have them read the following text:





You are being invited to participate in a research study. 

-	The purpose of this voluntary research study is to investigate how human beings perceive motion in an experimental setting.
The results of this research study will help scientists gain a deeper understanding of what contributes to individual differences in motion perception, and whether or how motion perception is correlated with other aspects of life. 
-	You will complete one computer-based surveys. Then, you will complete two short computer tasks in which you will attempt to detect motion on a computer screen.
-	All questionnaire and computer task data you provide will be saved using a numeric code. No information about your identity or how to contact you will be saved with the data. 
-	If you are participating as part of the Psychology Subject Pool, you will receive course credit for participation as specified in the syllabus provided by your instructor. This means you will get 1 credit for participating this research. Alternative means for earning this course credit are available as specified in the syllabus.

If you have questions, complaints, or concerns about the research, you could contact principal investigator Yiming Qian or her advisor Rick Gilmore.
If you have questions regarding your rights as a research subject or concerns regarding your privacy, you could contact the Office for Research Protections. 

Your participation is voluntary and you may decide to stop at any time. You do not have to answer any questions that you do not want to answer. 

Clicking the "Next” button implies two things: (1) that you are at least 18 years of age, and (2) you voluntarily consent to participate in the research. 
Thank you!

Once the consent is complete (It means the participant clicks to the next page), say:

>"*That's great. Now we'd like to move on to the vision screening portion of the study. Could you stand behind this line?*"

### Complete pattern visual acuity testing

- Complete [pattern acuity test](vision-screening-protocol.html)
  - Adult - HOTV @ 10ft

### Questionnaires

>"*Thank you. Now we'd like to move on to the questionnaire portion of the study. Please sit down. You can follow the instructions and finish the survey. Feel free to ask me if you have any questions. And let me know when you finish it.*"

- Have the participant sit back down at the computer.
- Let the participants finish the questionnaire.
- Answer the questions if the participants have any, when they works on the questionnaires. But in careful in the hobby page, spatial and verbal page, because the time are recorded. The page will vanish when the time have passed. So, depending on the nature of the questions, answer them fast and emphasize the time is recorded in this page.
- close the door for participants
After answering the question, say:
>"*Beware: there is a time limit for this page. *"

- If the participants have questions in the instruction page of hobby test, spatial and verbal test, answer careful and make sure the participants understand well. 
-	After the participants finish the questionnaire, ask them if they need a little break. If the participant wants to keep going, lead them to the test room

Say:

>"*You have finished the first part of testing. Next you have behavorial testing. Do you want to continue or have a little break?*"

### Set-up for computer-based tasks

- Guide participant to the testing room.
- Have them sit in the chair.
- Adjust the monitor and participant position.
- The monitor should be located **60cm** from the bridge of the nose on the participant.
- The chair height should be set so the participant is looking in the middle of the screen.
- Guide the participant to use the arrow keys for responses and the space bar to advance the screen.

### Run computer-based tasks

#### Select run order

The order of the computer experiments will be randomized across participants based on the participant ID shown in Qualtrics
- run the temporal duration threshold task first (Murray et al.) if the ID number is even.
- run the contrast sensitivity task (Abramov et al.) first if the ID number is odd.
*Record the task run first on the experiment run log.*

#### Temporal duration threshold task (Murray et al.)



- Open PsychoPy by clicking on the icon located on the desktop.
![PsychoPy_Logo](images/PsychoPy-1.PNG)  
- When PsychoPy opens, open the file for this experiment.
    - From the `File` menu, select the `Open Recent...` command and select the `motion-temporal-threshold.py` file.
- When the file opens, run the experiment by pressing press the green (running person) button. ![PsychoPy_Run](images/PPrunningMan.png)  
    - **Be careful not to type in the programming window.**
- Experimenters need to fill in the participant ID and gender.
    - A pop-up window will appear.
    - Participant ID in the pop-up window have shown "YYYYMMDD", which is the first part of participant ID. Enter the rest numbers of participant ID based on the note you take from the beginning of qualtrics.
    - Enter gender (enter "f" or "m", no upper case) in the pop window, and press the `Ok` button to enter the data.
- Speak to the participant

>“In this task, you need to detect the moving direction of a small patch of stripes. The time the patch appears on the display will get shorter and shorter. Our goal is to find out the shortest duration you need to detect the direction of motion."

>"Which hand do you prefer to press the arrow keys?"
>"Put your fingers on the left and right arrow keys. You'll press the left arrow if you see motion to the left and the right arrow if you see motion to the right. If you aren't sure, make your best guess."
>For the left-handed: "You could press this ENTER key on the right side to preceed instead of space bar. "

>"On the computer screen, you will see a black dot at first. When the black dot appear,  press the space bar to start the trial. Then you will see the patch. Make responses of left or right when the white dots appear.

>"Remember, accuracy is more important that speed. Please take your time."

>"This task takes about 1 min to complete. But to make sure that we get reliable results, there are 4 sections. You can take a short break between the sections."

>"Do you have any questions right now? Okay. I will leave you in the room. Follow the instructions on the screen. Call me when you finished this part."

#### Contrast sensitivity task (Abramov et al.)



![PsychoPy_Logo](images/PsychoPy-1.PNG)  
- When PsychoPy opens, open the file for this experiment.
    - From the `File` menu, select the `Open Recent...` command and select the `xxx.py` file.
- When the file opens, run the experiment by pressing press the green (running person) button. ![PsychoPy_Run](images/PPrunningMan.png)  
    - **Be careful not to type in the programming window.**
- Experimenters need to fill in the participant ID and gender.
    - A pop-up window will appear.
    - Participant ID in the pop-up window have shown "YYYYMMDD", which is the first part of participant ID. Enter the rest numbers of participant ID based on the note you take from the beginning of qualtrics.
    - Enter gender (enter "f" or "m", no upper case) in the pop window, and press the `Ok` button to enter the data.
- Speak to the participant

>“You will see a small patch of black and white stripes which is horizontal or vertical.Be careful. You need to detect the direction of the stripes not the moving direction. You can press the LEFT or RIGHT buttons if you see the stripes are horizontal, UP or DOWN button if you see the stripes are vertical. But if you aren't sure, just guess. "


>“In this task, you will see a small patch of black and white stripes and need to detect the direction of these strips, rather than their moving direction. The luminance of the stripes will get smaller and smaller. Our goal is to find out the smallest luminance that you need to detect the direction of stripes."

>"Which hand do you prefer to press the arrow keys?"
>"Put your fingers on the left and down arrow keys. You'll press the left arrow if you see see horizontal stripes and the down arrow if you see vertical stripes. If you aren't sure, make your best guess."
>For the left-handed: "You could press this ENTER key on the right side to preceed instead of space bar."

>"Remember, accuracy is more important that speed. Please take your time."

>"This task takes about 1 min to complete. But to make sure that we get reliable results, there are 4 sections. You could take a short break between the sections."

>"Do you have any questions right now? Okay. I will leave you in the room. Follow the instructions on the screen. Call me when you finish this part."

### (Optional) stereo acuity and color vision tests

If there is time left (5 min before the end of the 1 hr session),

>"*Thank you so much. It looks like we have time for two more short vision tests. Please come sit over here at this table.*"

Escort participant to table.

- Complete [Stereo Acuity Test](vision-screening-protocol.html)
- Complete [Color Vision Test](vision-screening-protocol.html)

## After session ends

### Thank participant

- After the participant finishes all the tests, thank him/her.

>"*Thank you for participating this experiment. We appreciate your time. Do you have any questions?*"

- Answer any questions the participant might have. You may direct them to Yiming or to Dr. Gilmore if you are unable to answer the question.

### Give participant credit on SONA

- Yiming or Andrea will assign credit in SONA.

### Clean-up

- Clean keyboard, mouse and table and begin [data export](sex-differences-data-export.md) (separate protocols).


