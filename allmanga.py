from bs4 import BeautifulSoup as soup
from requests import request
from string import ascii_lowercase


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
        if li.span is not None:
            print("completed")
        else:
            print("ongoing")
        print(li.a["href"].split("/")[-1])
