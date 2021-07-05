#PSD.py
from pylab import *
from rtlsdr import *
import numpy as np
import sys
from datetime import datetime

Power_L1 = []
Power_L5 = []

Power_L1_NoJam = []
Power_L5_NoJam = []

Status_of_Jamming_L1 = 0
Status_of_Jamming_L5 = 0

name_Text1  = datetime.now().strftime('TELECOM_Jam_L1_%d-%m-%Y_%H:%M:%S.csv')
name_Text5  = datetime.now().strftime('TELECOM_Jam_L5_%d-%m-%Y_%H:%M:%S.csv')

name_Text1_NoJam  = datetime.now().strftime('TELECOM_NoJam_L1_%d-%m-%Y_%H:%M:%S.csv')
name_Text5_NoJam  = datetime.now().strftime('TELECOM_NoJam_L5_%d-%m-%Y_%H:%M:%S.csv')

sdr = RtlSdr()

Time_to_receive = range(120) #time about 5 min

for i in Time_to_receive:
    
    
    sdr.sample_rate = 2.4e6
    #Sweep Frequency L1 L5
    #L1
    if (i%2) ==0 and i!=0:
        sdr.center_freq = 1575.42e6 #L1 1575.42
        name_graph = datetime.now().strftime('_TELECOM_L1_%d-%m-%Y_%H:%M:%S.png')
        Time_L1 = datetime.now().strftime('%Y-%m-%d, %H:%M:%S, ')
    #L5
    elif (i%2) ==1 and i!=1:
        sdr.center_freq = 1176.45e6 #L5 1176.45
        name_graph = datetime.now().strftime('_TELECOM_L5_%d-%m-%Y_%H:%M:%S.png')
        Time_L5 = datetime.now().strftime('%Y-%m-%d, %H:%M:%S, ')
    #Set Gain
    sdr.gain = 50
    samples1 = sdr.read_samples(256*1024)
    if (i%2) ==0:
        power = psd(samples1, NFFT=512, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
        axhline(y=-46,color='green',linestyle='--')
        xlabel('Frequency (MHz)')
        ylabel('Relative power (dB)')
    elif (i%2) ==1:
        power = psd(samples1, NFFT=512, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
        axhline(y=-44,color='green',linestyle='--')
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
    if (i%2) ==0 and i!=0: #skip 1st count
        #if Power(dB) > Threshold(-46) ==> Jamming 
        if float(format_float) >= -46: #Threshold is -46
            #if Median of Power(dB) - Threshold > 1 => Sure Jamming
            if abs(row1_median - (-46)) >= 1:
                if i == 2: #Error from DC
                    savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1_Error/'+name_graph)
                elif i != 2: #
                    savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1/Jam'+name_graph)

                #Save Power(dB) L1 to Text file
                if i == 2: #Error from DC
                    print("Not Save")
                elif i != 2: #
                    Power_L1.append(Time_L1+'1575.42e6, '+str(format_float)+', Jamming')
                    Status_of_Jamming_L1 = 1 #Change Status Jam

        #if Power(dB) < Threshold(-40) ==> NoJamming
        else:
            #Save Power(dB) L1 to Text file
            if Status_of_Jamming_L1 == 0: #if Status NoJam will Save first Spectrum
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L1/NoJam'+name_graph)
                Power_L1_NoJam.append(Time_L1+'1575.42e6, '+str(format_float)+', Non-Jamming')
                Status_of_Jamming_L1 = 2 #change status to 2 for check status first NoJam to last NoJam
            elif Status_of_Jamming_L1 == 1: #if status Jam last time and now is NoJam will change status to 0 to for start counting the Nojam status.
                Status_of_Jamming_L1 = 0 #change status to 0 for start counting the first NoJam to last Nojam

    #L5 
    elif (i%2) ==1 and i!=1: #skip 1st count
        #if Power(dB) > Threshold(-44) => Jamming
        if float(format_float) >= -44: #Threshold is -44
            #if Median of Power(dB) - Threshold > 1 => Sure Jamming
            if abs(row1_median - (-44)) >= 1: 
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L5/Jam'+name_graph)

                #Save Power(dB) L1 to Text file
                Power_L5.append(Time_L5+'1176.45e6, '+str(format_float)+', Jamming')
                Status_of_Jamming_L5 = 1
        else:
            #Save Power(dB) L5 to Text file
            if Status_of_Jamming_L5 == 0: #if Status NoJam will Save first Spectrum
                savefig('/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L5/NoJam'+name_graph)
                Power_L5_NoJam.append(Time_L5+'1176.45e6, '+str(format_float)+', Non-Jamming')
                Status_of_Jamming_L5 = 2 #change status to 2 for check status first NoJam to last NoJam
            elif Status_of_Jamming_L5 == 1: #if status Jam last time and now is NoJam will change status to 0 to for start counting the Nojam status.
                Status_of_Jamming_L5 = 0 #change status to 0 for start counting the first NoJam to last Nojam
    cla()
    time.sleep(1)
sdr.close()

if not Power_L1:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Power_L1/NoJam/"+name_Text1_NoJam,"w")
    for element in Power_L1_NoJam:
        file_out.write(element+"\n")
    file_out.close()
else:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Power_L1/Jam/"+name_Text1,"w")
    for element in Power_L1:
        file_out.write(element+"\n")
    file_out.close()

if not Power_L5:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Power_L5/NoJam/"+name_Text5_NoJam,"w")
    for element in Power_L5_NoJam:
        file_out.write(element+"\n")
    file_out.close()
else:
    file_out = open("/home/pi/Desktop/Lab_jamming/Output/PSD/Power_L5/Jam/"+name_Text5,"w")
    for element in Power_L5:
        file_out.write(element+"\n")
    file_out.close()
