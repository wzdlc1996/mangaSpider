# -*- coding: utf-8 -*-

"""
Parser for www.manhuaren.com
"""

import dukpy
import re
import requests
import bs4
import json

baseURL = "https://www.manhuaren.com"

#imgURL = "https://i.hamreus.com"

def getChapterList(url):
    with open("./config.json",'r') as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    chplis = formatedSite.findAll(attrs = {"class" : "chapteritem"})
    res = []
    for aTag in chplis:
        res.append({"Text" : aTag.getText(), "URL":baseURL + aTag.attrs["href"]})
    return res

def getCoreInfo(url):
    with open("./config.json",'r') as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    infoJS = re.search(r">eval\((.*)\)\n<",str(formatedSite)).group(1)
    sol = [re.search(r"\'(.*?)\'",z).group(1) for z in dukpy.evaljs("("+infoJS+")").split(",")]
    return sol

def getDlSetting(url):
    data = getCoreInfo(url)
    pathURLs = []
    picid = 0
    for x in data:
        pathURLs.append({"Name": "%05d"%picid, "URL": x})
        picid += 1
    return pathURLs, {"Referer": url}