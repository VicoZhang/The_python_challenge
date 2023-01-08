## 信息

曲奇图片，以及之前level_05关的图片，网页名`eat?`

显然不是吃。

## 尝试

曲奇，cookie，既是吃的，也是网页的cookie

查看第level_05的cookie，发现了

`info=you should have followed busynothing...`

也就是说把level05中的
`http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}`
改成`http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}`

直接拿来用！

```
import requests

s = '12345'
for i in range(400):
    url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(s)
    res = requests.get(url).text
    s = res.split(' ')[-1]
    print(s)
```

发现在第119次左右出现一个it

```
96070
83051
it.
55274
93397
```

看一下具体内容：http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=83051

`that's it.`

emmmm

重新看一下cookie

```
_ga=GA1.2.1708359815.1661165284; wikiticket2=vIgbC0i+d/bdsMNPol89ffiC; info=you should have followed busynothing...
```

看一下网上的解释

## 网上

要用request库来获取每个页面的cookie.果然，每个页面的cookie是一个字符

将这些字符合起来

```
import requests

s = '12345'
coos = ''

for i in range(130):
    url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(s)
    res = requests.get(url)
    s = res.text.split(' ')[-1]
    coo = res.cookies
    if not s.isnumeric():
        break
    coos += coo.values()[0]

print(coos)
```

得到：

``BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90``

BZh91AY! bz2

然而decompress显示报错：`Invalid data stream`

网上一种解释：https://blog.csdn.net/Wjf7496/article/details/109813106

需要转换

```
string = coos
new_string = string.replace('+', ' ')
new_strings = prs.unquote_to_bytes(new_string)
text = bz2.decompress(new_strings)
print(text.decode())
```

得到：`is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.`

这是莫扎特那一关！至于打电话，是level_14...

莫扎特他爹是谁？查网 Leopold Mozart

```
with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as pb:
    print(pb.phone('Leopold'))
```

得到：`555-VIOLIN`

violin !

得到`no! i mean yes! but ../stuff/violin.php.`

改成 http://www.pythonchallenge.com/pc//stuff/violin.php

得到一张图片：据说这是Leopold，标题是`it's me. what do you want?`

按照上面的意思，是`inform him that "the flowers are on their way`

怎么通知？

网上说是用cookie

```
headers = {'Cookie': 'info=the flowers are on their way'}
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
```

得到`oh well, don't you dare to forget the balloons`

balloons ):

## 官方

http://www.pythonchallenge.com/pcc/return/balloons.html