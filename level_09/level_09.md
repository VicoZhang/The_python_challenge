## 信息

一张图片

`Where is the missing link?`

点击图片会要求登录？

查看源码，发现两端文字：

`<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->`

这个看上去像是用户名和密码, un，pw就是username和password的缩写

还有一个放在文件里。是一堆数字。（后来发现，这一堆数字对应蜜蜂的形状，用来生成点击进入登陆界面
的窗口）

## 账户和密码

最初的印象，这是一串数码，尝试用decode解码，发现得到的还是乱码

``print(un.encode('utf-8').decode())``

后来了解，BZh91AY&SY是bz2模块进行加密的标志…………

## bz2

https://docs.python.org/zh-cn/3/library/bz2.html

因此，结果是

```
import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un).decode())
print(bz2.decompress(pw).decode())
```

``huge
file``

直接通关。http://www.pythonchallenge.com/pc/return/good.html

## 官方

http://www.pythonchallenge.com/pcc/return/good.html:huge:file
http://wiki.pythonchallenge.com/level8 

## 记录

这里的知识需要补足