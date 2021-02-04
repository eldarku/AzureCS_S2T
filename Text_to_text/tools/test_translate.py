import os, requests, uuid, json
#set these parameters for test
#CustomURL=''
CustomURL='&<CustomURL>'
src_lng='ru'
dst_lng1='en'
dst_lng2='tr'


subscription_key = '<subscription_key>'
endpoint = 'https://api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

params = '&from='+src_lng+'&to='+dst_lng1+'&to='+dst_lng2+CustomURL
constructed_url = endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

#set sentences for test
body = [
{
    'text': 'Тестовая фраза на русском языке'
}
]

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': ')))


