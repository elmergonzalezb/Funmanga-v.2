
#   TODO:
#   Store the (manga_id, chapter_no, image_url) in fun_imagelinks.db file
#   And (manga_name, manga_id) in fun_nameid.db


#   TODO:
#   Store (manga_id, status(completed or not)) in fun_ongoingstate.db
#   and (manga_id, genre_array, artist, type) in details 
#   eg: http://www.funmanga.com/service/manga_info/amai_yuuwaku_ootsuki_miu
#   There is a data-service attribute in every link and you can scrape them
#   Implement a search too

#   TODO:
#   Try encrypting everything


#   TODO:
#   Try cloudinary api and upload everything to the cloudinary servers 

from bs4 import BeautifulSoup as soup
from requests import request
import re 
import json

manga_name = "Gintama"

for i in range(684):
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
        