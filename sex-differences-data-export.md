# Gilmore Lab #

## High Density (HD) NetStation -> PowerDiva Data Export

### Close All Programs used for a Data Collection session

- Reminder: If you have not done so, save and close **NetStation session** by pressing the **Close Session** button in the upper right hand corner of the NetStation window.

- If you have not already done so, **quit** the **PowerDiva Video** application on the PDVideo computer.

### On the Net Station Computer

- From NetStation startup screen, go to File > Open to access archived sessions. Session files are usually located in: /Users/GilmoreLab/Documents/NetStation User Data/Sessions

![Net Station Open Archived Files](imgs/NS_Open_Archived_Files.jpg)

- To find the most recent session, click on the **Date** field in the Finder window. The small arrow should face downward to sort files in reverse date order.

![Net Station Arrow faces down](imgs/DateModifiedArrowDown.jpg)


- Go to **Tools > Waveform Tools** 
 
![Net Station Open Waveform Tools](imgs/NS_Open_Waveform_Tools.jpg)

  - Run the Concatenate tool:
    - Press the **Add** button, and add the .raw session file you wish to process  
    
![Net Station Add Inputs](imgs/NS_Concatenate_Tool.jpg)  

   - Select the **Concatenate Epochs for PowerDiva** tool from the lower window  
   - Click on **Jobs/Results** button to monitor progress  
   - To run the tool, press the **Run** button  
      
  - Run the Export for Power Diva tool  
    
![Net Station Export to Power Diva](imgs/NS_Export_PowerDiva.jpg)

   - Add the .cat file you just created to the upper window by pressing the **Add** button  
   - Select the Export for PowerDiva tool from the lower window  
   - Press the **Run** button to run the tool. This can take 3-8 minutes.  

- Quit NetStation.

- Transfer exported files to the PowerDiva Video machine for analysis. 
  - On the NetStation computer desktop, double-click the **NetStation_Sessions@PDVideo** alias (highlighted in green). This opens a connection via Ethernet to the PowerDiva Video computer.
  
![Net Station @ PD Video](imgs/NS_@PDVideo.jpg)

  - Create a new folder with ParticipantID code and project name within the NetStation_Sessions folder.
  - Double-click on **Sessions@Local** alias (highlighted in red). This opens a separate window to the local NetStation Sessions folder.
  
![Sessions @ Local](imgs/NS_Sessions_Local.jpg)

  - Select the files for copy to the PowerDiva Video machine. (Via the green folder)
    - Copy the raw data file (.raw), and the gains (.gains) and zeroes (.zeros) files and impedances (.imp)
      - Shift or command click on these files and drag them to the green Net Station folder. The process takes about five to ten minutes.

- Once copied you may shut down the Net Station computer.

### On the PD Video Computer

- Make a copy (file → duplicate) of the stimulus set (found in stimulus set folder on the desktop) and put this in the participant’s folder within the net station’s session folder.

- Open the Power Diva host 3.4 application by double clicking the icon on the desktop
  - Ignore error messages and choose to work offline

#### Import Data

- From the file menu of Power Diva host select import NS session.

- Session window: enter operator information and participant information
  - participant first name: keep blank 
  - participant last name: enter the participant ID code. 
  - Select the Net Station session files by clicking on the **choose** button to the right of the raw EEG’s field. 
    - Navigate to the Net Station Sessions folder you just copied the files to. 
    - Select the .raw file for the session.
  - Enter the zeroes and gains by clicking on **choose** 
    - Shift click on both .zeros and .gains files for this session. 
  - Select the stimulus set for this session: click on the **Choose** button 
    - Navigate to the duplicate file within the subject’s session folder. 
  - If loaded correctly you should see valid data appear in the video system, display type, and video mode fields. 
  - Hit **OK** to import the data into Power Diva host. Power Diva will check for artifacts

#### Check for Artifacts

