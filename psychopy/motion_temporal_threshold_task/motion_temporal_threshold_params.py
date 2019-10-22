# Murray et al. parameters

"""
This code is an attempt to replicate the Murray et al. 2018 study on sex differences in temporal motion detection thresholds.

Murray, S. O., Schallmo, M.-P., Kolodny, T., Millin, R., Kale, A., Thomas, P., Rammsayer, T. H., et al. (2018). 
Sex Differences in Visual Motion Processing. Current biology: CB. 
Retrieved from http://dx.doi.org/10.1016/j.cub.2018.06.014
"""

# fimi_grayscale
#monitor_name = 'fimi_grayscale'
#window_pix_h = 1280
#window_pix_v = 1024
#frameDur = 1/85

# testMonitor
monitor_name = 'testMonitor'
window_pix_h = 800
window_pix_v = 600
frame_rate_hz = 60
frameDur = 1/frame_rate_hz

# Data file parameters
task_name = "temp_thresh"               # Murray et al. temporal threshold

# Fixation
fixation_secs = .850                    # Fixation duration
fixation_grating_isi = .15              # Fixation/grating ISI

#--- Grating
#contrast_mod_type = 'fixed_trapezoidal' # Ramp up, constant, ramp down, e.g., Abramov et al. 2012
stim_dur_secs = 2                       # Total grating duration
ramp_up_secs = .5                       # Ramp up duration
full_scale_secs = 1                     # Full-scale (constant contrast) duration
ramp_dn_secs = ramp_up_secs             # Ramp down duration

contrast_mod_type = 'variable_triangular'  # 'variable_triangular', 'fixed_trapezoidal'

#grating_deg = (1.7, 10)                 # 1.7 deg or 10 deg
grating_deg = 4

spf = 1
mask_type = 'gauss'                    # 'circle' or 'gauss'
gaussian_sd = 0.2

grating_ori = 0                         # grating orientation in deg, 0 is vertical, 90 is horizontal

tfreqs = [4]                            # Hz
tf = tfreqs[0]                          # Hz
cyc_secs = 1/tf                         # seconds for one full cycle

max_resp_secs = 10                       # max response period in secs

max_contr = .98                         # two conditions: 0.03 and 0.98

# Staircase parameters
start_secs = .333                       # starting duration in secs for temporal staircase
max_secs = .5
max_secs_sd = .2
min_secs = 2 * frameDur                 # Require two frames to generate motion

stair_case_style = 'quest'             # 'simple' or 'quest'

conditions_QUEST = [
    {'label':'hi_contr', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.95, 'minVal':min_secs, 'maxVal':max_secs, 
    'grating_deg': grating_deg, 'spf':1, 'tf':tf, 'mask_type': mask_type, 'gaussian_sd': gaussian_sd}
]
#conditions_QUEST = [
#    {'label':'lo_contr_big_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.03, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':10 , 'spf':spf, 'tf':tf, 'mask_type': mask_type},
#    {'label':'hi_contr_big_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.98, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':10 , 'spf':spf, 'tf':tf, 'mask_type': mask_type},
#    {'label':'lo_contr_sma_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.03, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':1.7, 'spf':spf, 'tf':tf, 'mask_type': mask_type},
#    {'label':'hi_contr_sma_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.98, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':1.7, 'spf':spf, 'tf':tf, 'mask_type': mask_type}
#    ]
conditions_simple = [
    {'label':'lo_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.03,'grating_deg':1.7, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'hi_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.98,'grating_deg':1.7, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'lo_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.03,'grating_deg':10, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'hi_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.98,'grating_deg':10, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type}
    ]

# Donut/response frame
show_response_frame = True              # Square 'response' frame flag
donut_outer_rad = 10                    # Outer radius in deg
donut_inner_rad = 9.7                   # Inner radius in deg
donut_color = .55                       # Color (.55 is a light gray)

# Interstimulus and intertrial timing
iti = 3.0                               # Fixed ITI in secs
isi_min = .250                          # Fixation/grating ISI min val
isi_max = .500                          # Fixation/grating ISI max val
iti_min = 1.0                           # ITI min val
iti_max = 2.5                           # ITI max val
