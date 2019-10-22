#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------
# 
# 
# 
#-----------------------------------------------------------------------------------------------------------
"""
This code is an attempt to replicate the Murray et al. 2018 study on sex differences in temporal motion detection thresholds.

Murray, S. O., Schallmo, M.-P., Kolodny, T., Millin, R., Kale, A., Thomas, P., Rammsayer, T. H., et al. (2018). 
Sex Differences in Visual Motion Processing. Current Biology, 28(17), 2794-2799.
Retrieved from http://dx.doi.org/10.1016/j.cub.2018.06.014
"""

#-----------------------------------------------------------------------------------------------------------
# Initialize
#-----------------------------------------------------------------------------------------------------------

# import external packages
from __future__ import absolute_import, division, print_function
from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from psychopy.hardware import keyboard
import time, numpy

# user-defined parameters
import params

# Set up hardware
kb = keyboard.Keyboard()

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    expInfo = {'observer':time.strftime("%Y%m%d%H%M%S"),'gender':'M'}

# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='Motion Temporal threshold', fixed=['date'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make an output text file to save data
fileName = 'csv/' + expInfo['observer'] + "_" + params.task_name
dataFile = open(fileName + '.csv', 'w')
dataFile.write('motion_dir,grating_ori,key_resp,grating_deg,contrast,spf,tf_hz,show_frames,frame_rate_hz,show_secs,correct,rt,grating_start,grating_end\n')

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
win = visual.Window([params.window_pix_h, params.window_pix_v], allowGUI=False, monitor=params.monitor_name, units='deg')
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
respond = visual.GratingStim(win, color='white', tex=None, mask='circle', size=0.3)

pr_grating = visual.GratingStim(
    win=win, name='grating_murray',units='deg', 
    tex='sin', mask='gauss',
    ori=params.grating_ori, pos=(0, 0), size=params.grating_deg, sf=params.spf, phase=0,
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

n_trials = 0

# Start staircase
for this_stim_secs, this_condition in staircase:
    
    # Print trial number, condition info to console
    n_trials += 1
    print('trial :', str(n_trials), 'condition: ' + this_condition['label'] + " | " + 'stim_secs: ' + str(this_stim_secs))
    
    # Initialize grating parameters for this condition
    this_max_contrast = this_condition['max_contr']
    this_grating_degree = this_condition['grating_deg']
    this_tf = this_condition['tf']
    this_spf = this_condition['spf']

    # randomly set motion direction of grating on each trial
    if (round(numpy.random.random())) > 0.5:
        this_dir = +1 # leftward
        this_dir_str='left'
    else:
        this_dir = -1 # rightward
        this_dir_str='right'
    
    # draw initial grating
    pr_grating = visual.GratingStim(
        win=win, name='grating_murray',units='deg', 
        tex='sin', mask=this_condition['mask_type'],
        ori=params.grating_ori, pos=(0, 0), size=this_grating_degree, sf=this_spf, phase=0,
        color=0, colorSpace='rgb', opacity=1, blendmode='avg',
        texRes=128, interpolate=True, depth=0.0)
    
    # Show fixation
    fixation.draw()
    win.flip()
    
    # Hide fixation
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
        
        # Modulate contrast
        this_contr = calculate_contrast()
        pr_grating.color = this_contr

        # Draw next grating component
        pr_grating.draw()
        win.flip()
        grating_start = clock.getTime()

        # Start collecting responses
        thisResp = None

        # Is stimulus presentation time over?
        if (clock.getTime()-start_time > this_stim_secs):
            win.flip()
            keep_going = False 
            
        # check for quit (typically the Esc key)
        if kb.getKeys(keyList=["escape"]):
            thisResp = 0
            rt = 0
            
            print("Saving data.")
            write_trial_data_to_file()
            
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
    
    # Write data to file
    write_trial_data_to_file()

    # Clear screen and ITI
    win.flip()
    core.wait(rand_unif_int(params.iti_min, params.iti_max))
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
# Save data and clean-up
#-----------------------------------------------------------------------------------------------------------

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
