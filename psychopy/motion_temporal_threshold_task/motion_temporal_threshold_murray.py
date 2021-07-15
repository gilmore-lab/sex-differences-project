#!/usr/bin/env python
# -*-   coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------
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
from psychopy import locale_setup
from psychopy import prefs
from psychopy import core, visual, gui, data, event, sound, clock
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from psychopy.hardware import keyboard
import time, numpy, sys
import os  # handy system and path functions
from scipy.stats import norm

# user-defined parameters
import motion_temporal_threshold_params as params

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
    
def calculate_stim_duration(frames, frameRate):
    return (frames/frameRate)
    
def write_trial_data_header():
    dataFile.write('observer,gender')
    dataFile.write(',run_n,trial_n, motion_dir,grating_ori,key_resp,grating_deg')
    dataFile.write(',contrast,spf,tf_hz,stim_secs,actual_frame, FWHM')
    dataFile.write(',frame_rate_hz,frameDur,correct,rt')
    dataFile.write(',grating_start,grating_end\n')

def write_trial_data_to_file():
    dataFile.write('%s,%s' % (expInfo['Participant'], expInfo['Gender']))
    dataFile.write(',%i,%i,%i,%s,%s,%.2f' % (current_run,n_trials,this_dir,this_dir_str, thisKey, this_grating_degree))
    dataFile.write(',%.3f,%.3f,%.3f,%.9f,%i,%.9f' % (this_max_contrast, this_spf, this_tf, this_stim_secs,frame_n,actual_stim_secs))
    dataFile.write(',%.9f,%.9f,%.2f, %.3f' % (frameRate, frameDur, thisResp, rt))
    dataFile.write(',%.3f,%.3f\n' % ( start_resp_time, clock.getTime()))
    
def calculate_contrast():
    if params.contrast_mod_type == 'fixed_trapezoidal':
        ramp_up_secs = params.frameDur 
        ramp_down_secs = params.frameDur 
        secs_passed = clock.getTime()-start_time
        if this_stim_secs >= 3*params.frameDur:
            if 0 <=secs_passed < ramp_up_secs:
                this_contr =  0.5 * this_max_contrast
            elif this_stim_secs >= secs_passed > this_stim_secs-ramp_down_secs:
                this_contr = 0.5*this_max_contrast
            else:
                this_contr = this_max_contrast
        else:
            this_contr = this_max_contrast
    elif params.contrast_mod_type == 'hybrid_gaussian':
        if this_stim_secs < frameDur*6:  # when sigma=0.015, assume 8 sigma is stimuli duration, it is 120ms, FWHM is 18ms. 
            secs_passed = clock.getTime()-start_time
            sigma=this_stim_secs/6  # 6 sigma
            mu = this_stim_secs/2
            # actual_stim_secs=0.7759*sigma*2
            this_contr = norm.pdf(secs_passed,mu, sigma)*this_condition['max_contr']* numpy.sqrt(2*numpy.pi)*sigma
        else:
            secs_passed = clock.getTime()-start_time
            sigma=frameDur
            mu = 3*sigma
            if secs_passed < mu:
                this_contr = norm.pdf(secs_passed, mu, sigma)*this_condition['max_contr'] * numpy.sqrt(2*numpy.pi)*sigma
            elif secs_passed > (this_stim_secs-mu):
                this_contr = norm.pdf(this_stim_secs-secs_passed, mu, sigma)*this_condition['max_contr']* numpy.sqrt(2*numpy.pi)*sigma
            else:
                this_contr = this_condition['max_contr']
            
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
    
