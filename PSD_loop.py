#PSD.py
from pylab import *
from rtlsdr import *
import numpy as np
import sys
from datetime import datetime

Status_Device = []
#Status of Device
name_Status_Device = datetime.now().strftime('Status_Device_%d-%m-%Y_%H:%M:%S.txt')
Status_Device_Time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
Status_Device.append(Status_Device_Time)
file_out_Status = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Status_Device/"+name_Status_Device,"w")
for element in Status_Device:
    file_out_Status.write(element+"\n")
file_out_Status.close()

Power_L1 = []
Power_L5 = []

Power_L1_NoJam = []
Power_L5_NoJam = []

Status_of_Jamming_L1 = 0
Status_of_Jamming_L5 = 0

name_Text1  = datetime.now().strftime('Power_L1_%d-%m-%Y_%H:%M:%S.txt')
name_Text5  = datetime.now().strftime('Power_L5_%d-%m-%Y_%H:%M:%S.txt')
name_Text1_NoJam  = datetime.now().strftime('Power_L1_%d-%m-%Y_%H:%M:%S.txt')
name_Text5_NoJam  = datetime.now().strftime('Power_L5_%d-%m-%Y_%H:%M:%S.txt')

sdr = RtlSdr()

Time_to_receive = range(50) #เวลาในการบันทึก range(50) จะประมาณ 2 นาทีกว่า

for i in Time_to_receive:
    
    
    sdr.sample_rate = 2.4e6
    #Sweep Frequency L1 L5
    #L1
    if (i%2) ==0:
        sdr.center_freq = 1575.42e6 #L1
        name_graph = datetime.now().strftime('Spectrum_L1_%d-%m-%Y_%H:%M:%S.png')
        Time_L1 = datetime.now().strftime('%Y-%m-%d, %H:%M:%S, ')
    #L5
    elif (i%2) ==1:
        sdr.center_freq = 1176.45e6 #L5
        name_graph = datetime.now().strftime('Spectrum_L5_%d-%m-%Y_%H:%M:%S.png')
        Time_L5 = datetime.now().strftime('%Y-%m-%d, %H:%M:%S, ')
    #Set Gain
    sdr.gain = 50
    samples1 = sdr.read_samples(256*1024)
    
    power = psd(samples1, NFFT=512, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    xlabel('Frequency (MHz)')
    ylabel('Relative power (dB)')
    
    #Convert Watt to dB
    power_db = 10*np.log10(power)
    row_median = np.median(power_db,axis = 1)
    row1_median = row_median[0]
    format_float = "{:.2f}".format(row1_median)
    row_mean = np.mean(power_db,axis = 1)
    row1_mean = row_mean[0]
    format_float_mean = "{:.2f}".format(row1_mean)
    
    #Save Spectrum and Power(dB) L1 L5 
    #L1
    if (i%2) ==0:
        #if Power(dB) > Threshold(-46) ==> Jamming 
        if float(format_float) >= -44: #Threshold is -46
            #if Median of Power(dB) - Threshold > 1 => Sure Jamming
            if abs(row1_median - (-44)) >= 1:
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1/'+name_graph)
                
                if Status_of_Jamming_L1 == 2:
                    #Save Power(dB) Last time NoJam
                    print('NoJaming L1 last')
                    Power_L1_NoJam.append(Time_L1+'1575.42e6, Last time before jamming -2 sec')
                
                print('Jaming L1')
                #Save Power(dB) L1 to Text file
                Power_L1.append(Time_L1+'1575.42e6, '+str(format_float))
                Status_of_Jamming_L1 = 1 #เปลี่ยนสถานะว่าเกิดการ แจม
        
        #if Power(dB) < Threshold(-46) ==> NoJamming
        else:
            #Save Power(dB) L1 to Text file
            Power_L1_NoJam.append(Time_L1+'1575.42e6, '+str(format_float)) ###########
            if Status_of_Jamming_L1 == 0: #เช็คสถานะเมื่อไม่มีการแจมจะบันทึกข้อมูลครั้งแรก
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L1/'+name_graph)
                print('NoJamming L1 first')
                Status_of_Jamming_L1 = 2 #เปลี่ยนสถานะเป็น 2 เพื่อรอตรวจสอบว่าตอนที่ไม่มีการแจมครั้งแรกถึงครั้งสุดท้าย
            elif Status_of_Jamming_L1 == 1: #เมื่อมีสถานะจากการแจมครั้งล่าสุด และครั้งนี้ไม่มีการแจม จะเปลี่ยนสถานะเป็น 0 เพื่อเริ่มนับสถานะไม่มีการแจมใหม่
                print('NoJaming L1 ')
                Status_of_Jamming_L1 = 0 #เปลี่ยนสถานะเป็น 0 เพื่อรอบันทึกถึงครั้งที่ัไม่มีการแจมใหม่ ถึงครั้งสุดท้าย
            elif i == max(Time_to_receive)-1 and Status_of_Jamming_L1 == 2: #ถ้าโปรแกรมทำงานถึงรอบสุดท้าย และสถานะการแจมเป็น 2 จะบันทึกข้อมูลครั้งสุดท้าย
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L1/'+name_graph)
    #L5
    elif (i%2) ==1:
        #if Power(dB) > Threshold(-44) => Jamming
        if float(format_float) >= -42: #Threshold is -44
            #if Median of Power(dB) - Threshold > 1 => Sure Jamming
            if abs(row1_median - (-42)) >= 1:
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L5/'+name_graph)
                
                if Status_of_Jamming_L5 == 2:
                    #Save Power(dB) Last time NoJam
                    print('NoJaming L5 last')
                    Power_L5_NoJam.append(Time_L5+'1575.42e6, Last time before jamming -2 sec')
                
                print('Jaming L5')
                #Save Power(dB) L1 to Text file
                Power_L5.append(Time_L5+'1176.45e6, '+str(format_float))
                Status_of_Jamming_L5 = 1
        else:
            #Save Power(dB) L5 to Text file
            Power_L5_NoJam.append(Time_L5+'1176.45e6, '+str(format_float)) ###########
            if Status_of_Jamming_L5 == 0:
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L5/'+name_graph)
                Status_of_Jamming_L5 = 2
            elif Status_of_Jamming_L5 == 1:
                print('NoJaming L5')
                Status_of_Jamming_L5 = 0
            elif i == max(Time_to_receive) and Status_of_Jamming_L5 == 2:
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L5/'+name_graph)
    cla()
    time.sleep(1)
sdr.close()

if not Power_L1:
    print("L1 : List is empty")
else:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Jam/Power_L1/"+name_Text1,"w")
    for element in Power_L1:
        file_out.write(element+"\n")
    file_out.close()

if not Power_L1_NoJam:
    print("L1_NoJam : List is empty")
else:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/Power_L1/"+name_Text1_NoJam,"w")
    for element in Power_L1_NoJam:
        file_out.write(element+"\n")
    file_out.close()

if not Power_L5:
    print("L5 : List is empty")
else:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Jam/Power_L5/"+name_Text5,"w")
    for element in Power_L5:
        file_out.write(element+"\n")
    file_out.close()

if not Power_L5_NoJam:
    print("L5_NoJam : List is empty")
else:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/Power_L5/"+name_Text5_NoJam,"w")
    for element in Power_L5_NoJam:
        file_out.write(element+"\n")
    file_out.close()

