import requests

URL = 'http://api.ipify.org?format=json'

res = requests.get(URL)
#print(res.text)


