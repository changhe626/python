# -*- coding: utf-8 -*-
import urllib.request
url='http://www.qq.com/'
def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read().decode(encoding='GBK',errors='strict')
    return html
print(getHtml(url))
