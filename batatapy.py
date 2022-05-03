import json
import time
import requests

parameters = {
    "index": 0
}

while True:
    min = time.localtime()
    if min.tm_min == 0 or min.tm_min == 30:
        print(min.tm_min)
        url = requests.get('https://api.guildwars2.com/v2/commerce/prices?id=96978', params=parameters)
        text = url.text
        data = json.loads(text)
        print(data['buys'])
        print(data['sells'])
    else:
        print(min.tm_min)
        print("not yet time!")
    time.sleep(60)
