import json
import time
import requests

parameters = {
    "index": 0
}
h = time.localtime()
min = time.localtime()
print(h.tm_hour,':',min.tm_min)
print("-- -- -- --")
while True:
    time.sleep(1800)
    url = requests.get('https://api.guildwars2.com/v2/commerce/prices?id=96978', params=parameters)
    text = url.text
    data = json.loads(text)
    print(h.tm_hour,':',min.tm_min)
    print("buy quantity:", data['buys']['quantity'])
    print("buy price:", data['buys']['unit_price'])
    print("sell quantitiy:", data['sells']['quantity'])
    print("sell price:", data['sells']['unit_price'])
    print("-- -- -- --")






