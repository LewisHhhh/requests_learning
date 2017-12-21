# -*-coding:utf8 -*-
import requests

payload = {'wd':'花'}
# r = requests.get('https://www.baidu.com/s',params = payload)
try:
    
    headers = {'User-Agent': 'alexkh'}#采集时，我们可以用这个方法来伪装请求头部
    
    r = requests.get('https://movie.douban.com/top250',headers = headers,timeout = 5)#通过timeout属性设置超时时间，一旦超过这个时间还没获得响应内容，就会提示错误。，
    print type(r.text)#内容以unicode码输出
    print type(r.content)#内容以字节形式输出
    print r.encoding#获取网站的编码方式
    print r.headers#通过r.headers来获取响应头内容，以字典的形式返回了全部内容
    print r.request.headers#用r.request.headers来获取请求头内容
    
except:
    print 'response is error'



# r2 = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28',allow_redirects = False)
# print r2.status_code
# print r2.json()['data']['country']
