
def make(url):
    return url if url[:7] == 'http://' else "http://" + url
