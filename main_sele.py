from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import re
import requests as rq
import bs4
import lzstring
import os
import time
import random
import progressbar

chapURL = "https://www.manhuacat.com/manga/5611.html"
z = bs4.BeautifulSoup(rq.get(chapURL).content, "lxml").findAll("a", class_ = "fixed-a-es")
chaps = [{"url": x.attrs["href"], "name": x.attrs["title"]} for x in z]

def getPicNumber(url):
    z = bs4.BeautifulSoup(rq.get(url).content, "lxml")
    img_data = re.match(r"[\w\W]*img_data = \"(.*)\"", str(z)).group(1)
    return len(lzstring.LZString.decompressFromBase64(img_data).split(","))

firefoxOpts = Options()
firefoxOpts.add_argument("-headless")

browser = webdriver.Firefox(executable_path="./driver/geckodriver", options=firefoxOpts)

for i in progressbar.progressbar(range(len(chaps))):
    n = getPicNumber(chaps[i]["url"])
    fold = "./test/{}".format(chaps[i]["name"])
    try:
        os.mkdir(fold)
    except FileExistsError:
        pass
    for j in range(n):
        curUrl = re.match(r"(.*)\.html", chaps[i]["url"]).group(1) + "_" + str(j + 1) + ".html"
        browser.get(curUrl)
        picUrl = browser.find_elements_by_tag_name("img")[1] \
               .get_attribute("src")


        with open(fold + "/%05d.webp" % j, "wb") as f:
            cont = rq.get(picUrl, headers = {
                "Referer": curUrl,
                "Cookie": ";".join([x["name"] + "=" + x["value"] for x in browser.get_cookies()[-2:]]),
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
                "Host": "p1.manhuacat.com"
            }).content
            f.write(cont)

        time.sleep(random.choice([2, 3, 4, 5]))

browser.quit()
