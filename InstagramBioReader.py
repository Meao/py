"""
Разработка скрипта для получения и сохранения данных социальных сетей Twitter или Instagram.
"""

import json
import requests
from bs4 import BeautifulSoup


class InstagramBioReader:
    def __init__(self, url):
        self.url = url

    def __request_url(self, url):
        try:
            response = requests.get(
                url,
                headers={'User-Agent': 'Chrome/65.0.3325.181'})
            response.raise_for_status()
        except Exception as e:
            raise e
        else:
            return response.text

    def extract_json(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('body')
        script_tag = body.find('script')
        raw_string = script_tag.string.strip().replace('window._sharedData =', '').replace(';', '')
        return json.loads(raw_string)

    def page_data(self):
        results = {}
        try:
            response = self.__request_url(self.url)
            json_data = self.extract_json(response)
            data = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
        except Exception as e:
            raise e
        else:
            results['biography'] = data['biography']
            results['full_name'] = data['full_name']
        return results


url = 'https://www.instagram.com/herzenka_lib/'
instagram = InstagramBioReader(url)
data = instagram.page_data()

print(data)

# Serializing json  
json_object = json.dumps(data, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 