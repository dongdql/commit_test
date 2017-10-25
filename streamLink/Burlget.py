# coding=utf8

# get bilibili live stream url
import urllib
import urllib.request
from lxml import etree
import re
import sys

#roomUrl = sys.argv[1] #ֱ����url����
LIVEURL = 'http://live.bilibili.com/api/playurl?player=1&quality=0&cid=' #bilibiliֱ����url��׼url��ʽ��cid�Ƿ����

# data processing
def getlist(txt):
    mylist= re.findall(r"(?<=<url><!).*?(?=></url>)",txt,re.DOTALL)
    return mylist  

#�����ȡbilibiliֱ��Դurl
# request interface address
def getLiveUrl(url):
    webPage=urllib.request.urlopen(url)
    html = webPage.read().decode('utf-8')
    html = etree.HTML(html)
    script = html.xpath('//script/text()')
    cid = script[0]
    cid = cid.strip()
    cid = cid.replace('\n', '')
    cid = cid.replace(' ', '')
    cid = cid.split(';')[1]
    cid = cid.split('=')[1]
    url = 'http://live.bilibili.com/api/playurl?player=1&quality=0&cid=' + str(cid)
    request = urllib.request.Request(url, headers = {
        'X-Requested-With': 'ShockwaveFlash/25.0.0.127',
    })
    response = urllib.request.urlopen(request)
    #�ַ�������
    list = response.read()
    list = str(list)
    list = list.strip()
    list = list.replace('\n', '')
    list = list.replace(' ', '')
    list = list.split('CDATA')[2]
    list = list.split(']]')[0]
    urlstring = list[1:]
    return urlstring
    
videoURL = getLiveUrl("https://live.bilibili.com/2116479")
print(videoURL)
