
from bs4 import BeautifulSoup as soup
from requests import request
import re 
import json

manga_name = "Gintama"

for i in range(684):
    print(i)
    res=request("GET", "http://www.funmanga.com/" + manga_name + "/" + str(i))

    html_resp = res.text

    souped = soup(html_resp, "lxml")

    list_scripts = souped.findAll("script")

    m = re.findall(r'var images = (.*);' , list_scripts[3].string)

    #print(m)
    for a in m:
        #print(a)
        json_obj = json.loads(a)

        for url in json_obj:
            print(url)
        