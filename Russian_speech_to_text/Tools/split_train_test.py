import shutil
import os
import sys
import zipfile
import fileinput
import re
from sklearn.model_selection import train_test_split

dirroot = "D:\\ru_speechdata"
dirtrain=dirroot+"\\recovered"

rand_train=dirroot+"\\rand_train"
rand_test=dirroot+"\\rand_test"

if not os.path.exists(rand_train):
    os.mkdir(rand_train)

if not os.path.exists(rand_test):
    os.mkdir(rand_test)

f = open(dirtrain+"\\"+"_label.txt", "r", encoding="utf-8-sig")
lines = f.readlines()
f.close()


train_fw = open(rand_train+"\\"+"_label.txt", "w", encoding="utf-8-sig")
test_fw = open(rand_test+"\\"+"_label.txt", "w", encoding="utf-8-sig")


lines_train, lines_test = train_test_split(lines,test_size=0.1) 


for i, line in enumerate(lines):
    spl = lines[i].split("\t", 1)
    if lines[i] in lines_train:
        _=shutil.copy(dirtrain+"\\"+spl[0],rand_train+"\\"+spl[0])

    else:
        _=shutil.copy(dirtrain+"\\"+spl[0],rand_test+"\\"+spl[0])

        
for item in sorted(lines_train):
    _=train_fw.write(item)

for item in sorted(lines_test):
    _=test_fw.write(item)

train_fw.close()
test_fw.close()