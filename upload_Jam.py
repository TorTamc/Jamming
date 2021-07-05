import os
import datetime

doy = datetime.datetime.utcnow().strftime('%j')
year = datetime.datetime.utcnow().strftime('%Y')
#upload data jamming to server
A='pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1/* jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L1/'+year+'/'+doy+'/Spectrum/'
B='pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L5/* jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L5/'+year+'/'+doy+'/Spectrum/'

os.system(A)
os.system(B)

os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1/*')
os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L5/*')
