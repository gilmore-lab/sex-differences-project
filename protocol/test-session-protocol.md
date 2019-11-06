---
title: "Testing session protocol"
author: "Yiming Qian, Andrea Seisler, & Rick Gilmore"
date: "2019-11-06 09:27:47"
output:
  html_document:
    keep_md: true
    toc: true
    toc_depth: 3
    toc_float: true
    code_folding: hide
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
- Load page with surveys: <https://pennstate.qualtrics.com/jfe/form/SV_1FCXbmrfTWprQON>

### After participant arrives {.tabset}

#### Welcome participant

Say:

>"*Welcome to the brain, behavior, and development lab. Are you hear for the study about motion perception?*"

If the participant answers yes, say:

>"*Great. You can put your things here.*"

- Store belongings in **X**.

>"*Are you \<NAME OF PERSON ON SONA SYSTEMS SITE SCHEDULED FOR THIS SESSION\>?*"

- If the participant answers yes, say:

>"*Ok. We want to make sure that you get credit for participation. Please sit here for the first portion of the study.*"

- Have the person sit at the computer where the survey will be taken.

#### Begin the survey

- Enter the ID: YYYY-MM-DD-HHMM based on appointment time

Conduct the implied verbal consent.
You may say to the participant or have them read the following text:





You are being invited to volunteer to participate in a research study. This summary explains information about this research.	

-	The purpose of this voluntary research study is to investigate how human beings perceive motion in an experimental setting and how this ability is related to personal interests and other abilities. 
The results of this research study will help scientists gain a deeper understanding of what contributes to individual differences in motion perception, and whether or how motion perception is correlated with other aspects of life. 
-	You will complete some computer-based surveys about your background, personal interests, spatial and verbal abilities (~25 min). Then, you will complete one or two short (10-20 min) computer tasks in which you will attempt to detect motion or recognize the direction of motion presented on a computer screen.
-	All questionnaire and computer task data you provide will be saved using a numeric code. No information about your identity or how to contact you will be saved with the data. 
-	If you are participating as part of the Psychology Subject Pool, you will receive course credit for participating (at the rate of ½ credit per ½ hours) as specified in the syllabus provided by your instructor. This means you will get 1 credit for participating this research. Alternative means for earning this course credit are available as specified in the syllabus.

If you have questions, complaints, or concerns about the research, you should contact Yiming Qian at 814-863-3116 or Rick Gilmore at 814-865-3664.
If you have questions regarding your rights as a research subject or concerns regarding your privacy, you may contact the Office for Research Protections at 814-865-1775. 

Your participation is voluntary and you may decide to stop at any time.  You do not have to answer any questions that you do not want to answer. 

Clicking the “Take The Survey” button implies two things: (1) that you are at least 18 years of age, and (2) you voluntarily consent to participate in the research. 
Thank you!

Once the consent is complete, say:

>"*That's great. Now we'd like to move on to the vision screening portion of the study. Are you ready?*"

- If the participant says yes, proceed.

### Complete pattern visual acuity testing

- Complete [pattern acuity test](vision-screening-protocol.html)
  - Adult - HOTV @ 10ft

### Questionnaires

- Let the participants finish the items
-	Ask the participant if they need a little break. If the participant wants to keep going, lead them to the test room

Say:

>"*You have finished the first part of testing. Next you have behavorial testing. Do you want to continue or have a little break?*"

### Set-up for computer-based tasks

- Guide participant to the testing room.
- Have them sit in the chair.
- Adjust the monitor and participant position.
- The monitor should be located **60cm** from the bridge of the nose on the participant.
- The chair height should be set so the participant is looking directly at the **X** in the middle of the screen.
- Guide the participant to use the arrow keys for responses.

### Run computer-based tasks

#### *Select run order*

The order of the computer experiments will be randomized across participants by flipping a coin.
If the coin is HEADS, run the Murray et al. task first; if the coin is TAILS, run the Abramov et al. task first.
Record the task run first on the experiment run log.

#### Murray et al.



- Open PsychoPy by clicking on the icon located on the desktop.
![PsychoPy_Logo](images/PsychoPy-1.PNG)  
- When PsychoPy opens, open the file for this experiment.
    - From the `File` menu, select the `Open Recent...` command and select the `motion-temporal-threshold.py` file.
- When the file opens, run the experiment by pressing press the green (running person) button.
    - **Be careful not to type in the programming window.**
    - A welcome screen with the following message will appear: *Welcome to the motion duration threshold study. Press any key to continue.*
- When you are ready to enter the participant ID, press a key on the keyboard.
    - A pop-up window will appear.
    - Enter the participant ID in the pop window, and press the `Ok` button to enter the data.
- Speak to the participant

>“In this task, you will try to detect whether a small patch of stripes is moving to the left or to the right. The time the patch appears on the display will get shorter and shorter. Our goal is to find out the shortest duration you need to reliably detect the direction of motion."

>"This task takes about 2 min to complete. But to make sure that we get reliable results, we'll need to do it 4 times. You can take a short break between the sections."

>"Put your fingers on the left and right arrow keys. You'll press the left arrow if you see motion to the left and the right arrow if you see motion to the right. If you aren't sure, just guess."

>"Are you ready. Ok, let's go."

#### Abramov et al.

- Open the files "" located in folder.
- In PsychoPy, press the green button. 
- Enter the ID in the pop window and speak to the participant.

>“*Okay. You can follow the instructions and do the tasks in the computer. I am outside this room, if you have questions,...*"

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


