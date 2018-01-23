
import urllib.request
import re
url = "https://tieba.baidu.com/index.html"
#爬取网页
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml(url)

# #获取图片地址
def getImg(html):
    rule = r'src="(.*\.jpg|jpeg|png)"'
    rule_compile = re.compile(rule)

    imglist = re.findall(rule_compile,html)
    return imglist

# url = "http://tieba.baidu.com/p/5519425947"
# html = getHtml(url)
#下载图片
x = 0
for i in getImg(html):
    urllib.request.urlretrieve(i,'D:\JPG\%s.jpg' % x)
    x+=1
