import math, os, requests, uuid, json
import pandas as pd
from sklearn.model_selection import train_test_split

#prepare ready-to-upload sentence files from multi-sheet excel input file


#sourcepath= input("Enter full path to the excel file with test sentences:\n")

sourcepath="D:\\textdata\\input\\Dictionary.xlsx"


data=[]
xl = pd.ExcelFile(sourcepath)

#read all worksheets
for sh in xl.sheet_names:
    #only first three columns
    cur_sheet=xl.parse(sh).iloc[:, 0:3]
    #correct order is important
    cur_sheet.columns=['Sentences_RU', 'Sentences_EN', 'Sentences_TR']
    data.append(cur_sheet)

#combined data
combined_df = pd.concat(data, ignore_index=True, sort=False)

#drop rows with at least one empty value
combined_df.dropna(inplace=True)

#drop linebreaks and strip the data
for column in combined_df.columns:
    combined_df[column]=combined_df[column].str.replace('\n','').str.replace('\t','').str.replace('\r','').str.replace('"','').str.replace(';',',').str.strip()


#export whole dataset 
for column in combined_df.columns:
    combined_df[column].to_csv(sourcepath[::-1].split('.',1)[1][::-1]+'_'+'full_'+column+'.align', index=False, header=False, index_label=False )


#tsv files, if needed
#combined_df[['Sentences_RU', 'Sentences_EN']].to_csv(sourcepath[::-1].split('.',1)[1][::-1]+'_'+'full_'+'RU_EN'+'.tsv', sep='\t', index=False, header=False, index_label=False )
#combined_df[['Sentences_TR', 'Sentences_EN']].to_csv(sourcepath[::-1].split('.',1)[1][::-1]+'_'+'full_'+'TR_EN'+'.tsv', sep='\t', index=False, header=False, index_label=False )

#combined_df[['Sentences_EN', 'Sentences_RU']].to_csv(sourcepath[::-1].split('.',1)[1][::-1]+'_'+'full_'+'EN_RU'+'.tsv', sep='\t', index=False, header=False, index_label=False )
#combined_df[['Sentences_EN', 'Sentences_TR']].to_csv(sourcepath[::-1].split('.',1)[1][::-1]+'_'+'full_'+'EN_TR'+'.tsv', sep='\t', index=False, header=False, index_label=False )


#random split into train/test 90%/10%
train_set, test_set = train_test_split(combined_df,test_size=0.1) 

#export train dataset
for column in train_set.columns:
    train_set[column].to_csv(sourcepath[::-1].split('.',1)[1][::-1]+'_'+'train_'+column+'.align', index=False, header=False, index_label=False )

#export test dataset
for column in test_set.columns:
    test_set[column].to_csv(sourcepath[::-1].split('.',1)[1][::-1]+'_'+'test_'+column+'.align', index=False, header=False, index_label=False )

#export test dataset for later treanslation quality testing
test_set.to_excel(sourcepath[::-1].split('.',1)[1][::-1]+'_test_set.xlsx', index=False )


#combined_df.to_excel(sourcepath[::-1].split('.',1)[1][::-1]+'_whole_dataset.xlsx', index=False )



