import requests

req = 'https://datazen.katren.ru/calendar/day/'
req_result = requests.request('GET', req)
print(req_result)
# <Response [200]>
print(req_result.json())
# {'holiday': False, 'date': '2019-05-22'}
