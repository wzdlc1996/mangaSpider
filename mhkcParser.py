# -*- coding: utf-8 -*-

import requests
import bs4
import json

baseURL = "http://mh12306.com"


def getChapterList(url):
    with open("./config.json", "r") as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    allChapLis = formatedSite.findAll(id="epList")
    res = []
    for div in allChapLis:
        allLinks = div.findAll('a')
        for aTags in allLinks:
            det = aTags.attrs
            res.append({"Text": aTags.getText(), "URL":baseURL+det['href']})
    return res

def getDlSetting(url):
    with open("./config.json", "r") as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    allImgLis = formatedSite.findAll(id="ep-read")[0].findAll('img')
    ind = 0
    pathURLs = []
    for img in allImgLis:
        det = img.attrs
        pathURLs.append({"Name":"%05d"%ind, "URL" : det['data-src']+"&i=1"})
        ind += 1
    return pathURLs, {}
        