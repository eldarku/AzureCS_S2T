import shutil
import os
import sys
import zipfile



dirroot = "D:\\ru_speechdata"
dirinput = dirroot+"\\raw_input"


#extract all the data into dirinput (in my case D:\\speechdata\\raw_input)
#in my case it looks like that:
              
#recursively extract all sentences archives inplace

for root, dirs, files in os.walk(dirinput):
    for file in files:
        if file.split(".")[1]== "zip" and file.split(".")[0]!="data": #unzip just small sentence archives, skipp big and possibly damaged ones 'data.zip'
            #print(root+"\\"+file)
            
            try:
                with zipfile.ZipFile(root+"\\"+file, 'r') as zip_ref:
                    zip_ref.extractall(root+"\\"+file.split(".")[0])  #unzip inplace
            except Exception as exc:
                print(exc)
                pass

