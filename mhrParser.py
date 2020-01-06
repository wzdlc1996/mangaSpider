# -*- coding: utf-8 -*-

"""
Parser for www.manhuaren.com
"""

import dukpy
import re
import requests
import bs4
import json

baseURL = "https://www.manhuaren.com/m938147/"
#imgURL = "https://i.hamreus.com"

def getChapterList(url):
    with open("./config.json",'r') as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    infoJS = re.search(r">eval\((.*)\)\n<",str(formatedSite)).group(1)
    return dukpy.evaljs(infoJS)
    allChapLis = formatedSite.findAll(id="detail-list-select-1")
    res = []
    for div in allChapLis:
        allLinks = div.findAll('a')
        for aTags in allLinks:
            det = aTags.attrs
            res.append({"Text": aTags.getText(), "URL":baseURL+det['href']})
    return res