import os
import datetime

doy = datetime.datetime.utcnow().strftime('%j')
year = datetime.datetime.utcnow().strftime('%Y')

os.system("pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1/* jamming@161.246.18.204:/home/jamming/NAS/E12/Jam/L1/Spectrum/$year/$doy/")
os.system("pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L5/* jamming@161.246.18.204:/home/jamming/NAS/E12/Jam/L5/Spectrum/$year/$doy/")
os.system("pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/Power_L1/* jamming@161.246.18.204:/home/jamming/NAS/E12/Jam/L1/Textfile/$year/$doy/")
os.system("pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/Power_L5/* jamming@161.246.18.204:/home/jamming/NAS/E12/Jam/L5/Textfile/$year/$doy/")
os.system("pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Status_Device/* jamming@161.246.18.204:/home/jamming/NAS/E12/Status/")

os.system("rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1/*")
os.system("rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L5/*")
os.system("rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/Power_L1/*")
os.system("rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/Power_L5/*")
os.system("rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Status_Device/*")