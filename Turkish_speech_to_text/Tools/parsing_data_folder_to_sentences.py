import shutil
import os
import sys
import fileinput
import re


dirroot = "D:\\tr_speechdata"
dirinput = dirroot+"\\data"
dirtrain=dirroot+"\\data_recovered"

#some folders where provided as a single archive, this script can help to parse it to the same structure as all other data

if not os.path.exists(dirtrain):
    os.mkdir(dirtrain)

for root, dirs, files in os.walk(dirinput):
    for file in files:
        if (file.split(".")[0][:6]== "sample") & (file.split(".")[1]== "wav"): #name of small sentence audio file
            #print(root+"\\"+file)
            spl = root.split("\\") 
            os.makedirs(dirtrain+"\\"+spl[len(dirroot.split("\\"))+1].replace(" ","_")+"\\voice\\speech\\"+file.split(".")[0][6:]+"\\data"+file.split(".")[0][6:]+ "\\audio\\",exist_ok=True)
            _=shutil.copy(root+"\\"+file,dirtrain+"\\"+spl[len(dirroot.split("\\"))+1].replace(" ","_")+"\\voice\\speech\\"+file.split(".")[0][6:]+"\\data"+file.split(".")[0][6:]+ "\\audio\\"+"original.wav")






for root, dirs, files in os.walk(dirinput):
    for file in files:
        if (file=="transcript.txt"):
    
            f = open(root+"\\"+file, "r", encoding="utf-8")
            lines = f.readlines()
            spl = root.split("\\") 
            for i, line in enumerate(lines):
                n=lines[i].split("\t", 1)[0].split(".")[0][6:]
                t=lines[i].split("\t", 1)[1].strip()+"\n"
                spl = root.split("\\")
                os.makedirs(dirtrain+"\\"+spl[len(dirroot.split("\\"))+1].replace(" ","_")+"\\voice\\speech\\"+n+"\\data"+n+ "\\text\\")
                fobj = open(dirtrain+"\\"+spl[len(dirroot.split("\\"))+1].replace(" ","_")+"\\voice\\speech\\"+n+"\\data"+n+ "\\text\\"+"input.txt", "w", encoding="utf-8")
                _=fobj.write(t)
                fobj.close()
            f.close()

 


