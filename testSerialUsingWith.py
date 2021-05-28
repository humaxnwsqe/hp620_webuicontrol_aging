import serial
from serial import SerialException
import time
import datetime
import io
import threading
import keyboard
from multiprocessing import Process, freeze_support
import sys
import logging

delayTime = 600 # Unit per measurement is second.
stop = False # Flag for stopping loop
filename = 'log_meminfo.txt' # A log file to save command 'meminfo' printed. 
val_baudrate = 115200 # One of option for serial connection
val_port = 'COM7' # One of option for serial connection
val_timeout = 1 # One of option for serial connection
cur_datetime = "" #Current date and time"

#logging.basicConfig(level=logging.DEBUG) # To print log in case of debugging.


def onkeypress(event):
    global stop
    #global delayTime
    waitingTime = 60
    if event.name == 'esc':
        #print("Key 'q' has pressed!")
        print("You pressed the 'esc' Key. Saving command meminfo printed will be stopped in %d seconds." %waitingTime)
        stop = True


if __name__ == '__main__':
    freeze_support()

    # ---------> hook event handler
    keyboard.on_press(onkeypress)
    # --------->

    with serial.Serial() as ser:
        
        ser.baudrate = val_baudrate
        ser.port = val_port
        ser.timeout = val_timeout
        

        try:
            ser.open()
            #if ser.is_open == True:
            #tmp_portnum = ser.portstr
            print("##############################################")
            print("#### Serial port %s is opened!"%ser.portstr)
            print("##############################################")
        except SerialException:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Wrong serial port was selected. Please check an available serial port agian.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # For checking connected serial port number!
        #print(ser.portstr)     
        

        while ser.readable():

            #cur_datetime = datetime.datetime.today().strftime("%Y-%m-%d-%a-%H-%M-%S %Z")
            cur_datetime = datetime.datetime.today().strftime("%c")
            
            print("#####################################################################")
            print("###Saving command info printed will be started!")
            print("###If you want to stop saving this, please press'ESC' key.###")
            print("Time: %s"%cur_datetime)
            print("#####################################################################")

            ser.write(b'meminfo\r')
            res = ser.readline().decode()
            tmpstr = res.rstrip('\r\n')
            logging.debug("Command \'%s\' was typed."%tmpstr)
            #ser.flush()
            while ser.in_waiting > 0:
                res = ser.readline().decode()
                currenttime = datetime.datetime.now()

                with open(filename, 'a') as f:
                    f.write(currenttime.strftime('%Y-%m-%d %H:%M:%S\t\t') + str(res) + "\n")
                #datafile.write(str(res) + "\n")        
                #print(res)
            #ser.dtr = True
            

            print("\n--------------------")
            print("%d seconds waiting."%delayTime)
            print("--------------------")
            print("###If you want to stop saving command \'%s'\ info, please press'ESC' key.###"%tmpstr)
            time.sleep(delayTime)
            if stop:
                print("---The end of saving meminfo---")
                break

            
            
#datafile.close()
#def main():
#    print('testSerialUsingWith.py')


