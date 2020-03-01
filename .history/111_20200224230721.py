import requests

url1 = 'https://elegantecasa.ru/google_merchant/316a0fcf-a065-4024-9d50-de00ab1f800a.xml'
url2 = 'https://elegantecasa.ru/google_merchant/b7d7c5b3-2f70-4f5b-b49f-a0caef5c2b39.xml'


r = requests.get(url1)

data = r.text

with open('1.txt', 'w', encoding='utf-8') as f:
    f.write(data)