- Set the **Channel Substitution** screen
  - Set "Raw Thresh Detector" to 50 μV (adults), 60 μV (children).
    - Any sample > threshold is marked as bad epoch/sample.
    - Leave "Fast Filter Detector" at defaults (and unchecked): "Threshold" = 30 μV, "Fast Filter Cutoff" = 40 Hz
    - Leave "Slope Detector" at defaults (and unchecked): "Threshold" = 30 μV, "Slow Filter Cutoff" = 4 Hz 
    - Leave "Substitute Channels with more than ____" % bad channels at default values: We use 15% as default.
    - Substitutes entire epoch (all samples) from bad channels with weighted average of 6 neighboring channels.

  - Press the **Repeat Detection** button
  - Press **OK** to continue

????- Referencing
	- Net Station uses fixed Cz (vertex) referencing. Channel is called VREF.
	- PowerDiva calls this "user defined montage."
	- We average referencing for channels.????

- Set **Analysis Parameters** screen
  - Set Processing Task (Harmonics of Interest) 
    - Ensure all multiples of F1 (1F1, 2F1, 3F1 , 4F1, 5F1, 6F1, 7F1, 8F1, 9F1) are selected 
    - Select also 1F2, 1F1 + 1F2, and 1F1 – 1F2
    - Set for all conditions by selecting **Set To All** button at the top.
  - Set Epoch Rejection Parameters
    - Set "Raw Thresh Detector" to 50 μV (adults), 60 μV (children).
    - Set for all conditions by selecting **Set To All** button.
  - Click **Continue** to view the imported PD session.

- Within the session export MATLAB data.
  - Go to **File > Export**
  - Set **Export** screen
    - Export as: MATLAB files
    - Under Matlab Options
      - Check box for **axx filter**
      - Change P-thresh to 0.05
    - Under **Data Types**
      - Check “axx”.
    - Press **Export**
    - After export complete, Press **Done**
	- Then close the session.

- Export text file data for analysis in Excel
	- In the R&D menu select Batch Export ODBC.
	- A window will pop up concerning bins. For all experiments except for sweeps select No Bins, for sweeps select export bins.
	- A window pops up called Choose Source Folder. Within this window navigate to the desktop and double click on the Power Diva alias folder. Highlight the session of choice and press ‘choose’ 
	- A window pops up called Choose Export Folder. Navigate to the desktop and select an external storage device (such as a USB). Double click on this device, then press the ‘New Folder’ button. Name this folder according to subject ID, project name, and current date (e.g. 810529jefe_mofo_pattern_110901). Then highlight this folder and press the ‘Choose’ button. 
	- Remove storage device and load onto computer with MATLAB and/or Excel for analysis (see separate protocol) 
	
## PowerDiva Session Folder Contents ##

A full folder for a PowerDiva session should contain a series of files. The folder should have the SESSIONNAME as the first part of the name. SESSIONNAMES may be in the YYYYMMDDD_HHMM (test date and time) format or for old files in a YYMMDDabcd_YYYYMMDD_HHMM (Ss birthdate and first two initials of first and last names plus testing date and time)format or something similar. We will standardize soon.

- **SESSIONNAME_main.pdh** file
	- PowerDiva Host session file.
	- Must be archived with StuffIt (creating *.sit file) before being moved from Mac OS 9 machine
	- *.sit archive must be UnStuffed before launching PowerDiva Host program
- **Data_mtg0** folder
	- Contains a series of files by condition number (1..n)
		- SESSIONNAME_c00n.axx
		- SESSIONNAME_c00n.qa
		- SESSIONNAME_c00n.raw
			- This *.raw format is not identical to EGI's NetStation
		- SESSIONNAME_c00n.rls
	- Must be archived with StuffIt (creating a *.sit archive) before being moved from Mac OS 9 machine
	- *.sit archive must be UnStuffed before launching PowerDiva Host program
	
- **Data** folder
	- Empty

- **Exp_MATL_HCN_128_Avg** folder for conditions 1..n

	- Axx_c00n.mat

	- Montage_ssn.mat
	
	- See [power-diva-export-metadata.md](power-diva-export-metadata.md) for more information about the format of these files.


- RLS export data (ODBC export)

	- See [power-diva-export-metadata.md](power-diva-export-metadata.md) for more information about the format of these files.

	- **QETXT.INI**

	- **RLS.txt**
	
		- Combine this file with RLS.txt files from other participants in a separate step.

	- **SCHEMA.INI**

	- **SsnHeader.txt**
	
