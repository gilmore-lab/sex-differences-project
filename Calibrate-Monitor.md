# Calibrate Monitor
## EEG
### Prepare Computers
- In 120H Switch on power of large surge protector on bottom left shelf.

- Switch on power of smaller, thin surge protector on second shelf (ignore lights; always on).

- Turn on **PD Video**, **NetStation** and **Link 15** computers, and both monitors.

  - If either monitor screen is unresponsive, you may need to toggle to the correct computer via the gray KVM switches on the top left (PD Video / Link 15) and right (NetStation  / PD Host) shelf.

- Turn on external timebase, behind the monitors (switch is back, right side).

- Remove the plug from the external timebase outlet labeled **OUT**. (Clock Out stays in).  - What is this for calibration
 
    ![Rear of External Timebase](imgs/rear-of-ext-timebase.pictClipping.jpg)

- Make sure that white round switch on top of the left KVM switch is set to B.

    ![White Switch on top of Black KVM Switch](imgs/Serial_Switch_B.jpg)

- On PD Video computer, open Power Diva Video 3.4 software. (icon label says alias)

    ![Power Diva Video icon](imgs/power-diva-video-icon.pictClipping.jpg)
 
- In Power Diva Video, go to Configuration > Video Manager. In **Mode** window, make sure the calibrated video setting is selected: 

	- 800 x 600, 72 Hz, 8 bit

 
     ![Power Diva Video Manager](imgs/2015-04-28-calibration.jpg)  

- Choose **Cancel**

### Prepare Photometer

- Take the photometer out of the box. 
- Set it up by plugging in the power and the light meter.
- Turn on the photometer
- Ensure the following settings: 
- Zero the photometer by placing the cap on the light meter and pressing the 'zero' button


### Start Calibrating Luminance

- Click **Calibrate Lum**  

    ![Luminance Calibration](imgs/LuminanceCalibration2.jpg)


- Enter the Monitor Screen Width in centimeters
- Select **Start**  
    ![Luminance Calibration - Enter Value](imgs/LuminanceCalibration_EnterValue2.jpg)

## MRI

Projector calibration should be run every time the projector screen, lightbulb or projector PC are changed.

### Prepare scan room

All mirrors and the projector screen have marks on the floor indicating their proper position.
- Move the projector screen into the scanner room doorway
- Move the mirror behind the scanner next to the mirror in the corner of the room so that the image will reflect back to the projector screen
- Adjust the angle of the mirror until the entire image is visible on the projector screen.
- Exit the room.
- Turn off all lights in the scanner room.

### Prepare Photometer

- Take the photometer out of the box. 
- Set it up by plugging in the power and the light meter.
- Turn on the photometer
- Ensure the following settings:
- Zero the photometer by placing the cap on the light meter and pressing the 'zero' button


### Run Matlab Script

- At a minimum a black (0,0,0) and white (255,255,255) image must be displayed on the projector screen 
- The script to do this is located on Github: https://github.com/gilmore-lab/photometer_proj
 
### Measure Luminance

- Measure the value of each image on the projector screen with the light meter.

### Log values

- Log the values in the file Box Sync/gilmore-lab/protocols-procedures/projector-calibration.xls
