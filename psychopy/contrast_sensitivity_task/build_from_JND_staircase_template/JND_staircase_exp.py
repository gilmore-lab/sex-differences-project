#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Measure your JND in contrast using a staircase method
"""

from __future__ import absolute_import, division, print_function

from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
import time, numpy

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    expInfo = {'observer':'jwp', 'refOrientation':0}
dateStr = time.strftime("%b_%d_%H%M", time.localtime())  # add the current time

# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='simple JND Exp', fixed=['date'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make a text file to save data
fileName = expInfo['observer'] + dateStr
dataFile = open(fileName + '.txt', 'w')
dataFile.write('targetSide,oriIncrement,correct,RT\n')

# Parameters
stim_dur_secs = 2
ramp_up_secs = .5
full_scale_secs = 1
ramp_dn_secs = ramp_up_secs
tf = 1 # Hz, so stim_dur is 1/freq_temp
cyc_secs = 1/tf # in seconds
iti = 3.0 # seconds
max_contr = 0.5
end_exp_now = False

# Clock variables
clock = core.Clock()
countDown = core.CountdownTimer()

# create window and stimuli
win = visual.Window([800, 600], allowGUI=False, monitor='testMonitor', units='deg')
fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.2)
pr_grating = visual.GratingStim(
    win=win, name='grating_S1_T5',units='deg', 
    tex='sin', mask='circle',
    ori=90, pos=(0, 0), size=(3.5, 3.5), sf=0.6, phase=0,
    color=[max_contr, max_contr, max_contr], colorSpace='rgb', opacity=1, blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)

message1 = visual.TextStim(win, pos=[0, + 3],
    text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0, -3],
    text="Then press LEFT arrow to identify a horizontal grating; UP arrow to identify a vertical grating.")

# create the staircase handler
staircase = data.StairHandler(startVal=0.5, # contrast in [0,1]
    stepType='db',
    stepSizes=[8, 4, 4, 2, 2, 1, 1],  # reduce step size every two reversals
    minVal=0.0001, maxVal=1.0,
    nUp=1, nDown=3,  # will home in on the 80% threshold
    nTrials=20)

# display instructions and wait
message1.draw()
message2.draw()
fixation.draw()
win.flip()
# check for a keypress, then proceed
event.waitKeys()

# Start staircase
for this_max_contrast in staircase:
    # Initialize grating
    
    # set orientation of grating
    if (round(numpy.random.random())) > 0.5:
        this_ori = 90
    else:
        this_ori = 0

    pr_grating = visual.GratingStim(
        win=win, name='grating_S1_T5',units='deg', 
        tex='sin', mask='circle',
        ori=this_ori, pos=(0, 0), size=(3.5, 3.5), sf=0.6, phase=0,
        color=[this_max_contrast, this_max_contrast, this_max_contrast], colorSpace='rgb', opacity=1, blendmode='avg',
        texRes=128, interpolate=True, depth=0.0)
        
    # Show fixation
    fixation.draw()
    win.flip()
    
    # ISI
    core.wait(.5)
    
    # draw grating
    keep_going = True
    start_time = clock.getTime()
    while keep_going:
        pr_grating.phase = round(numpy.mod(clock.getTime(), cyc_secs)/cyc_secs)/2 # need value of 0 or 0.5 to switch phase
    
        # Contrast ramp in, hold, down
        secs_passed = clock.getTime()-start_time
        if secs_passed <= ramp_up_secs:
            this_contr = (secs_passed/ramp_up_secs)*this_max_contrast
        elif (secs_passed > ramp_up_secs) & (secs_passed <= ramp_up_secs + full_scale_secs):
            this_contr = this_max_contrast
        else:
            contr = ((stim_dur_secs - secs_passed)/ramp_up_secs)*this_max_contrast
        pr_grating.color = [this_contr, this_contr, this_contr]
    
        # Draw next grating component
        pr_grating.draw()
        win.flip()
        grating_start = clock.getTime()

        
        # Start collecting responses
        thisResp = None

        
        # Is stimulus presentation time over?
        if (clock.getTime()-start_time > stim_dur_secs):
            win.flip()
            keep_going = False
            
     
#    # check for quit (typically the Esc key)
#    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
#        core.quit()

    # clear screen get response
    while thisResp is None:
        allKeys = event.waitKeys()
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
    #thisResp = 1
    staircase.addResponse(thisResp)
    dataFile.write('%i,%.3f,%i\n' % (this_ori, this_max_contrast, thisResp))

# staircase has ended
dataFile.close()
staircase.saveAsPickle(fileName)  # special python data file to save all the info

# give some output to user
print('reversals:')
print(staircase.reversalIntensities)
print('mean of final 6 reversals = %.3f' % numpy.average(staircase.reversalIntensities[-6:]))

win.close()
core.quit()
