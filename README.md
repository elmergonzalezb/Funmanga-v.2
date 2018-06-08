# Funmanga dowloader In python

## TODO1

> The purpose
> Clone [http://www.funmanga.com](http://www.funmanga.com)

## TODO2

> Store the (manga_id, chapter_no, image_url) in fun_imagelinks.db file
> And (manga_slug, manga_id) in fun_slugid.db

## TODO3

> Store (manga_id, genre_array, artist, type, manga_image, status(completed or not)) in fun_details.db
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

---

## Databases

|    Database         | Table Name | Contents                                                                               |
|---------------------|:----------:|---------------------------------------------------------------------------------------:|
| fun_imagelinks.db   | funmanga   | manga_id, chapter_no, image_url                                                        |
| fun_slugid.db       | funmanga   | manga_slug, manga_id                                                                   |
| fun_details.db      | funmanga   | manga_id, manga_name, genre_array, artist, type, manga_image, status(completed or not) |

---

| Property    | Type |
|-------------|:----:|
| manga_id    | INT  |
| chapter_no  | INT  |
| image_url   | TEXT |
| manga_slug  | TEXT |
| manga_name  | TEXT |
| status      | BIT  |
| genre_array | TEXT |
| artist      | TEXT |
| type        | TEXT |
| manga_image | TEXT |

---

**status:**
> 1 -> Completed
> 0 -> Ongoing

## Files

### Database Files

**fun_imagelinks.db:**
> Store the (manga_id, chapter_no, image_url) in fun_imagelinks.db file

**fun_slugid.db:**
> And (manga_slug, manga_id) in fun_slugid.db

**fun_details.db:**
> Store (manga_id, genre_array, artist, type, manga_image, status(completed or not)) in fun_details.db

### Python Files

**databasegen.py:**
> Generates the skelital database files and tables for sqlite3 as of (2018 May)

**allmanga.py:**
> Gets all manga links form the manga-list url and saves the manga-slugs
