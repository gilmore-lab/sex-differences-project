#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This code is an attempt to replicate the Abramov et al. 2012 study on spatiotemporal contrast sensitivity thresholds.

Abramov, I., Gordon, J., Feldman, O., & Chavarga, A. (2012). Sex & vision I: Spatio-temporal resolution. Biology of Sex Differences, 3(1), 20. 
bsd.biomedcentral.com. Retrieved from http://dx.doi.org/10.1186/2042-6410-3-20
"""

from __future__ import absolute_import, division, print_function
from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from psychopy.hardware import keyboard
import time, numpy

# user defined parameters
import contrast_sensitivity_params as params

# Set up hardware
kb = keyboard.Keyboard()

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    expInfo = {'observer':time.strftime("%Y%m%d%H%M%S"),'gender':'M'}
#dateStr = time.strftime("%b_%d_%H%M", time.localtime())  # add the current time

# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='simple JND Exp', fixed=['date'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make a text file to save data
fileName = 'csv/' + expInfo['observer']
dataFile = open(fileName + '.csv', 'w')
dataFile.write('ori,cyc_deg,tf_hz,contrast,correct,rt\n')

#-----------------------------------------------------------------------------------------------------------
# Define helper functions
#-----------------------------------------------------------------------------------------------------------

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
    
def write_trial_data_to_file():
    dataFile.write('%i,%i,%s,%2.2f' % (this_dir, params.grating_ori, thisKey, this_grating_degree))
    dataFile.write(',%.3f,%.3f,%.3f,%i' % (this_contr, this_spf, this_tf, this_stim_secs))
    dataFile.write(',%.3f,%.3f,%i,%.3f' % (params.frameDur, 0, thisResp, rt))
    dataFile.write(',%.3f,%.3f\n' % (start_resp_time, clock.getTime()))
    
def calculate_contrast():
    if params.contrast_mod_type == 'fixed_trapezoidal':
        secs_passed = clock.getTime()-start_time
        if secs_passed <= params.ramp_up_secs:
            this_contr = (secs_passed/params.ramp_up_secs)*this_max_contrast
        elif (secs_passed > params.ramp_up_secs) & (secs_passed <= params.ramp_up_secs + params.full_scale_secs):
            this_contr = this_max_contrast
        else:
            this_contr = ((params.stim_dur_secs - secs_passed)/params.ramp_up_secs)*this_max_contrast
    elif params.contrast_mod_type == 'variable_triangular': # linear ramp up for half of this_stim_secs, then ramp down
        secs_passed = clock.getTime()-start_time
        if secs_passed <= this_stim_secs * 0.5: # first half
            this_contr = (secs_passed/(this_stim_secs*0.5))*this_max_contrast
        else: 
            this_contr = (this_stim_secs - secs_passed )/(this_stim_secs * 0.5)*this_max_contrast
    else:
        this_contr = this_condition['max_contr']
        
    # Sanity check on this_contr to keep in [0.1]
    if this_contr > 1:
        this_contr = 1
    elif this_contr < 0:
        this_contr = 0
        
    return(this_contr)
#-----------------------------------------------------------------------------------------------------------

# Clock variables
clock = core.Clock()
countDown = core.CountdownTimer()

# create window and stimuli
monitor_name = 'testMonitor'
window_pix_h = 800
window_pix_v = 600
frameDur = 1/60
win = visual.Window([params.window_pix_h, params.window_pix_v], allowGUI=False, monitor=params.monitor_name, units='deg')
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
pr_grating = visual.GratingStim(
    win=win, name='phase_reverse_grating',units='deg', 
    tex='sin', mask='circle',
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
    text="When the white box appears, press LEFT arrow to identify a horizontal grating or the UP arrow to identify a vertical grating.")

# create the staircase handler
if params.stair_case_style == 'quest':
    staircase = data.MultiStairHandler(stairType='quest', conditions=params.conditions_QUEST,  nTrials=50)
else:
    staircase = data.MultiStairHandler(stairType='simple', conditions=params.conditions_simple, nTrials=50)

#-----------------------------------------------------------------------------------------------------------
# Start experiment
#-----------------------------------------------------------------------------------------------------------

# display instructions and wait
message1.draw()
message2.draw()
fixation.draw()
win.flip()

# check for a keypress, then proceed
event.waitKeys()

# Start staircase
n_trials = 0
for this_max_contrast, this_condition in staircase:

    # Print trial number, condition info to console
    n_trials += 1
    print('trial :', str(n_trials), 'condition: ' + this_condition['label'] + " | " + 'stim_secs: ' + str(this_stim_secs))
 
    # Initialize grating
    
    # set orientation of grating
    if (round(numpy.random.random())) > 0.5:
        this_ori = 90
    else:
        this_ori = 0
        
    # pick spf randomly (for now)
    if (round(numpy.random.random())) > 0.5:
        this_spf = params.spfreqs[0]
    else:
        this_spf = params.spfreqs[1]
 
    pr_grating = visual.GratingStim(
        win=win, name='phase_reverse_grating',units='deg', 
        tex='sin', mask='circle',
        ori=this_ori, pos=(0, 0), size=params.grating_deg, sf=this_spf, phase=0,
        color=[this_max_contrast, this_max_contrast, this_max_contrast], colorSpace='rgb', opacity=1, blendmode='avg',
        texRes=128, interpolate=True, depth=0.0)
    
    # Pick tf randomly (for now)
    this_tf = params.tfreqs[round(numpy.random.random())]
    
    # Show fixation
    fixation.draw()
    win.flip()
    
    # ISI (uniform within [isi_min, isi_max])
    core.wait(params.isi_min + numpy.random.random()*(params.isi_max-params.isi_min))
    
    # draw grating
    keep_going = True
    start_time = clock.getTime()
    while keep_going:
        t = clock.getTime()
        pr_grating.phase = round(numpy.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
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
        if (clock.getTime()-start_time > params.stim_dur_secs):
            win.flip()
            keep_going = False
            
        # check for quit (typically the Esc key)
        if kb.getKeys(keyList=["escape"]):
            thisResp = 0
            rt = 0
            print("Saving data.")
            dataFile.write('%i,%i,%i,%.3f,%i,%.3f\n' % (this_ori, this_spf, this_tf, this_max_contrast, thisResp, rt))
            staircase.saveAsPickle(fileName)  # special python data file to save all the info
            print("Exiting program.")
            core.quit()

    # clear screen get response
    donut.draw()
    win.flip()
    start_resp_time = clock.getTime()
    
    while thisResp is None:
        allKeys = event.waitKeys()
        rt = clock.getTime() - start_resp_time
        for thisKey in allKeys:
            if ((thisKey == 'left' and this_ori == 90) or
                (thisKey == 'up' and this_ori == 0)):
                thisResp = 1  # correct
            elif ((thisKey == 'left' and this_ori == 0) or
                (thisKey == 'up' and this_ori == 90)):
                thisResp = 0  # incorrect
            elif thisKey in ['q', 'escape']:
                test = False
                core.quit()  # abort experiment
        event.clearEvents('mouse')  # only really needed for pygame windows

    # add the data to the staircase so it can calculate the next level
    staircase.addResponse(thisResp)
    dataFile.write('%i,%i,%i,%.3f,%i,%.3f\n' % (this_ori, this_spf, this_tf, this_max_contrast, thisResp, rt))
    
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
