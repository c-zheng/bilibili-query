#!/usr/bin/env python3
import requests
import sys

def frontpage_ranking(cat):
    url = "http://www.bilibili.com/index/catalogy/" + str(cat) + "-3day.json"
    r = requests.get(url)
    if  r.status_code == 200:
        resp = r.json()
        for i in range(10):
            print(resp['hot']['list'][int(i)]['title'])
            print('Up: ', resp['hot']['list'][int(i)]['author'])
            print('Views: ', resp['hot']['list'][int(i)]['play'])
            print('=======')

if __name__ == "__main__":
    frontpage_ranking(sys.argv[1])
