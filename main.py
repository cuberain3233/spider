import requests,os,re
#此处为文章页链接：
url = 'http://m.77dushu.com/book/102743/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
}
html = requests.get(url)
html.encoding  = 'utf-8'
#找出页标题
title = re.search("(<title>).*(</title>)",html.text).group()
title = title.replace('<title>','').replace('</title>','') + ".html"
print (title)
#生成文章页：
cont = open(title,"w",encoding='utf-8')
cont.write(html.text)
cont.close()






