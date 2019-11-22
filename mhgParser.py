import dukpy
import lzstring
import re
import requests
import bs4
import json

baseURL = "https://www.manhuagui.com"
imgURL = "https://i.hamreus.com"

def getChapterList(url):
    with open("./config.json",'r') as f:
        conf = json.load(f)
    baseSite = requests.get(url, headers = {"User-Agent": conf["User-Agent"]})
    formatedSite = bs4.BeautifulSoup(baseSite.content, features="lxml")
    allChapLis = formatedSite.findAll(id="chapter-list-0")
    res = []
    for div in allChapLis:
        allLinks = div.findAll('a')
        for aTags in allLinks:
            det = aTags.attrs
            res.append({"Text": aTags.getText(), "URL":baseURL+det['href']})
    return res
    

def getCoreInfo(url):
    with open("./config.json", "r") as f:
        conf = json.load(f)
    getSite = bs4.BeautifulSoup(requests.get(url, headers = {"User-Agent": conf["User-Agent"]}).content, features="lxml")
    jsSlic = re.search(r">window.*(\(function\(p.*?)</script>", str(getSite)).group(1)
    coreStr = re.search(r"[0-9],'([A-Za-z0-9+/=]+?)'", jsSlic).group(1)
    decStr = lzstring.LZString.decompressFromBase64(coreStr)
    jsNew = re.sub(r"'[A-Za-z0-9+/=]*'\[.*\]\('\\x7c'\)", "'"+decStr+"'.split('|')", jsSlic)
    sol = dukpy.evaljs(jsNew)
    return json.loads(re.search(r"(\{.*\})",sol).group(1))

def getDlSetting(url):
    data = getCoreInfo(url)
    pathURLs = []
    picid = 0
    for pic in data['files']:
        mangaurl = imgURL+data['path']+re.match(r".*?\.[a-z]*", pic).group(0)
        fullurl = mangaurl+"?cid="+str(data['cid'])+"&md5="+data['sl']['md5']
        pathURLs.append({"Name": "%05d"%picid, "URL": fullurl})
        picid += 1
    refURL = baseURL+"/comic/"+str(data['bid'])+"/"+str(data['cid'])+".html"
    return pathURLs, {"Referer": refURL}