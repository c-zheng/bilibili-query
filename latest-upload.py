#!/usr/bin/env python3
import requests
import sys

def latest_upload(mid):
    payload = {'mid':mid, 'pagesize':1, 'page':1}
    r = requests.post('http://space.bilibili.com/ajax/member/getSubmitVideos', data = payload)
    retcode = None
    if  r.status_code == 200:
        resp = r.json()
        if resp['data']['count'] != 0:
            aid = (resp['data']['vlist'][0]['aid'])
            title = (resp['data']['vlist'][0]['title'])
            length = (resp['data']['vlist'][0]['length'])
            retcode = {"aid":aid, "title":title, "length":length}
    return retcode

if __name__ == "__main__":
    latest = latest_upload(sys.argv)
    if latest != None:
        print(latest["aid"], latest["title"], latest["length"])
    else:
        print("Nothing can be found!")
