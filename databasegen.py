import sqlite3

# slug -> id
# fun_slugid.db

conn = sqlite3.connect("fun_slugid.db")
c = conn.cursor()

#Create Table funmanga in fun_slugid.db for the fist time
c.execute("CREATE TABLE IF NOT EXISTS funmanga (manga_slug TEXT, manga_id INT)")
conn.commit()

c.close()
conn.close()

# Details
# fun_details.db

conn = sqlite3.connect("fun_details.db")
c = conn.cursor()

#Create Table funmanga in fun_details.db for the fist time
c.execute("CREATE TABLE IF NOT EXISTS funmanga (manga_slug INT, manga_name TEXT, genre_array TEXT, artist TEXT, type TEXT, manga_image TEXT, status BIT)")
conn.commit()

c.close()
conn.close()

# Image links

conn = sqlite3.connect("fun_imagelinks.db")
c = conn.cursor()

#Create Table funmanga in fun_imagelinks.db for the fist time
c.execute("CREATE TABLE IF NOT EXISTS funmanga (manga_slug INT, chapter_no REAL, image_url TEXT)")
conn.commit()

c.close()
conn.close()

# chapter names and links

conn = sqlite3.connect("fun_chapternames.db")
c = conn.cursor()

#Create Table funmanga in fun_chapternames.db for the fist time
c.execute("CREATE TABLE IF NOT EXISTS funmanga (manga_slug INT, chapter_no REAL, chapter_name TEXT, fun_chapter_link TEXT)")
conn.commit()

c.close()
conn.close()
