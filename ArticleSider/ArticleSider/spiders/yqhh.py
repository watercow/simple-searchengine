import requests
import random
import re
from tools.crawl_xici_ip import GetIP


def get_cookie():
    url = 'http://yqhh.werner.wiki/draw/'
    req = requests.get(url)
    print (req.headers)
    text = 'token=52e2c875194949c0fd4bf605b15b6e44'
    cookie = re.match('.*token=(.*?);', text)
    if cookie:
        print (cookie.group(1))
    return

# set header
header = {
    'Host'       : 'yqhh.werner.wiki',
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
    'Accept'     : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Cookie'     : "token=5dc53bf3e30fd7040ca3d34d9794164a; csrftoken=SsecrzNZg9V3nF3fl7IIIWOS00xuK8So"
}

def draw():
    post_url = 'http://yqhh.werner.wiki/set/'
    get_ip = GetIP()
    for i in range(0,20):
        post_data = {
            'color'               : 6,
            'number'              : i,
            'csrfmiddlewaretoken' : 'SsecrzNZg9V3nF3fl7IIIWOS00xuK8So'
        }
        ip = get_ip.get_random_ip()
        proxy_dict = {
            "http": ip
        }
        print (ip)
        response = requests.post(post_url, data=post_data, headers=header, proxies=proxy_dict)
        print (response.text)
    return

draw()
