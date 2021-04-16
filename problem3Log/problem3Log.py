from datetime import datetime

fileName1 = "problem3Log\myLog.txt"
with open(fileName1,'r') as lg:
    dt = str(datetime.now()).replace(':','-').split()
    newFileName = "problem3Log"+"\Error_Warn_"+''.join(dt)+".txt"
    with open(newFileName,'a') as errWarn:
        eachLines = lg.readlines()
        for line in eachLines:
            temp = line.split()
            if temp[4].lower() in ['warn','error']:
                wr = ''.join(temp[16:])
                errWarn.write(temp[4]+'-'+wr+'\n')


        
