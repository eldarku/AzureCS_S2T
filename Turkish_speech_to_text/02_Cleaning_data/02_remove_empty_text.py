import shutil
import os
import sys


dirroot = "D:\\tr_speechdata"
dirtrain = dirroot+"\\recovered"

f = open(dirtrain+"\\"+"_label.txt", "r", encoding="utf-8-sig")
lines = f.readlines()
f.close()
fw = open(dirtrain+"\\"+"_label.txt", "w", encoding="utf-8-sig")


del_i=[]

#remove all empty (less than 5 symbols including endline symbol) lines in the text transcript and corresponding .wav files


for i, line in enumerate(lines):
    spl = lines[i].split("\t", 1)
    if len(spl[1])<5:
        print(spl[0]+" line removed, text is " + spl[1]+"line number is "+str(i)+"\n")
        os.remove(dirtrain+"\\"+spl[0].strip())
        del_i.append(i)

lines = [ line for i,line in enumerate(lines) if i not in del_i]
        
for item in lines:
    _=fw.write(item)


fw.close()
