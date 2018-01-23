import urllib.request
url = "http://www.pbc.gov.cn/"
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
html = getHtml(url)
def getIdex(html):
    rul = r''