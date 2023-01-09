## 信息

直接看源码，一堆字符

```
From: leopold.moz@pythonchallenge.com
Subject: what do you mean by "open the attachment?"
Mime-version: 1.0
Content-type: Multipart/mixed; boundary="===============1295515792=="

It is so much easier for you, youngsters.
Maybe my computer is out of order.
I have a real work to do and I must know what's inside!

--===============1295515792==
Content-type: audio/x-wav; name="indian.wav"
Content-transfer-encoding: base64

字符放在文件里


--===============1295515792==--
```

所以应该是按照提示，将字符变成一个wav文件。

## 尝试

文件名：indian.wav

文件类型：audio/x-wav

编码方式：base64 编码工具 https://docs.python.org/zh-cn/3/library/base64.html

工具：wave库 https://docs.python.org/zh-cn/3/library/wave.html

如下：

```
import base64

wave_data = ''
with open('page_source.txt', 'r') as f:
    for line in f.readlines():
        wave_data += str(line.replace('\n', ''))

with open('indian.wav', 'wb') as ff:
    ff.write(base64.b64decode(wave_data))
```

得到一个音频文件，打开后听到“sorry”

？页面显示`- "what are you apologizing for?"`

按照网上的意思，地图中陆地和海洋的颜色相反，所以需要将写入的数据按帧反转。

```
with wave.open('indian.wav', 'rb') as f:
    with wave.open('indian1.wav', 'wb') as ff:
        ff.setparams(f.getparams())
        for i in range(f.getnframes()):
            ff.writeframes(f.readframes(1)[::-1])
```


得到：

`you are an idiot,hahahahaha…………`

输入`idiot`

http://www.pythonchallenge.com/pc//hex/idiot2.html

## 官方

http://www.pythonchallenge.com/pcc/hex/idiot2.html

