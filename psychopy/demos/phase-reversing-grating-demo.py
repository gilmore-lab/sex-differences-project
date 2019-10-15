#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.4),
    on Mon Jul  8 16:05:00 2019
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
#expName = 'sinusoidal_grating_S1_T1'  # from the Builder filename that created this script
#expInfo = {'participant': '', 'session': '001'}
#dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
#if dlg.OK == False:
#    core.quit()  # user pressed cancel
#expInfo['date'] = data.getDateStr()  # add a simple timestamp
#expInfo['expName'] = expName
#expInfo['psychopyVersion'] = psychopyVersion
#
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
#
# An ExperimentHandler isn't essential but helps with data saving
#thisExp = data.ExperimentHandler(name=expName, version='',
#    extraInfo=expInfo, runtimeInfo=None,
#    originPath='/Users/yimingqian/Documents/sinusoidal_grating_1.py',
#    savePickle=True, saveWideText=True,
#    dataFileName=filename)
# save a log file for detail verbose info
#logFile = logging.LogFile(filename+'.log', level=logging.EXP)
#logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
#expInfo['frameRate'] = 1 #1HZ
#if expInfo['frameRate'] != None:
#    frameDur = 1.0 / round(expInfo['frameRate'])
#else:
#    frameDur = 1.0 / 1.0  # could not measure, so guess

frameDur = 1/60
# Contrast ramps up from 0 for ramp_up_secs, remains at max_contr for full_scale_secs and ramps down for ramp_dn_secs
# note sum(ramp_up_secs, full_scale_secs, ramp_dn_secs) = stim_dur_secs
stim_dur_secs = 2
ramp_up_secs = .5
full_scale_secs = 1
ramp_dn_secs = ramp_up_secs
tf = 1 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
iti = 3.0 # seconds
max_contr = 0.5

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
pr_grating = visual.GratingStim(
    win=win, name='grating_S1_T5',units='deg', 
    tex='sin', mask='circle',
    ori=90, pos=(0, 0), size=(3.5, 3.5), sf=0.6, phase=0,
    color=[max_contr,max_contr,max_contr], colorSpace='rgb', opacity=1, blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)

clock = core.Clock()
countDown = core.CountdownTimer()

# Grating: 20 Hz; 2.5% max contrast; horizontal
keep_going = True
tf = 20 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .025
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False
        

# Intertrial interval
countDown.add(iti)
while countDown.getTime() > 0:
    pass

# Grating: 20 Hz; 5% max contrast; vertical
keep_going = True
tf = 20 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .05
pr_grating.ori = 0.0
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False

# Intertrial interval
countDown.add(iti)
while countDown.getTime() > 0:
    pass

# Grating: 20 Hz; 10% max contrast; vertical
keep_going = True
tf = 24 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .10
pr_grating.ori = 0.0
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False

# Intertrial interval
countDown.add(iti)
while countDown.getTime() > 0:
    pass

# Grating: 10 Hz; 10% max contrast; vertical
keep_going = True
tf = 8 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .10
pr_grating.ori = 90.0
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False

# Intertrial interval
countDown.add(iti)
while countDown.getTime() > 0:
    pass

# Grating: 5 Hz; 5% max contrast; vertical
keep_going = True
tf = 4 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .05
pr_grating.ori = 90.0
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False

# Intertrial interval
countDown.add(iti)
while countDown.getTime() > 0:
    pass

# Grating: 5 Hz; 5% max contrast; vertical
keep_going = True
tf = 1 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .05
pr_grating.ori = 90.0
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False

# Intertrial interval
countDown.add(iti)
while countDown.getTime() > 0:
    pass

# Grating: 5 Hz; 5% max contrast; vertical
keep_going = True
tf = 24 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .05
pr_grating.ori = 90.0
pr_grating.sf = 0.5
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False
        
# Intertrial interval
countDown.add(iti)
while countDown.getTime() > 0:
    pass

# Grating: 5 Hz; 5% max contrast; vertical
keep_going = True
tf = 8 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
max_contr = .05
pr_grating.ori = 90.0
pr_grating.sf = 0.5
start_time = clock.getTime()
while keep_going:
    pr_grating.phase = round(np.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
    # Contrast ramp in, hold, down
    secs_passed = clock.getTime()-start_time
    if secs_passed <= ramp_up_secs:
        contr = (secs_passed/ramp_up_secs)*max_contr
    elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
        contr = max_contr
    else:
        contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*max_contr
    pr_grating.color = [contr, contr, contr]
    
    pr_grating.draw()
    win.flip()
    
    keys = event.getKeys
    # handle keypress
    #    if len(keys) > 0:
    #        keep_going = False
    if (clock.getTime()-start_time > stim_dur_secs):
        keep_going = False
        

win.close()
core.quit()
