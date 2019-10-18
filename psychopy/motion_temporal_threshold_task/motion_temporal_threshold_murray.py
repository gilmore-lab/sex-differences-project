#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This code is an attempt to replicate the Murray et al. 2018 study on sex differences in temporal motion detection thresholds.

Murray, S. O., Schallmo, M.-P., Kolodny, T., Millin, R., Kale, A., Thomas, P., Rammsayer, T. H., et al. (2018). 
Sex Differences in Visual Motion Processing. Current Biology, 28(17), 2794-2799.
Retrieved from http://dx.doi.org/10.1016/j.cub.2018.06.014
"""

from __future__ import absolute_import, division, print_function
from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from psychopy.hardware import keyboard
import time, numpy

# Parameters
import params

# Set up hardware
kb = keyboard.Keyboard()

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    expInfo = {'observer':time.strftime("%Y%m%d%H%M%S"),'gender':'M'}

# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='simple JND Exp', fixed=['date'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make a text file to save data
fileName = 'csv/' + expInfo['observer'] + "_" + params.task_name
dataFile = open(fileName + '.csv', 'w')
dataFile.write('direction,cyc_deg,tf_hz,show_secs,correct,rt\n')

# Helper functions
def rand_unif_int(min, max):
    # Force min >= 0 and max >= 0
    if min < 0:
        min = 0
    if max < 0:
        max = 0
    return (min + numpy.random.random()*(max-min))
    
def calculate_stim_duration(frames, frame_rate_hz):
    if frame_rate_hz == 0:
        frame_rate_hz = 60
    return (frames/frame_rate_hz)

# Clock variables
clock = core.Clock()
countDown = core.CountdownTimer()

# create window and stimuli
win = visual.Window([params.window_pix_h, params.window_pix_v], allowGUI=False, monitor=params.monitor_name, units='deg')
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
respond = visual.GratingStim(win, color='white', tex=None, mask='circle', size=0.3)

pr_grating = visual.GratingStim(
    win=win, name='grating_murray',units='deg', 
    tex='sin', mask='gauss',
    ori=90, pos=(0, 0), size=params.grating_deg, sf=params.spf, phase=0,
    color=[params.max_contr, params.max_contr, params.max_contr], colorSpace='rgb', opacity=1, blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)
    
# `donut` has a true hole, using two loops of vertices:
donutVert = [[(-params.donut_outer_rad,-params.donut_outer_rad),(-params.donut_outer_rad,params.donut_outer_rad),(params.donut_outer_rad,params.donut_outer_rad),(params.donut_outer_rad,-params.donut_outer_rad)],
[(-params.donut_inner_rad,-params.donut_inner_rad),(-params.donut_inner_rad,params.donut_inner_rad),(params.donut_inner_rad,params.donut_inner_rad),(params.donut_inner_rad,-params.donut_inner_rad)]]
donut = ShapeStim(win, vertices=donutVert, fillColor=params.donut_color, lineWidth=0, size=.75, pos=(0, 0))

message1 = visual.TextStim(win, pos=[0, + 3],
    text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0, -3],
    text="When the white box appears, press LEFT arrow to identify leftward motion or the RIGHT arrow to identify rightward motion.")

# create the staircase handler
#staircase = data.StairHandler(startVal=20, # stimulus duration in frames
#    stepType='db',
#    stepSizes=[8, 4, 4, 2, 2, 1, 1],  # reduce step size every two reversals
#    minVal=2, maxVal=40,
#    nUp=1, nDown=3,  # will home in on the 80% threshold
#    nTrials=40)
    
#if params.stair_case_style == 'quest':
#    staircase = data.MultiStairHandler(stairType='quest', conditions=params.conditions_QUEST, 
#    minVal=2, maxVal=40, pThreshold=0.63, nTrials=50)
#else:
#    staircase = data.MultiStairHandler(stairType='simple', conditions=params.conditions_simple, nTrials=50)
#    
staircase = data.QuestHandler(0.5, 0.2, pThreshold=0.63, gamma=0.01,
                              minVal=0, maxVal=1, ntrials=10)

# display instructions and wait
message1.draw()
message2.draw()
fixation.draw()
win.flip()

# check for a keypress, then proceed
event.waitKeys()

# Start staircase
#for this_stim_frames_p, this_condition in staircase:
for this_stim_frames_p in staircase:
    # Initialize grating
    this_stim_frames = this_stim_frames_p*20
    print(calculate_stim_duration(this_stim_frames, params.frame_rate_hz))
    #print(this_condition)
    #this_max_contrast = this_condition['max_contr']
    this_max_contrast = .98

    # set orientation of grating
    if (round(numpy.random.random())) > 0.5:
        this_dir = +1 # leftward
    else:
        this_dir = -1 # rightward
        
    # pick spf randomly (for now)
    this_spf = params.spfreqs[0]
#    if (round(numpy.random.random())) > 0.5:
#        this_spf = params.spfreqs[0]
#    else:
#        this_spf = params.spfreqs[1]
    #this_max_contrast = .98
 
    pr_grating = visual.GratingStim(
        win=win, name='grating_murray',units='deg', 
        tex='sin', mask='circle',
        ori=params.grating_ori, pos=(0, 0), size=params.grating_deg, sf=this_spf, phase=0,
        color=[this_max_contrast, this_max_contrast, this_max_contrast], colorSpace='rgb', opacity=1, blendmode='avg',
        texRes=128, interpolate=True, depth=0.0)
    
    # Pick tf and max contrast
    this_tf = params.tfreqs[0]
    
    # Show fixation
    fixation.draw()
    win.flip()
    core.wait(params.fixation_secs)
    win.flip()
    
    # ISI (uniform within [isi_min, isi_max])
    core.wait(params.fixation_grating_isi)
    
    # draw grating
    keep_going = True
    start_time = clock.getTime()
    while keep_going:
        secs_from_start = (start_time - clock.getTime())
        pr_grating.phase = this_dir*(secs_from_start/params.cyc_secs)
        #pr_grating.contrast = numpy.sin(2 * numpy.pi * t * this_tf) # from counterphase.py demo
        
        # Contrast ramp in, hold, down
        secs_passed = clock.getTime()-start_time
        if secs_passed <= params.ramp_up_secs:
            this_contr = (secs_passed/params.ramp_up_secs)*this_max_contrast
        elif (secs_passed > params.ramp_up_secs) & (secs_passed <= params.ramp_up_secs + params.full_scale_secs):
            this_contr = this_max_contrast
        else:
            this_contr = ((params.stim_dur_secs - secs_passed)/params.ramp_up_secs)*this_max_contrast
        pr_grating.color = this_contr
    
        # Draw next grating component
        pr_grating.draw()
        win.flip()
        grating_start = clock.getTime()

        # Start collecting responses
        thisResp = None

        # Is stimulus presentation time over?
        if (clock.getTime()-start_time > this_stim_frames*params.frameDur):
            win.flip()
            keep_going = False
            
        # check for quit (typically the Esc key)
        if kb.getKeys(keyList=["escape"]):
            thisResp = 0
            rt = 0
            print("Saving data.")
            dataFile.write('%i,%.3f,%i,%.3f,%i,%.3f\n' % (this_dir, this_spf, this_tf, this_stim_frames*params.frameDur, thisResp, rt))
            staircase.saveAsPickle(fileName)  # special python data file to save all the info
            print("Exiting program.")
            core.quit()

    # clear screen get response
    if params.show_response_frame:
        respond.draw()
        win.flip()
    start_resp_time = clock.getTime()
    
    # Show response fixation
    while thisResp is None:
        allKeys = event.waitKeys()
        rt = clock.getTime() - start_resp_time
        for thisKey in allKeys:
            if ((thisKey == 'left' and this_dir == -1) or
                (thisKey == 'right' and this_dir == +1)):
                thisResp = 0 # incorrect
            elif ((thisKey == 'left' and this_dir == +1) or
                (thisKey == 'right' and this_dir == -1)):
                thisResp = 1  # correct
            elif thisKey in ['q', 'escape']:
                test = False
                core.quit()  # abort experiment
        event.clearEvents('mouse')  # only really needed for pygame windows

    # add the data to the staircase so it can calculate the next level
    staircase.addResponse(thisResp)
    dataFile.write('%i,%i,%i,%.3f,%i,%.3f\n' % (this_dir, this_spf, this_tf, this_stim_frames*params.frameDur, thisResp, rt))
    
    # Clear screen and ITI
    win.flip()
    core.wait(rand_unif_int(params.iti_min, params.iti_max))

# staircase has ended
dataFile.close()
staircase.saveAsPickle(fileName)  # special python data file to save all the info

# give some output to user
print('reversals:')
print(staircase.reversalIntensities)
print('mean of final 6 reversals = %.3f' % numpy.average(staircase.reversalIntensities[-6:]))

# clean-up
win.close()
core.quit()
