## 信息
``<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->``

发现点击图片，出现 `and the next nothing is 44827`, 
网站url变成：`http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345`

意思是，访问一次图片，得到一个 nothing, 用其替换url中的nothing, 得到下一个nothing，
依次类推，不超过400次循环可以得到。

访问网址？

urllib may help

## urllib

https://docs.python.org/zh-cn/3/library/urllib.html

urllib 是一个收集了多个涉及 URL 的模块的包

其中的request模块可以提供访问url的接口，只需按照上面的规律得到下一个url，然后交给
urlopen去打开，最后返回的是一个urllib.response对象，这个对象有read()、readline()、readlines()
等方法，有header、url等属性。其read方法返回网站中的内容，用decode将二进制解码，得到内容的字符串。

```
from urllib import request

s = '12345'
for i in range(400):
    url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(s)
    res = request.urlopen(url).read().decode()
    s = res.split(' ')[-1]
    print(res)
```

最后在235行左右得到
peak.html

所有的输出文件在result.pdf中

## 其他做法

> 对于更高级别的 HTTP 客户端接口，建议使用 Requests 

既然如此，试一下Request

```
import requests

s = '12345'
for i in range(400):
    url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(s)
    res = requests.get(url).text
    s = res.split(' ')[-1]
```

大同小异

## 网站答案

http://wiki.pythonchallenge.com/level4
