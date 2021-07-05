import os
import time
import datetime

doy = datetime.datetime.utcnow().strftime('%j')
year = datetime.datetime.utcnow().strftime('%Y')
#upload status of device to server
U='pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Status_Device/* jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L1/'+year+'/'+doy+'/Status/'
I='pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Status_Device/* jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L5/'+year+'/'+doy+'/Status/'

time.sleep(10)

os.system(U)
os.system(I)

os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Status_Device/*')
