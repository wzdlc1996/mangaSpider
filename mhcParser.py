import requests as rq
import bs4
import lzstring
import re

testUrl = "https://www.manhuacat.com/manga/5611.html"
baseUrl = "https://p1.manhuacat.com/uploads/"

def getChapterList(url = testUrl):
    z = bs4.BeautifulSoup(rq.get(url).content, 'lxml')
    z = z.findAll("a", class_="fixed-a-es")
    return [{"URL": x.attrs["href"], "Text": x.attrs["title"]} for x in z]

def getDlSetting(url):
    z = bs4.BeautifulSoup(rq.get(url).content, "lxml")
    img_data = re.match(r"[\w\W]*img_data = \"(.*)\"", str(z)).group(1)
    imgList = lzstring.LZString.decompressFromBase64(img_data).split(",")
    pathURLs = []
    for i in range(len(imgList)):
        pathURLs.append({"Name": "%05d" % i, "URL": baseUrl + imgList[i]})
    return pathURLs, {"Referer" : url}
        

