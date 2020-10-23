# -*- coding: utf-8 -*-

"""
Parser for www.manhuabei.com
"""

import re
import requests
import bs4
import json
import execjs

baseURL = "https://www.manhuabei.com"
imgURL = "https://img01.eshanyao.com/showImage.php?url="
imgURLnew = "https://manga.mipcdn.com/i/s/img01.eshanyao.com/"

def getChapterImageInfo(formatedSite):
    scptText = str(formatedSite.findAll("script"))
    return re.search(r'chapterImages = "(.*?)"',scptText).group(1)

def cryptoDe(info):
    js = ''
    with open("./obfsJsScr/manhuabei20200824.js", "r") as f:
        for line in f.readlines():
           js += line 
    ctx = execjs.compile(js)
    deInfo = ctx.call("decrypt20180904", info)
    return deInfo

def getChapterList(url):
    with open("./config.json",'r') as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    allChapLis = formatedSite.findAll(id="chapter-list-1")
    res = []
    for div in allChapLis:
        allLinks = div.findAll('a')
        for aTags in allLinks:
            det = aTags.attrs
            res.append({"Text": re.search(r'\n([0-9]*[^ ]*) ',aTags.getText())\
                        .group(1), "URL":baseURL+det['href']})
    return res
    

def getCoreInfo(url):
    with open("./config.json", "r") as f:
        conf = json.load(f)
    getSite = bs4.BeautifulSoup(requests.get(url, headers = {"User-Agent": \
                                conf["User-Agent"]}).content, features="lxml")
    chpPath = re.search(r'chapterPath = "(.*?)"', str(getSite.findAll("script"))).group(1)
    return cryptoDe(getChapterImageInfo(getSite)), chpPath

def getDlSetting(url):
    data, chp = getCoreInfo(url)
    pathURLs = []
    picid = 0
    for pic in data:
        if re.match(r"^http", pic):
            fullurl = imgURL+pic
        else:
            fullurl = imgURLnew + chp + pic
        pathURLs.append({"Name": "%05d"%picid, "URL": fullurl})
        picid += 1
    return pathURLs, {}