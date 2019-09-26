#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.4),
    on Mon Sep  9 12:17:25 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.4'
expName = 'interleaved_QUEST_staircase_contrast'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/yimingqian/Box Sync/projects/sexdifference/codes/contrast_sensitivity_task/interleaved_QUEST_staircase_contrast.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

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
    frameDur = 1.0 / 120.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text="Press the left and right cursor keys to indicate whether the grating was vertical or horizontal. \n \nIf you don't see anything then guess! \n \n \nPress any key to continue",
    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixation = visual.GratingStim(
    win=win, name='fixation',
    tex=None, mask='gauss',
    ori=0, pos=[0, 0], size=1, sf=None, phase=0.0,
    color='black', colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=0)
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask='gauss',
    ori=1.0, pos=(0,0), size=1.0, sf=1.0, phase=0.0,
    color='white', colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksMsg = visual.TextStim(win=win, name='thanksMsg',
    text="You're done! You can contact the researcher outside the room. You are free to have a break!",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
endInstructions = keyboard.Keyboard()
# keep track of which components have finished
instructionsComponents = [instrText, endInstructions]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # not accounting for scr refresh
        instrText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    
    # *endInstructions* updates
    if t >= 0.0 and endInstructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        endInstructions.tStart = t  # not accounting for scr refresh
        endInstructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(endInstructions, 'tStartRefresh')  # time at next scr refresh
        endInstructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(endInstructions.clock.reset)  # t=0 on next screen flip
        endInstructions.clearEvents(eventType='keyboard')
    if endInstructions.status == STARTED:
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
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# check responses
if endInstructions.keys in ['', [], None]:  # No response was made
    endInstructions.keys = None
thisExp.addData('endInstructions.keys',endInstructions.keys)
if endInstructions.keys != None:  # we had a response
    thisExp.addData('endInstructions.rt', endInstructions.rt)
thisExp.addData('endInstructions.started', endInstructions.tStartRefresh)
thisExp.addData('endInstructions.stopped', endInstructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of trials etc
conditions = data.importConditions('stairDefinitions.xlsx')
trials = data.MultiStairHandler(stairType='QUEST', name='trials',
    nTrials=40,
    conditions=conditions,
    originPath=-1)
thisExp.addLoop(trials)  # add the loop to the experiment
# initialise values for first condition
level = trials._nextIntensity  # initialise some vals
condition = trials.currentStaircase.condition

for level, condition in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if random()>0.5:
        ori = 0  #this is orientation of the grating
        correctAns = 'left'
    else:
        ori = 90
        correctAns = 'right'
    grating.setColor(level, colorSpace='rgb')
    grating.setSize(stim_diam_degs)
    grating.setOri(ori)
    grating.setSF(SF)
    resp = keyboard.Keyboard()
    # keep track of which components have finished
    trialComponents = [ISI, fixation, grating, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if t >= 0.25 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # not accounting for scr refresh
            fixation.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        frameRemains = 0.25 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
            fixation.setAutoDraw(False)
        
        # *grating* updates
        if t >= 0.5 and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # not accounting for scr refresh
            grating.frameNStart = frameN  # exact frame index
            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            grating.setAutoDraw(True)
        
        # *resp* updates
        if t >= 0.5 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t  # not accounting for scr refresh
            resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            resp.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp.keys = theseKeys.name  # just the last key pressed
                resp.rt = theseKeys.rt
                # was this 'correct'?
                if (resp.keys == str(correctAns)) or (resp.keys == correctAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # not accounting for scr refresh
            ISI.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.25)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
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
    trials.addOtherData('side',correctAns)
    trials.addOtherData('ISI.started', ISI.tStart)
    trials.addOtherData('ISI.stopped', ISI.tStop)
    trials.addOtherData('fixation.started', fixation.tStartRefresh)
    trials.addOtherData('fixation.stopped', fixation.tStopRefresh)
    trials.addOtherData('grating.started', grating.tStartRefresh)
    trials.addOtherData('grating.stopped', grating.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (MultiStairHandler)
    trials.addResponse(resp.corr)
    trials.addOtherData('resp.rt', resp.rt)
    trials.addOtherData('resp.started', resp.tStartRefresh)
    trials.addOtherData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksMsg]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksMsg* updates
    if t >= 0.0 and thanksMsg.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksMsg.tStart = t  # not accounting for scr refresh
        thanksMsg.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanksMsg, 'tStartRefresh')  # time at next scr refresh
        thanksMsg.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksMsg.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        thanksMsg.tStop = t  # not accounting for scr refresh
        thanksMsg.frameNStop = frameN  # exact frame index
        win.timeOnFlip(thanksMsg, 'tStopRefresh')  # time at next scr refresh
        thanksMsg.setAutoDraw(False)
    
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

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
