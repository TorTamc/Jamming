import numpy as np
import sys
from datetime import datetime

Status_Device = []
#Status of Device
name_Status_Device = datetime.now().strftime('Status_TELECOM_%d-%m-%Y_%H:%M:%S.txt')
Status_Device_Time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
Status_Device.append(Status_Device_Time)
file_out_Status = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Status_Device/"+name_Status_Device,"w")
for element in Status_Device:
    file_out_Status.write(element+"\n")
file_out_Status.close()
