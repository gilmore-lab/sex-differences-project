#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Fri Oct 18 17:03:52 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import time

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'contrast_sensitivity_task'  # from the Builder filename that created this script
expInfo = {'Gender':'','Participant':time.strftime("%Y%m%d%H%M%S")}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['Participant'],  expInfo['expName'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/yxq5055/Box/Project_Sex_difference_on_Motion_Perception/codes/psychopy_procedure.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# set up parameters
ramp_up_secs=0.5
full_scale_secs=1
stim_dur_secs=2
this_tf=1

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction_practice"
instruction_practiceClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text="You will see black and white stripes which are horizontal or vertical. Press the LEFT or RIGHT buttons if you see the stripes are horizontal, UP or DOWN button if you see the stripes are vertical. \n\nIf you don't see anything then guess! \n \n \nNext you will have several pratice trials. Press any key to continue.",
    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endInstructions = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.GratingStim(
    win=win, name='fixation',
    tex=None, mask='gauss',
    ori=0, pos=[0, 0], size=1, sf=None, phase=0.0,
    color='black', colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=-1.0)
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask='gauss',
    ori=1.0, pos=[0,0], size=1.0, sf=1.0, phase=0.0,
    color='white', colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=-2.0)
resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
fd_instructions = visual.TextStim(win=win, name='fd_instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instruction_trial"
instruction_trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Good job!\n\nPress RIGHT or LEFT button if you see horizontal grating.\nPress UP or DOWN button if you see vertical grating.\nIf you don't see anything then guess! No more feedback will be provided. Take your time and get the response as accurate as possible.\n \n Press any key to continue.",
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.GratingStim(
    win=win, name='fixation',
    tex=None, mask='gauss',
    ori=0, pos=[0, 0], size=1, sf=None, phase=0.0,
    color='black', colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=-1.0)
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask='gauss',
    ori=1.0, pos=[0,0], size=1.0, sf=1.0, phase=0.0,
    color='white', colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=-2.0)
resp = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksMsg = visual.TextStim(win=win, name='thanksMsg',
    text="You're done! You can contact the researcher outside the room and feel free to have a break if you need!",
    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction_practice"-------
# update component parameters for each repeat
endInstructions.keys = []
endInstructions.rt = []
# keep track of which components have finished
instruction_practiceComponents = [instrText, endInstructions]
for thisComponent in instruction_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruction_practice"-------
while continueRoutine:
    # get current time
    t = instruction_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    
    # *endInstructions* updates
    waitOnFlip = False
    if endInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endInstructions.frameNStart = frameN  # exact frame index
        endInstructions.tStart = t  # local t and not account for scr refresh
        endInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endInstructions, 'tStartRefresh')  # time at next scr refresh
        endInstructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endInstructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endInstructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endInstructions.status == STARTED and not waitOnFlip:
        theseKeys = endInstructions.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            endInstructions.keys = theseKeys.name  # just the last key pressed
            endInstructions.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_practice"-------
for thisComponent in instruction_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# check responses
if endInstructions.keys in ['', [], None]:  # No response was made
    endInstructions.keys = None
thisExp.addData('endInstructions.keys',endInstructions.keys)  # shown in the output
if endInstructions.keys != None:  # we had a response
    thisExp.addData('endInstructions.rt', endInstructions.rt)   # shown in the output
thisExp.addData('endInstructions.started', endInstructions.tStartRefresh)
thisExp.addData('endInstructions.stopped', endInstructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of trials etc
conditions = data.importConditions('stairDefinitions.xlsx')
loop_practice = data.MultiStairHandler(stairType='QUEST', name='loop_practice',
    nTrials=5,
    conditions=conditions,
    originPath=-1)
thisExp.addLoop(loop_practice)  # add the loop to the experiment
# initialise values for first condition
level = loop_practice._nextIntensity  # initialise some vals
condition = loop_practice.currentStaircase.condition

for level, condition in loop_practice:
    currentLoop = loop_practice
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    if random()>0.5:
        ori = 90  #this is orientation of the grating
        correctAns = ['left','right']
    else:
        ori = 0
        correctAns = ['up','down']
    grating.setColor(level, colorSpace='rgb')
    grating.setSize(stim_diam_degs)
    grating.setOri(ori)
    grating.setSF(SF)
    resp.keys = []
    resp.rt = []
    # keep track of which components have finished
    trialComponents = [fixation, grating, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.15-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *grating* updates
        if grating.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.tStartRefresh = tThisFlipGlobal  # on global time
            grating.phase = np.sin(2 * np.pi * clock.getTime() * this_tf) # from counterphase.py demo
            # Contrast ramp in, hold, down
            secs_passed = clock.getTime()-t
            if secs_passed <= ramp_up_secs:
                this_contr = (secs_passed/ramp_up_secs)*level
            elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
                this_contr = level
            else:
                this_contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*level
            grating.color = this_contr
    #            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            grating.draw()
            win.flip()

        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp.keys = theseKeys.name  # just the last key pressed
                resp.rt = theseKeys.rt
                # was this 'correct'?
                if ((resp.keys == 'left'and ori==90) or (resp.keys == 'right' and ori==90) or (resp.keys == 'up'and ori==0) or (resp.keys == 'down'and ori==0)):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_practice (MultiStairHandler)practice
    loop_practice.addResponse(resp.corr)
    # thisExp.addData('resp', theseKeys.name)
    # thisExp.addData('resp.rt', theseKeys.rt)
    # thisExp.addData('resp.started', resp.tStartRefresh)
    # thisExp.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if resp.corr==1:   #stored on last run routine
        msg="Correct!"
    else:
        msg="Oops! That was wrong"
    fd_instructions.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [fd_instructions]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fd_instructions* updates
        if fd_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fd_instructions.frameNStart = frameN  # exact frame index
            fd_instructions.tStart = t  # local t and not account for scr refresh
            fd_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fd_instructions, 'tStartRefresh')  # time at next scr refresh
            fd_instructions.setAutoDraw(True)
        if fd_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fd_instructions.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fd_instructions.tStop = t  # not accounting for scr refresh
                fd_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fd_instructions, 'tStopRefresh')  # time at next scr refresh
                fd_instructions.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# all staircases completed


