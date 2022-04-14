# hp620_webuicontrol_aging
Please execute 'testLaunher.py' using python command like below:
> python .\testLauncher.py

Before running 'testLauncher.py', please make a factory default setting through WEB UI or other ways.
And then check available serial port information and log in to the serial port using id/pw.
These python codes are working based on a 'COM7' serial port.
So if your environment is not using COM7, please change the serial port which your environment is available in the codes.
If you don't have information about the id/pw, please contact to any members who may know it.
Also please log in to WEB UI and then change a default log in password to '000000'

# Project : HP620 WEB UI Control Aging
## Purpose
A bug related to memory leakage of a home gateway (DUT) had been found and the new SW that fixed the bug has released. 
To check the bug fixed or not, some repetitive changes of the home gateway's configuration control WEB page (WEB UI) should be executed.
But this kind of testing is a type of boring and repetitive task for human so some python scripts with some packages: selenium, pytest, serial and multiprocessing has made to check both memory leakage and WEB UI control. 

## Used major technique
- Python 3
- pytest
- serial
- multiprocessing
- selenium

## Simple Diagram and How to use
- Diagram

<p align="center">
    <img src='./images/WEB_UI_Control Aging_to_check_Memory_Leak.png'>
    <br>
    
</p>

- How to use
  - Please execute 'testLaunher.py' using python command like below:
    - python .\testLauncher.py
    - Before running 'testLauncher.py', please make a factory default setting through WEB UI or other ways.
    And then check available serial port information and log in to the serial port using id/pw.
    These python codes are working based on a 'COM7' serial port.
    So if your environment is not using COM7, please change the serial port which your environment is available in the codes.
    If you don't have information about the id/pw, please contact to any members who may know it.
    Also please log in to WEB UI and then change a default log in password to '000000'
