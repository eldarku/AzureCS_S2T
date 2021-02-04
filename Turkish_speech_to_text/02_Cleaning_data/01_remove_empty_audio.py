import shutil
import os
import sys
import soundfile as sf


dirroot = "D:\\tr_speechdata"
dirtrain=dirroot+"\\recovered"

f=open(dirtrain+"\\"+"_label.txt", "r", encoding="utf-8-sig")
lines = f.readlines()
f.close()
fw=open(dirtrain+"\\"+"_label.txt", "w", encoding="utf-8-sig")

#remove all .wav files less than 1 seconds length and corresponding lines in _label.txt

for root, dirs, files in os.walk(dirtrain):
    for file in files:
        if file.split(".")[1]== "wav":
            sf_file = sf.SoundFile(root+"\\"+file)
            ln=(len(sf_file) / sf_file.samplerate)
            sf_file.close()
            if (ln<1):
                sf_file.close()
                print(file+" removed, length is " + str(ln))
                os.remove(root+"\\"+file)
                for i, line in enumerate(lines):
                    if (line.startswith(file)==True):
                        print("removed line: "+ line+"line number is "+str(i)+"\n")
                        _=lines.pop(i)

 
for item in lines:
    _=fw.write(item)



fw.close()