# ------Prepare to start Routine "instruction_trial"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
instruction_trialComponents = [text, key_resp_2]
for thisComponent in instruction_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruction_trial"-------
while continueRoutine:
    # get current time
    t = instruction_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_trial"-------
for thisComponent in instruction_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of trials etc
conditions = data.importConditions('stairDefinitions.xlsx')
loop_trial = data.MultiStairHandler(stairType='QUEST', name='loop_trial',
    nTrials=30,
    conditions=conditions,
    originPath=-1)
thisExp.addLoop(loop_trial)  # add the loop to the experiment
# initialise values for first condition
level = loop_trial._nextIntensity  # initialise some vals
condition = loop_trial.currentStaircase.condition

for level, condition in loop_trial:
    currentLoop = loop_trial
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    if random()>0.5:
        ori = 90  #this is orientation of the grating
        correctAns = ['left','right']
    else:
        ori = 0
        correctAns = ['up','down']
    grating.setColor(level, colorSpace='rgb')
    grating.setSize(stim_diam_degs)
    grating.setOri(ori)
    grating.setSF(SF)
    resp.keys = []
    resp.rt = []
    # keep track of which components have finished
    trialComponents = [fixation, grating, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.15-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *grating* updates
        if grating.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.tStartRefresh = tThisFlipGlobal  # on global time
#       keep_going = True
#       start_time=clock.getTime()
        #while keep_going:
        # keep track of start time/frame for later
            grating.phase = np.sin(2 * np.pi * clock.getTime() * this_tf) # from counterphase.py demo
        # Contrast ramp in, hold, down
            secs_passed = clock.getTime()-t
            if secs_passed <= ramp_up_secs:
                this_contr = (secs_passed/ramp_up_secs)*level
            elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
                this_contr = level
            else:
                this_contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*level
            grating.color = this_contr
    #            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            grating.draw()
            win.flip()
#            if (clock.getTime()-start_time > stim_dur_secs):
#                win.flip()
#                keep_going = False
    
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp.keys = theseKeys.name  # just the last key pressed
                resp.rt = theseKeys.rt
                # was this 'correct'?
                if ((resp.keys == 'left'and ori==90) or (resp.keys == 'right' and ori==90) or (resp.keys == 'up'and ori==0) or (resp.keys == 'down'and ori==0)):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
#               keep_going = False
                continueRoutine = False
        
                
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
#    trial.addOtherData('ori',ori)
#    trial.addOtherData('correctAns', correctAns)
#    trial.addOtherData('resp.keys', str(resp.keys))
#    trial.addOtherData('resp.rt', resp.rt)
#    trial.addOtherData('fixation.started', fixation.tStartRefresh)
#    trial.addOtherData('fixation.stopped', fixation.tStopRefresh)
#    trial.addOtherData('grating.started', grating.tStartRefresh)
#    trial.addOtherData('grating.stopped', grating.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for loop_trial (MultiStairHandler)
    loop_trial.addResponse(resp.corr)
    thisExp.addData('ori',ori)
    thisExp.addData('correctAns', correctAns)
    thisExp.addData('resp', theseKeys.name)
    thisExp.addData('resp.rt', theseKeys.rt)
#    loop_trial.addOtherData('resp.rt', resp.rt)
#    loop_trial.addOtherData('resp.started', resp.tStartRefresh)
#    loop_trial.addOtherData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# ------Prepare to start Routine "thanks"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
thanksComponents = [thanksMsg, key_resp_3]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksMsg* updates
    if thanksMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksMsg.frameNStart = frameN  # exact frame index
        thanksMsg.tStart = t  # local t and not account for scr refresh
        thanksMsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksMsg, 'tStartRefresh')  # time at next scr refresh
        thanksMsg.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys = theseKeys.name  # just the last key pressed
            key_resp_3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanksMsg.started', thanksMsg.tStartRefresh)
thisExp.addData('thanksMsg.stopped', thanksMsg.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv',appendFile=True)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
