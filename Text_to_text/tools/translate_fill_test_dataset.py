import math, os, requests, uuid, json
import pandas as pd

#translate multiple sentences in all directions to test model accuracy and find weak points

#sourcepath= input("Enter full path to the excel file with test sentences:\n")

sourcepath="D:\\textdata\\input\\merged_test_set.xlsx"
src_data = pd.read_excel(io=sourcepath)


subscription_key = '<subscription_key>'
endpoint = 'https://api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

#read first three columns from the first worksheet
src_ru=src_data.copy().iloc[:,0]
src_en=src_data.copy().iloc[:,1]
src_tr=src_data.copy().iloc[:,2]

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


#preparing sentence structure for the cognitive service
def add_text(src):
    for  i in range(len(src)):
        src[i]={ 'text' : src[i] }  

# for all 3 languages
[add_text(x) for x in [src_ru,src_en,src_tr]]

#initializing dictionary for translations
translations={'ru_en_general': [], 'ru_en_custom': [], 'ru_tr_general': [], 'ru_tr_custom': [], 
'tr_en_general': [], 'tr_en_custom': [], 'tr_ru_general': [], 'tr_ru_custom': []}

#batch size (how many sentences send at once), 10 is optimal, to avoid exceeding limit
nbatch=10 

def translate(src_lng,dst_lng1,dst_lng2,CustomURL,model_type):
    #construct params for url: we translate each sentence to two languages at once
    #+customURL part used for custom translator model
    params = '&from='+src_lng+'&to='+dst_lng1+'&to='+dst_lng2+CustomURL
    constructed_url = endpoint + path + params
    # using appropriate dataset - src_ru,src_en or src_tr
    src=globals()['src_'+src_lng]
    #calculate batch amount needed
    for l in range(math.ceil(len(src)/nbatch)):
        #construct current batch and convert it to list
        body = list(src[(l*nbatch):((l+1)*nbatch)])
        #run the request
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        #fill two elements - from one (source) language to two other (destination) languages
        translations[src_lng+'_'+dst_lng1+'_'+model_type].extend([x['translations'][0]['text'] for x in response])
        translations[src_lng+'_'+dst_lng2+'_'+model_type].extend([x['translations'][1]['text'] for x in response])

#ru->en and en->tr translations
translate('ru','en','tr','','general')
#tr->en and tr->ru translations
translate('tr','en','ru','','general')

#ru->en and en->tr translations for custom model
translate('ru','en','tr','&category=eb160f6f-f8d4-4f3b-becf-ac4163da8f94-CLOTHIN','custom')
#tr->en and tr->ru translations for custom model
translate('tr','en','ru','&category=eb160f6f-f8d4-4f3b-becf-ac4163da8f94-CLOTHIN','custom')

#merge source and transaltions
data=pd.concat([src_data, pd.DataFrame(translations)], axis=1)
 
#export to excel
data.to_excel(sourcepath.replace('.xl','_translated.xl'), index=False)