# Murray et al. parameters

"""
This code is an attempt to replicate the Murray et al. 2018 study on sex differences in temporal motion detection thresholds.

Murray, S. O., Schallmo, M.-P., Kolodny, T., Millin, R., Kale, A., Thomas, P., Rammsayer, T. H., et al. (2018). 
Sex Differences in Visual Motion Processing. Current biology: CB. 
Retrieved from http://dx.doi.org/10.1016/j.cub.2018.06.014
"""
# from psychopy import visual
# testMonitor
monitor_name = 'testMonitor'
window_pix_h = 800
window_pix_v = 600
# win = visual.Window([window_pix_h, window_pix_v], allowGUI=False, monitor=monitor_name, units='deg')

# fimi_grayscale
#monitor_name = 'fimi_grayscale'
#window_pix_h = 1280
#window_pix_v = 1024
#frameDur = 1/85
frame_rate_hz = 85

# Data file parameters
task_name = "temp_thresh"               # Murray et al. temporal threshold

# Fixation
fixation_secs = .850                    # Fixation duration
fixation_grating_isi = .15              # Fixation/grating ISI

#--- Grating
#contrast_mod_type = 'fixed_trapezoidal' # Ramp up, constant, ramp down, e.g., Abramov et al. 2012
# stim_dur_secs = 2                       # Total grating duration
# ramp_up_secs = frameDur                       # Ramp up duration
# full_scale_secs = 1                     # Full-scale (constant contrast) duration
# ramp_dn_secs = frameDur             # Ramp down duration

contrast_mod_type = 'hybrid_gaussian'  # 'variable_triangular', 'fixed_trapezoidal', 'hybrid_gaussian'

grating_deg = 3.5
max_contr = .98
spf = 1.2
mask_type = 'gauss'                    # 'circle' or 'gauss'
gaussian_sd = 0.2
grating_ori = 0                         # grating orientation in deg, 0 is vertical, 90 is horizontal
tf = 4                                  # Hz or cycles/second
cyc_secs = 1/tf                         # seconds for one full cycle

max_resp_secs = 10                       # max response period in secs

# Staircase parameters
start_secs = .25                       # starting duration in secs for temporal staircase
max_secs = 1
max_secs_sd = .2
min_secs = 2 * 1/85                  # Require two frames to generate motion

staircase_style = 'QUEST'               # 'simple' or 'QUEST'
staircase_ntrials = 30

conditions_QUEST = [
    {'label':'hi_contr', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.98, 'minVal':min_secs, 'maxVal':max_secs, 
    'grating_deg': grating_deg, 'spf':spf, 'tf':tf, 'mask_type': mask_type, 'gaussian_sd': gaussian_sd}
]
#conditions_QUEST = [
#    {'label':'lo_contr_big_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.03, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':10 , 'spf':spf, 'tf':tf, 'mask_type': mask_type},
#    {'label':'hi_contr_big_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.98, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':10 , 'spf':spf, 'tf':tf, 'mask_type': mask_type},
#    {'label':'lo_contr_sma_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.03, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':1.7, 'spf':spf, 'tf':tf, 'mask_type': mask_type},
#    {'label':'hi_contr_sma_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.98, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':1.7, 'spf':spf, 'tf':tf, 'mask_type': mask_type}
#    ]
conditions_simple = [
    {'label':'hi_contr', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.98,'grating_deg':grating_deg, 'stepSizes':[4,2,2,1],
    'spf':spf, 'tf':tf, 'mask_type':mask_type},
    ]

# Donut/response frame
show_response_frame = True              # Square 'response' frame flag
donut_outer_rad = 12                    # Outer radius in deg
donut_inner_rad = 11                   # Inner radius in deg
donut_color = [0, .75, 0]                  # Color 

# Interstimulus and intertrial timing
iti = 3.0                               # Fixed ITI in secs
isi_min = .20                          # Fixation/grating ISI min val
isi_max = .50                          # Fixation/grating ISI max val
iti_min = 1.0                           # ITI min val
iti_max = 2.5                           # ITI max val

# win.close()