def show_practice_trial():
    win.flip()
    # randomly set motion direction of grating on each trial
    if numpy.random.random() >= 0.5:
        this_dir = +1 # leftward
        this_dir_str='left'
    else:
        this_dir = -1 # rightward
        this_dir_str='right'
    
    this_stim_secs = .5
    this_grating_degree = 4
    this_spf = 1.2
    keep_going = 1
    
    pr_grating = visual.GratingStim(
        win=win, name='grating_murray',units='deg', 
        tex='sin', mask='gauss',
        ori=params.grating_ori, pos=(0, 0), size=this_grating_degree, sf=this_spf, phase=0,
        color=0, colorSpace='rgb', opacity=1, blendmode='avg',
        texRes=128, interpolate=True, depth=0.0)
    
    # fixation until keypress
    fixation.draw()
    win.flip()
    event.waitKeys()
    win.flip()
    
    # ISI
    core.wait(params.fixation_grating_isi)
    
    # show grating
    start_time = clock.getTime()
    while keep_going:
        secs_from_start = (start_time - clock.getTime())
        pr_grating.phase = this_dir*(secs_from_start/params.cyc_secs)
        
        # Modulate contrast
        this_contr = .98
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
                    
            print("Exiting program.")
            core.quit()
    
    # clear screen, get response
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
    #-----------------------------------------------------------------------------------------------------------
    
    win.flip()
    beep.setSound('A', secs=0.2, hamming=True)
    beep.setVolume(0.5)
    if (thisResp == 0):
        instructionsIncorrect.draw()
    else:
        instructionsCorrect.draw()
        # Feedback
        beep.play(when=win)    # Only first plays?
        # donut.draw()            # Try visual feedback for now
    win.flip()
    
    # wait
    core.wait(1)
#-----------------------------------------------------------------------------------------------------------

#dataFile.write('motion_dir,grating_ori,key_resp,grating_deg,contrast,spf,tf_hz,show_frames,frame_rate_hz,show_secs,correct,rt,grating_start,grating_end\n')
#-----------------------------------------------------------------------------------------------------------
# Start experiment
#-----------------------------------------------------------------------------------------------------------

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'motion_temporal_threshold'  # from the Builder filename that created this script
expInfo = {'Participant':'','Gender':''}
# present a dialog to change params
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)  # sortKeys=True: alphabetical order
  # clean up the temporary background  
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# make an output text file to save data
fileName = _thisDir + os.sep + 'motion_temporal_threshold_data' + os.sep + '%s_%s' % (expInfo['Participant'] ,expInfo['expName'])
# An ExperimentHandler isn't essential but helps with data saving
dataFile = open(fileName + '.csv', 'w')
write_trial_data_header()

win = visual.Window([params.window_pix_h, params.window_pix_v],fullscr=True, screen=0, monitor=params.monitor_name, units='deg')
# get the real frame rate of the monitor
frameRate= win.getActualFrameRate()
if frameRate != None:
    frameDur = 1.0 / frameRate
else:
    frameDur = 1.0 / params.frame_rate_hz  # could not measure, so guess
    
# Clock variables
clock = core.Clock()
countDown = core.CountdownTimer()
# Set up hardware
kb = keyboard.Keyboard()
#-----------------------------------------------------------------------------------------------------------
# Start experiment
#-----------------------------------------------------------------------------------------------------------
# sound
beep = sound.Sound('A', secs=0.2, stereo=True, hamming=True)
beep.setVolume(0.5)

# create stimuli
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

# text messages
welcome  = visual.TextStim(win, pos=[0, 0], 
    text = 'Welcome to the motion duration threshold study.\n\nPress SPACE bar to continue.')
instructions1 = visual.TextStim(win, pos=[0, 0], text = 'You will see a small patch of black and white stripes moving leftward or rightward.\n\nPress SPACE bar to continue.')
instructions2 = visual.TextStim(win, pos=[0, 0], text = 'Your need to detect whether the patch is moving to the left or the right.\n\nPress SPACE bar to continue.')
instructions3a = visual.TextStim(win, pos=[0, + 3],
    text='At first, you will see the small black dot appears, look at it. ')
instructions3b = visual.TextStim(win, pos=[0, -3],
    text="Then press SPACE bar to start the display. \n\nPress SPACE bar to continue.")
