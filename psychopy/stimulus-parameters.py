#================================================
# Task 1 
# 
# Adaptation/replication of 
#
# Abramov, I., Gordon, J., Feldman, O., & Chavarga, A. (2012). Sex & vision I: 
# Spatio-temporal resolution. Biology of sex differences, 3(1), 20. 
# bsd.biomedcentral.com. Retrieved from http://dx.doi.org/10.1186/2042-6410-3-20

#-------------------------------------------------
# Stimulus description
#
# Phase reversing grating
# Vary contrast adaptively
# Varying other parameters according to fixed conditions
# Self-paced
# catch trials(contrast fixed at 45%)  # This is used in the contrast sensitivity task in Murray et al., 2018


# Constant parameters
# view_distance_cm = 60
# stim_duration_secs = 2
# surround_diam_degs = [13,13]
# grating_phase = 0
# tf = [1] # temporal frequency Hz

# Variable parameters
# grating_contrast = QUEST algorithm (80% accuracy)
# sf = [1.2, 12] # grating spatial frequency in cyc/deg
# ori = [0, 90] # grating orientation vertical or horizontal
# stim_diam_degs = [2, 12] # deg to compare with Murray et al. 2018

#================================================
# Task 2 
# 
# Adaptation/replication of 
#
# Murray, S. O., Schallmo, M.-P., Kolodny, T., Millin, R., Kale, A., Thomas, P., Rammsayer, T. H., et al. (2018). 
# Sex Differences in Visual Motion Processing. Current biology: CB. Retrieved from http://dx.doi.org/10.1016/j.cub.2018.06.014
#
#-------------------------------------------------
# Stimulus description
# Gratings were presented within a circular aperture, whose edges were blurred with a Gaussian envelope (SD = 0.21).
# variable duration controlled by a staircase procedure (a trapezoidal temporalenvelope), range 6.7 – 333 ms
# Response time was not limited.
# 10 catch trials per run (all 10 diameter, 98% contrast gratings, 333 ms duration)

# Constant parameters
# view_distance_cm = 60
# stim_duration_secs = QUEST algorithm (80% accuracy)
# surround_diam_degs = [13,13]
# grating_phase = 0
# speed = [4] # grating speed in 4 cycle/s

# Variable parameters
# grating_contrast = [3, 98]
# tf = [?] # temporal frequency Hz
# sf = [1.2, 12] # grating spatial frequency in cycle/deg
# ori = [0, 180] # grating orientation left or right
# stim_diam_degs = [2, 12] 
