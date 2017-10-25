# coding=utf8
# download video
import datetime
import urllib.request
import os
import sys,time

#url = sys.argv[1]
#dir = sys.argv[2]

def downloadflv(url, dir):
    print('1') #download started
    if os.path.exists('E:/%s' %dir) == False:
        os.mkdir(r'E:/%s' %dir)
    try:
        urllib.request.urlretrieve(url,"E:/%s/video.flv" %dir)
        time.sleep(2*60)
        print('3') #download ended
    except Exception as e:
        print ("2") #download failed
downloadflv("http://txy.live-play.acgvideo.com/live-txy/341771/live_19001465_5479356.flv?wsSecret=eb09c50a6f5f84bea39168ace949ddb8&wsTime=1499671461","TEST")
