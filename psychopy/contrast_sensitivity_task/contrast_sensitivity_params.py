# Abramov et al. parameters

"""
This code is an attempt to replicate the Abramov et al. 2012 study on spatiotemporal contrast sensitivity thresholds.

Abramov, I., Gordon, J., Feldman, O., & Chavarga, A. (2012). Sex & vision I: Spatio-temporal resolution. Biology of Sex Differences, 3(1), 20. 
bsd.biomedcentral.com. Retrieved from http://dx.doi.org/10.1186/2042-6410-3-20
"""

# fimi_grayscale
#monitor_name = 'fimi_grayscale'
#window_pix_h = 1280
#window_pix_v = 1080
#frameDur = 1/85

# testMonitor
monitor_name = 'testMonitor'
window_pix_h = 800
window_pix_v = 600
frameDur = 1/60

# Grating
stim_dur_secs = 2
ramp_up_secs = .5
full_scale_secs = 1
ramp_dn_secs = ramp_up_secs

grating_deg = (3.2, 3.2)

max_contr = 0.5
start_contr = 0.25
min_contr = 0.005

spfreqs = [1, 20]
spf = spfreqs[0]
tfreqs = [1, 20]    # Hz
tf = tfreqs[0]      # Hz
cyc_secs = 1/tf     # seconds

# Donut/response frame
donut_outer_rad = 3.5
donut_inner_rad = 3.2
donut_color = .6

# Interstimulus and intertrial timing
iti = 3.0           # seconds
isi_min = .250      # seconds
isi_max = .500      # seconds
iti_min = 1.0       # seconds
iti_max = 2.5       # seconds

stair_case_style = 'simple'             # 'simple' or 'quest'

conditions_QUEST = [
    {'label':'lo_contr_big_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.03, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':10 , 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'hi_contr_big_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.98, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':10 , 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'lo_contr_sma_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.03, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':1.7, 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'hi_contr_sma_disp', 'startVal':start_secs, 'startValSd':max_secs_sd, 'pThreshold':.82, 'max_contr':.98, 'minVal':min_secs, 'maxVal':max_secs, 'grating_deg':1.7, 'spf':spf, 'tf':tf, 'mask_type': mask_type}
    ]
conditions_simple = [
    {'label':'lo_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.03,'grating_deg':1.7, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'hi_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.98,'grating_deg':1.7, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'lo_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.03,'grating_deg':10, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type},
    {'label':'hi_contr_big_disp', 'startVal':start_secs, 'minVal': min_secs, 'maxVal': max_secs, 'max_contr':.98,'grating_deg':10, 'stepSizes':[8,4,4,2,2,1], 'spf':spf, 'tf':tf, 'mask_type': mask_type}
    ]
