import shutil
import os
import sys
import re


dirroot = "D:\\ru_speechdata"
dirtrain = dirroot+"\\recovered"

f = open(dirtrain+"\\"+"_label.txt", "r", encoding="utf-8-sig")
lines = f.readlines()
f.close()


for i, line in enumerate(lines):
    spl = lines[i].split("\t", 1)
    line = re.sub(r"[^A-Za-z\s]", "", spl[1].strip())
    words = line.split()
    for word in words:
        print(i, lines[i], word)
   

