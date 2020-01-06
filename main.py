# -*- coding: utf-8 -*-

import mhkcParser as ps
import os
import multiprocessing as mp
import json
import requests as rq
import time
import random
import progressbar

url = "http://mh12306.com/comic/5d4e8479019c1c5461c704bd.html"
foldpref = "./test/"

class dlManga(object):
    def __init__(self, fold, opt):
        self.session = rq.session()
        self.fold = fold
        self.opt = opt
    def __call__(self, dic):
        getFile = rq.get(dic['URL'], headers=self.opt).content
        with open(self.fold+dic["Name"]+".jpg","wb") as f:
            f.write(getFile)

with open("./config.json","r") as f:
    conf = json.load(f)

chapList = ps.getChapterList(url)
totNum = len(chapList)
for ind in progressbar.progressbar(range(0, 3)):
    chap = chapList[ind]
    chapPath = foldpref+chap["Text"]+"/"
    try:
        os.mkdir(foldpref+chap["Text"])
    except FileExistsError:
        pass
    dlDic, addOption = ps.getDlSetting(chap["URL"])
    headerOption = {"User-Agent": conf["User-Agent"]}
    headerOption.update(addOption)
    with mp.Pool(processes=4) as pool:
        pool.map(dlManga(chapPath, headerOption), dlDic)
    time.sleep(0.5+random.random() * 0.5)

if __name__=="__main__":
    pass
