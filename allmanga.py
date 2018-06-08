from bs4 import BeautifulSoup as soup
from requests import request
from string import ascii_lowercase
import sqlite3

conn = sqlite3.connect("fun_slugid.db")
c = conn.cursor()


for alphabet in (" " + ascii_lowercase):
    #For a-z and ""(for just "http://www.funmanga.com/manga-list/")
    req = request("GET", "http://www.funmanga.com/manga-list/" + alphabet)
    resp = req.text

    html_soup = soup(resp, "lxml")

    uls = html_soup.findAll("ul", {"class":"manga-list"})

    left_col = uls[0]
    right_col = uls[1]

    lis = left_col.findAll("li")
    lis.extend(right_col.findAll("li"))

    for li in lis:

        completed = 0
        
        if li.span is not None:
            completed = 1
        else:
            pass
       
        manga_slug = li.a["href"].split("/")[-1]
        manga_name = li.a.text
        print(manga_name,completed)

        c.execute("SELECT * FROM funmanga WHERE manga_slug = ?", [manga_slug])
        results = c.fetchone()

        if results != None and results != []:
            print(results)
        else:
            c.execute("INSERT INTO funmanga (manga_slug) VALUES (?)",(manga_slug,))
            print("inserted",manga_slug)
    conn.commit()
        
c.close()
conn.close()