- NetStation Files

	- **SESSIONNAME.GAIN**
	
		- Gains

	- **SESSIONNAME.ZERO**	
	
		- Zeros

	- **SESSIONNAME.IMP**

		- Impedances

	- **SESSIONNAME.raw**
	
		- Raw data
	
- StuffIt-compressed version of **Stimulus Set**.

## Protocol for Importing & Analyzing Data on Excel

Export the Data: In Power Diva Host, go to the RVSB menu and select ‘Batch Export ODBC’. When the prompt window pops up, select to “Export No Bins” option. Choose your source folder (the power diva session file, found in the Power Diva Alias folder on the Desktop), and then your exporting folder (a USB drive). The data will then be exported to the USB drive in text file format. Create a folder in the USB drive with the participant’s ID and the stimulus type as the folder title, then place the text files in this folder.

1. Import data to one of the lab computers. Open Excel and start up a new spreadsheet. 

2. From Excel, choose the Open command, and open the RLS.txt file of the session you wish to import. Select the data in this file; copy it and paste it into your spreadsheet. 

3. Before you import another session’s data, create a column in your spreadsheet and title it Participant. 

4. Write the participants ID on the first block in the Participant column. To copy the ID to the rest of the column: click on that same block one more time, place your cursor to the lower right corner of the box, and drag your cursor down the column until all rows with data have the participant’s ID. 

5. For each participant’s session data, repeat steps 2 & 4.

6. Once all session data is in the spreadsheet, highlight all of the data, then go to the Data menu and select the Pivot Table Report option.

7. A prompt window will appear asking about the source of the data. Hit ‘Excel database’. The next prompt will ask where your data is; your data should already be selected if you highlighted it previously, so just hit OK. 

8. Next, choose the Layout option to set up your Pivot Table Chart. The structure of your chart will be based on where (e.g. Column, Row, Page) you drag the item categories in this section. Drag the Participant, iCh (channel), and Harm (harmonic) items to the Page section. Drag the iCond (condition) into the Column section. In the Data space, drag and drop the Sr (signal real) and Si (signal imaginary) items, double click each one, and select Average for both. Do this again and select Variance for both. Finally, drag one more Sr into the Data section, and select Count (These will be needed to compute the t2 circ analysis of the signal). Hit OK.

9. NOTE: You may want to go to Options and uncheck the Grand Totals options, as these can crowd your table.

10. Hit Finish

11. For the t2 circ computation: 
In the leftmost box just below your table, type in ‘Mean’. This will be for a row of vector-averaged means of SSVEP signal, ordered by condition. 
Below that, type ‘S.E.M.’ for the standard error of the mean (a measure of variance) for each condition. 
Below that, type ‘t2circ’ for the significance test (similar to a t-test, but this factors in the phase of the signal, relative to the stimulus) of activity for each condition.
Below that, type ‘p-value’, which will show the statistical confidence of the t2circ value (p-values under .05 have a confidence of 95% or more).

12. Formulas: Double click on the box just right of each of the above title boxes, and enter the following formulas, remembering that the Pivot Table item categories (like ‘Average of Sr’) for each condition should be entered according to their spreadsheet coordinates (like E19). For this first time, choose the coordinates of the first condition.
	Mean:  =SQRT(SUMSQ(Average of Sr:Average of Si))
	S.E.M.: =SQRT(AVERAGE(Variance of Sr:Variance of Si)/(Count of Sr-1))
	T2circ: =SUMSQ(Average of Sr:Average of Si)/2/AVERAGE(Var of Sr:Var of Si)
	p-value: =FDIST(Count of Sr*t2circ,2,2*Count of Sr-2)
Click on the box next to Mean, then drag the cursor across the row (like the Copy method in Step 4.) to copy the formula into each condition column. Do this for S.E.M., t2circ, and p-value rows as well.

13. You can make a chart of the data by selecting what you’d like to chart, then going to the Insert menu and selecting Chart. Pick your chart preferences and parameters, then click OK.

