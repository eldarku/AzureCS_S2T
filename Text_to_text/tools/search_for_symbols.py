import shutil
import os
import sys
import re
import pandas 


dirroot = "D:\\textdata\\input"

 

for root, dirs, files in os.walk(dirroot):
    for file in files:
        if file.split(".")[1]== "txt":

            f=open(dirroot+"\\"+file, "r", encoding="utf-8")
            lines = f.readlines()
            print(file[0:-4])
            for i, line in enumerate(lines):
                if (re.search(r'(.*[.;:].*[^" \n])',lines[i].replace(u'\xa0', u' ').strip())!=None):
                    
                    print(i, lines[i].strip())
 

            f.close()

 
