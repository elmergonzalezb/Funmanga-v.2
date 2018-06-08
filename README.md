# Funmanga dowloader In python

## TODO1

> The purpose
> Clone [http://www.funmanga.com](http://www.funmanga.com)

## TODO2

> Store the (manga_id, chapter_no, image_url) in fun_imagelinks.db file
> And (manga_name, manga_id) in fun_nameid.db

## TODO3

> Store (manga_id, status(completed or not)) in fun_ongoingstate.db
> and (manga_id, genre_array, artist, type) in fun_details.db
> eg [http://www.funmanga.com/service/manga_info/amai_yuuwaku_ootsuki_miu](http://www.funmanga.com/service/manga_info/amai_yuuwaku_ootsuki_miu)
> There is a data-service attribute in every link and you can scrape them
> Implement a search too

## TODO4

> Try encrypting everything

## TODO5

> Try cloudinary api and upload everything to the cloudinary servers

---

## To Download in python

```python
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

r = requests.get(image_url) # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:

# Saving received content as a png file in
# binary format

# write the contents of the response (r.content)
# to a new file in binary mode.
    f.write(r.content)
```

## Databases

|    Database         | Contents                           |
|---------------------|:----------------------------------:|
| fun_imagelinks.db   | manga_id, chapter_no, image_url    |
| fun_nameid.db       | manga_name, manga_id               |
| fun_ongoingstate.db | manga_id, status(completed or not) |
| fun_details.db      | manga_id, genre_array, artist, type|

| Property    | Type |
|-------------|:----:|
| manga_id    | INT  |
| chapter_no  | INT  |
| image_url   | TEXT |
| manga_name  | TEXT |
| status      | BIT  |
| genre_array | TEXT |
| artist      | TEXT |
| type        | TEXT |