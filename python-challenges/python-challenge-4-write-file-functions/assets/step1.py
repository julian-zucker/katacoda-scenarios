import urllib.request as req

def fetch_url(url, file_name):
    file_in = req.urlopen(url)
    data = file_in.read()
    file_out = open(file_name, mode='wb')
    # Add a line here to write the data from the url to the file!

    file_out.close()
