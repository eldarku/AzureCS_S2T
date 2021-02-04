import shutil
import os
import sys
 

dirroot = "D:\\tr_speechdata"
dirtrain = dirroot+"\\recovered"

f = open(dirtrain+"\\"+"_label.txt", "r", encoding="utf-8-sig")
lines = f.readlines()
f.close()
fw = open(dirtrain+"\\"+"_label.txt", "w", encoding="utf-8-sig")

#manual replace, then auto-transliterate

for i, line in enumerate(lines):
    spl = lines[i].split("\t", 1)
    spl[1]=spl[1].replace('\t', ' ').replace('\u200b', '').strip()
    lines[i] = spl[0]+"\t"+spl[1]+"\n"

for item in lines:
    _ = fw.write(item)

fw.close()
 
    



 

 