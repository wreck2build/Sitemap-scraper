from fileinput import close
from itertools import count
import requests
url =print(input('please type your sitemap url'))
page = requests.get(url)

import re
blog_urls = re.findall(r"https:[\w/\-?=%.]+\.[\w/\-&?=%.]+", page.text)

from bs4 import BeautifulSoup
h1_list = []
count = 0
for blog_url in blog_urls:
    html_content = requests.get(blog_url).content
    pretty_html = BeautifulSoup(html_content, "html.parser")
    h1 = pretty_html.find('h1')
    h1_list.append(h1)

pure_h1_list = []
for raw_h1 in h1_list:
    raw_h1 = str(raw_h1)
    h1_tag_start = raw_h1.find('>')
    raw_h1 = raw_h1[1 + h1_tag_start:]
    h1_tag_end = raw_h1.find('<')
    pure_h1 = raw_h1[:h1_tag_end]
    pure_h1_list.append(pure_h1)
    

import csv

import io
file = open('E:\Matin\python_exc\my-scraper-3.csv' , 'w', encoding="utf-8")
writer = csv.writer(file)

for pure_h1 in pure_h1_list:
    file.write(pure_h1)
    file.write('\n')
file.close()