instructions4 = visual.TextStim(win, pos=[0, 0], text = 'After the small patch of black and white stripes disappear, you will see a white dot. It is the response cue. Once the white dot appears, press the LEFT arrow key if you see leftward motion and the RIGHT arrow key if you see rightward motion.\n\nIf you are not sure, just guess.\n\nYour goal is accuracy, not speed.\n\nPress SPACE bar to continue.')
instructions5 = visual.TextStim(win, pos=[0, 0], text = 'Let us try some easy practice trials. \n\nPress SPACE bar to continue.')
instructionsIncorrect = visual.TextStim(win, pos=[0, 0], text = 'Almost. Make sure to pay close attention.')
instructionsCorrect = visual.TextStim(win, pos=[0, 0], text = 'Awesome.')
instructions6 = visual.TextStim(win, pos=[0, 0], text = 'Good job!\n\n You will hear beep sound with correct answers. Your goal is accuracy, not speed.\n \n Do you have any questions? If not, press SPACE bar to start the real trials!')
instructions_practice=visual.TextStim(win, pos=[0, 0], text = 'Decide whether it is leftward or rightward motion.\n\nWhen you see the black dot, press the SPACE bar to start the display. \nWhen the white dot appears, press the arrow keys to make a response . \n\nLet us have more practice trials. Press SPACE bar to continue.')
thanksMsg = visual.TextStim(win, pos=[0, 0],text="You're done! You can contact the researcher outside the room and feel free to have a break if you need!")

#-----------------------------------------------------------------------------------------------------------
# experiment procedures
#-----------------------------------------------------------------------------------------------------------

# welcome
welcome.draw()
win.flip()
event.waitKeys()
win.flip()

# instructions
instructions1.draw()
win.flip()
event.waitKeys()

instructions2.draw()
win.flip()
event.waitKeys()

instructions3a.draw()
instructions3b.draw()
fixation.draw()
win.flip()
event.waitKeys()

instructions4.draw()
win.flip()
event.waitKeys()

instructions5.draw()
win.flip()
event.waitKeys()

#-----------------------------------------------------------------------------------------------------------
# Show sample 1

# randomly set motion direction of grating on each trial
#if (round(numpy.random.random())) > 0.5:
#    this_dir = +1 # leftward
#    this_dir_str='left'
#else:
#    this_dir = -1 # rightward
#    this_dir_str='right'
#
#this_stim_secs = .5
#this_grating_degree = 4
#this_spf = 1.2
#keep_going = 1
#
#pr_grating = visual.GratingStim(
#    win=win, name='grating_murray',units='deg', 
#    tex='sin', mask='gauss',
#    ori=params.grating_ori, pos=(0, 0), size=this_grating_degree, sf=this_spf, phase=0,
#    color=0, colorSpace='rgb', opacity=1, blendmode='avg',
#    texRes=128, interpolate=True, depth=0.0)
#
#start_time = clock.getTime()
#while keep_going:
#    secs_from_start = (start_time - clock.getTime())
#    pr_grating.phase = this_dir*(secs_from_start/params.cyc_secs)
#    
#    # Modulate contrast
#    this_contr = .98
#    pr_grating.color = this_contr
#
#    # Draw next grating component
#    pr_grating.draw()
#    win.flip()
#    grating_start = clock.getTime()
#
#    # Start collecting responses
#    thisResp = None
#
#    # Is stimulus presentation time over?
#    if (clock.getTime()-start_time > this_stim_secs):
#        win.flip()
#        keep_going = False 
#        
#    # check for quit (typically the Esc key)
#    if kb.getKeys(keyList=["escape"]):
#        thisResp = 0
#        rt = 0
#                
#        print("Exiting program.")
#        core.quit()
#
# clear screen get response
#if params.show_response_frame:
#    respond.draw()
#    win.flip()
#start_resp_time = clock.getTime()
#
# Show response fixation
#while thisResp is None:
#    allKeys = event.waitKeys()
#    rt = clock.getTime() - start_resp_time
#    for thisKey in allKeys:
#        if ((thisKey == 'left' and this_dir == -1) or
#            (thisKey == 'right' and this_dir == +1)):
#            thisResp = 0 # incorrect
#        elif ((thisKey == 'left' and this_dir == +1) or
#            (thisKey == 'right' and this_dir == -1)):
#            thisResp = 1  # correct
#            
#            # Feedback
#            highA.play(loops=-1)    # Only first plays?
#            donut.draw()            # Try visual feedback for now
#        elif thisKey in ['q', 'escape']:
#            test = False
#            core.quit()  # abort experiment
#-----------------------------------------------------------------------------------------------------------

