import requests , sys , os , webbrowser

link = "http://res.cloudinary.com/testrootworld/image/upload/v1528458999/funmanga/the-gamer/8.jpg"
file_name = "download.jpg"
with open(file_name, "wb") as f:
        print "Downloading %s" % file_name
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
webbrowser.open(file_name)
