#from test_lANSettingChange4 import *
#from testSerialUsingWith import * 
from os import system
from subprocess import call
from multiprocessing import Process, freeze_support

import testSerialUsingWith 
import test_lANSettingChange

#system("python .\\testSerialUsingWith.py")
#system("python .\\test_lANSettingChange4.py")
#call(["python",".\\testSerialUsingWith.py"])
#call(["python",".\\test_lANSettingChange4.py"])

#'''
if __name__ == '__main__':
    freeze_support()
    process1 = Process(target=call, args=(["python",".\\testSerialUsingWith.py"], ))
    process2 = Process(target=call, args=(["python",".\\test_lANSettingChange.py"],))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
#'''


