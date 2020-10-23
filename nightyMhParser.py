# -*- coding: utf-8 -*-

"""
Parser for 90mh.com
"""

import requests
import bs4
import re
import json

baseURL = "http://www.90mh.com"


def getChapterList(url):
    with open("./config.json", "r") as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    allChapLis = formatedSite.findAll(id="chapter-list-10")
    res = []
    for div in allChapLis:
        allLinks = div.findAll('a')
        for aTags in allLinks:
            det = aTags.attrs
            res.append({"Text": aTags.getText()[1:-1], "URL":baseURL+det['href']})
    return res

def getDlSetting(url):
    with open("./config.json", "r") as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    allImgAddr = re.search(r"chapterImages = \[(.*)\]",str(formatedSite)).group(1).split(",")
    allImgAddr = list(map(lambda x: x[1:-1], allImgAddr))
    bed = "https://js1.zzszs.com.cn/" + re.search(r'chapterPath = "(.*?)"', str(formatedSite)).group(1)
    pathURLs = []
    ind = 0
    for x in allImgAddr:
        pathURLs.append({"Name":"%05d"%ind, "URL" : bed + x})
        ind += 1
    return pathURLs, {}
        