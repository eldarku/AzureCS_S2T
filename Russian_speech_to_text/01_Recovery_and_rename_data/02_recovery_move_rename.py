import shutil
import os
import sys
import fileinput
import re


dirroot = "D:\\ru_speechdata"
dirinput = dirroot+"\\raw_input"
dirtrain=dirroot+"\\recovered"


if not os.path.exists(dirtrain):
    os.mkdir(dirtrain)

#we need to rename .wav files in the transcript txt file
fobj = open(dirtrain+"\\"+"_label.txt", "w", encoding="utf-8-sig")


for root, dirs, files in os.walk(dirinput):
    for file in files:
        if file== "original.wav": #name of small sentence audio file
            #print(root+"\\"+file)
            spl = root.split("\\") 
            #copy .wav file to dirtrain, [len(dirroot.split("\\"))+1] is the name of folder, 
            #then replace " " with "_" and replace audio file name "original" to the folder name where it located
            if spl[-2][:4]=='data': #only located in the correct folders (data*) files needed
                _=shutil.copy(root+"\\"+file, dirtrain+"\\"+spl[len(dirroot.split("\\"))+1].replace(" ","_")+"_"+"sample"+file.replace("original",spl[-3])) 
        if file== "input.txt": #raw input text
            spl = root.split("\\")
            #print(root+"\\"+file)
            if spl[-2][:4]=='data': #only located in the correct folders (data*) files needed
                for line in fileinput.input(root+"\\"+file, openhook=fileinput.hook_encoded("utf-8"), inplace=False):
                    #same thing with the text in the transcript: use parent folder name + "sample"+sample number + extension + tab+line content
                    line=spl[len(dirroot.split("\\"))+1].replace(" ","_")+"_"+"sample"+spl[-3]+".wav"+"\t"+line
                    _=fobj.write(line)
                fileinput.close()

fobj.close()


