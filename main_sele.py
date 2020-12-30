import mhcParser as ps
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import re
import requests

firefoxOpts = Options()
firefoxOpts.add_argument("-headless")

browser = webdriver.Firefox(executable_path="./driver/geckodriver", options=firefoxOpts)



browser.close()