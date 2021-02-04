import shutil
import os
import sys
import soundfile as sf


dirroot = "D:\\tr_speechdata"
dirtrain=dirroot+"\\recovered"

fobj = open(dirroot+"\\"+"_length.csv", "w", encoding="utf-8-sig")


for root, dirs, files in os.walk(dirtrain):
    for file in files:
        if file.split(".")[1]== "wav":
            f = sf.SoundFile(root+"\\"+file)
            _=fobj.write(file+", "+str(len(f) / f.samplerate)+"\n")

fobj.close()


