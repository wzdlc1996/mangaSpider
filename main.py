# -*- coding: utf-8 -*-

import mhgParser as ps
import os
import multiprocessing as mp
import json
import requests as rq
import time
import random
import progressbar
import urllib.request

proxy = urllib.request.getproxies()

url = "https://www.mhgui.com/comic/21061/"
ext = ""
foldpref = "./test/"

class dlManga(object):
    def __init__(self, fold, opt):
        self.session = rq.session()
        self.fold = fold
        self.opt = opt

    def __call__(self, dic):
        getFile = rq.get(dic['URL'], headers=self.opt, proxies=proxy).content
        with open(self.fold+dic["Name"]+ext, "wb") as f:
            f.write(getFile)


with open("./config.json", "r") as f:
    conf = json.load(f)

chapList = ps.getChapterList(url, proxies=proxy)

totNum = len(chapList)
for ind in progressbar.progressbar(range(totNum)):
    chap = chapList[ind]
    chapPath = foldpref+chap["Text"] + "/"
    try:
        os.mkdir(foldpref+chap["Text"])
    except FileExistsError:
        pass
    dlDic, addOption = ps.getDlSetting(chap["URL"], proxies=proxy)
    headerOption = {"User-Agent": conf["User-Agent"]}
    headerOption.update(addOption)
    # with mp.Pool(processes=4) as pool:
    #     pool.map(dlManga(chapPath, headerOption), dlDic)
    z = dlManga(chapPath, headerOption)
    for x in dlDic:
        try:
            z(x)
        except:
            for _ in range(5):
                try:
                    z(x)
                except:
                    pass
    time.sleep(0.5+random.random() * 0.5)