show_practice_trial()
show_practice_trial()
show_practice_trial()
show_practice_trial()
show_practice_trial()
instructions_practice.draw()
win.flip()
event.waitKeys()
show_practice_trial()
show_practice_trial()
show_practice_trial()
show_practice_trial()
show_practice_trial()

instructions6.draw()
win.flip()
event.waitKeys()

# Start staircase
current_run=0
total_run=range(4)
for current_run in total_run:
    # create the staircase handler
    if params.staircase_style == 'QUEST':
        staircase = data.MultiStairHandler(stairType='QUEST', conditions=params.conditions_QUEST,  nTrials=params.staircase_ntrials)
    else:
        staircase = data.MultiStairHandler(stairType='simple', conditions=params.conditions_simple, nTrials=params.staircase_ntrials)
    print('Created staircase: %s' % params.staircase_style)
    n_trials = 0
    for this_stim_secs, this_condition in staircase:
        frame_n=0
        # Print trial number, condition info to console
        n_trials += 1
        print('trial:', str(n_trials), 'condition: ' + this_condition['label'] + " | " + 'stim_secs: ' + str(this_stim_secs))
        
        # Initialize grating parameters for this condition
        this_max_contrast = this_condition['max_contr']
        this_grating_degree = this_condition['grating_deg']
        this_tf = this_condition['tf']
        this_spf = this_condition['spf']
    
        # randomly set motion direction of grating on each trial
        if numpy.random.random() >= 0.5:
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
        
        # Show fixation until key press
        fixation.draw()
        win.flip()
        event.waitKeys()
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
            if this_contr>=0.5*this_condition['max_contr']:
                frame_n+=1
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
                    beep.setSound('A', secs=0.15, hamming=True)
                    beep.setVolume(0.5)
                    # Feedback
                    beep.play(when=win)    # Only first plays?
                    # donut.draw()            # Try visual feedback for now
                    win.flip()
                elif thisKey in ['q', 'escape']:
                    test = False
                    core.quit()  # abort experiment
            event.clearEvents('mouse')  # only really needed for pygame windows
            win.mouseVisible = False
    
        # add the data to the staircase so it can calculate the next level
        staircase.addResponse(thisResp)
        if this_stim_secs < frameDur*6:  # when sigma=0.015, assume 8 sigma is stimuli duration, it is 120ms, FWHM is 18ms. 
            sigma=this_stim_secs/6
        else:
            sigma=frameDur
        actual_stim_secs=this_stim_secs-(6*sigma-0.7759*sigma*2)
        # Write data to file
        write_trial_data_to_file()
    
        # Clear screen and ITI
        win.flip()
        core.wait(rand_unif_int(params.iti_min, params.iti_max))
        # core.wait(params.fixation_grating_isi)
    if current_run<3:
        message='Well done! You have finished Session %i. \n\nPress SPACE bar to continue.'%(current_run+1)
        intru_break = visual.TextStim(win, pos=[0, 0], text = message)
        intru_break.draw()
        win.flip()
        event.waitKeys()
    current_run=current_run+1
#-----------------------------------------------------------------------------------------------------------
thanksMsg.draw()
win.flip()
event.waitKeys()
#-----------------------------------------------------------------------------------------------------------
# Save data and clean-up
#-----------------------------------------------------------------------------------------------------------

# staircase has ended
dataFile.close()
staircase.saveAsPickle(fileName)  # special python data file to save all the info

# give some output to user
if params.staircase_style == 'simple':
    print('reversals:')
    print(staircase.reversalIntensities)
    print('mean of final 5 reversals = %.3f' % numpy.average(staircase.reversalIntensities[-5:]))

# clean-up
win.close()
core.quit()
