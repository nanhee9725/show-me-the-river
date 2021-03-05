# 여기는 데이터 쌓는곳

import pickle

import requests
from flask import json
from pymongo import MongoClient
import xmltodict
client = MongoClient('localhost', 27017)
db = client.dbsparta
url = "http://opendata.kwater.or.kr/openapi-data/service/pubd/myportal/travel/list?searchTypeCd=02&regionCd=GU&numOfRows=1000&pageNo=1&serviceKey=imG5GZCUuCRZfkWsdGDQoX8j7OAfiwXFC%2BippX80egTFswLEMUUFv8kdFk2p%2BkRcTBXQUcHWNGfgN83SBpP9RA%3D%3D"
response = requests.get(url)

# url = 'http://opendata.kwater.or.kr/openapi-data/service/pubd/myportal/travel/list'
# # request 할 때 필요한 parameter
# params = {'searchTypeCd': '01', 'regionCd': 'HA', 'numOfRows': '1000', 'pageNo': '1', 'serviceKey': 'imG5GZCUuCRZfkWsdGDQoX8j7OAfiwXFC%2BippX80egTFswLEMUUFv8kdFk2p%2BkRcTBXQUcHWNGfgN83SBpP9RA%3D%3D'}
# response = requests.get(url, params=params)

result = json.loads(json.dumps(xmltodict.parse(response.text)))
print(result)
items = result['response']['body']['items']['item']


print(items)
for item in items:
    print(item)
    # print(item['course'])
    doc = {
        'searchType': item['searchType'],
        'region': item['region'],
        'regionCd': item['regionCd'],
        'title': item['title'],
        'intro': item['intro'],
        # 'course': item['course'],
    }

    db.river.insert_one(doc)

    # import pickle
    # with open('items','wb') as file:
    #     pickle.dump(searchType, file)
    #     pickle.dump(regionCd, file)
    #     pickle.dump(title, file)
    #     pickle.dump(intro, file)
    #     pickle.dump(course, file)
    #
    #
    # json_string = json.dumps(item, ident=3)
    # print(json_string)
    #
    # db.river.insert_one(doc)
    #
    # import pickle
    # with open('items','rb') as file :
    #     searchType = pickle.load(file)
    #     regionCd = pickle.load(file)
    #     title = pickle.load(file)
    #     intro = pickle.load(file)
    #     course = pickle.load(file)
    #     print(searchType)
    #     print(regionCd)
    #     print(title)
    #     print(intro)
    #     print(course)

