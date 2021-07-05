import os
import datetime
import time
import glob
import os.path

doy = datetime.datetime.utcnow().strftime('%j')
year = datetime.datetime.utcnow().strftime('%Y')

#upload data Text and Spectrum of non-jamming to server
try:
    folder_path = r'/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L1/'
    file_type = '*.png'
    files = glob.glob(folder_path + file_type)
    min_file = min(files, key=os.path.getctime)
    V='pscp -P 8030 -pw b8yps2e5 '+min_file+' jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L1/'+year+'/'+doy+'/Spectrum/'
    os.system(V)
except:
    pass

try:
    folder_path1 = r'/home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L5/'
    file_type1 = '*.png'
    files1 = glob.glob(folder_path1 + file_type1)
    min_file1 = min(files1, key=os.path.getctime)
    W='pscp -P 8030 -pw b8yps2e5 '+min_file1+' jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L5/'+year+'/'+doy+'/Spectrum/'
    os.system(W)
except:
    pass

try:
    folder_path2 = r'/home/pi/Desktop/Lab_jamming/Output/PSD/Power_L1/NoJam/'
    file_type2 = '*.csv'
    files2 = glob.glob(folder_path2 + file_type2)
    min_file2 = min(files2, key=os.path.getctime)
    X='pscp -P 8030 -pw b8yps2e5 '+min_file2+' jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L1/'+year+'/'+doy+'/Text/'
    os.system(X)
except:
    pass

try:
    folder_path3 = r'/home/pi/Desktop/Lab_jamming/Output/PSD/Power_L5/NoJam/'
    file_type3 = '*.csv'
    files3 = glob.glob(folder_path3 + file_type3)
    min_file3 = min(files3, key=os.path.getctime)
    Y='pscp -P 8030 -pw b8yps2e5 '+min_file3+' jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L5/'+year+'/'+doy+'/Text/'
    os.system(Y)
except:
    pass
    
Z='pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Power_L1/Jam/* jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L1/'+year+'/'+doy+'/Text/'
O='pscp -P 8030 -pw b8yps2e5 /home/pi/Desktop/Lab_jamming/Output/PSD/Power_L5/Jam/* jamming@161.246.18.204:/home/jamming/NAS/TELECOM/L5/'+year+'/'+doy+'/Text/'

os.system(Z)
os.system(O)

os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L1/*')
os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/NoJam/L5/*')
os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Power_L1/NoJam/*')
os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Power_L5/NoJam/*')
os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Power_L1/Jam/*')
os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Power_L5/Jam/*')
os.system('rm -rf /home/pi/Desktop/Lab_jamming/Output/PSD/Jam/L1_Error/*')
