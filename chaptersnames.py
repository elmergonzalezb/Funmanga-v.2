import sqlite3
from bs4 import BeautifulSoup as soup
from requests import request

conn = sqlite3.connect("fun_slugid.db")
c = conn.cursor()

c.execute("SELECT manga_slug FROM funmanga")
allmanga = c.fetchall()

c.close()
conn.close()

conn = sqlite3.connect("fun_chapternames.db")
c = conn.cursor()


for manga_slug in allmanga:
    req = request("GET", "http://www.funmanga.com/" + manga_slug[0])

    resp = req.text

    html_soup = soup(resp, "lxml")

    ul = html_soup.find("ul", {"class":"chapter-list"})

    lis = ul.findAll("li")

    for li in lis:
        chapter_link = li.a["href"]
        chapter_link = "/".join(chapter_link.split("/")[3:])
        
        c.execute("SELECT * FROM funmanga WHERE fun_chapter_link = ?", [chapter_link])
        results = c.fetchone()
        
        if results != None and results != []:
            print(results,"results")
        else:
            chapter_no = chapter_link.split("/")[1]
            chapter_name = li.a.span.text.strip()

            c.execute("INSERT INTO funmanga (chapter_name, fun_chapter_link, manga_slug, chapter_no) VALUES (?,?,?,?)", (chapter_name, chapter_link, manga_slug[0], chapter_no))
            print("inserted", manga_slug[0], chapter_no, chapter_name, chapter_link)
    conn.commit()

c.close()
conn.close()