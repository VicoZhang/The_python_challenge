## 已知

一张图片，拉链，zip？

`<!-- <-- zip -->`

果真

`now there are pairs`

网页标题

所以要解压缩的文件在哪里？尝试把html改成zip，下载得到一个压缩文件

## 尝试

一共解压缩到900多个文件，最后一个是readme

```
welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
```

打开90052.txt 

```Next nothing is 94191```

这和之前的level_05是一样的嘛

发现会报一个FileNotFoundError的错误，加上try

```
file_num = '90052'

while True:
    try:
        with open('./channel/{}.txt'.format(file_num), 'r') as f:
            res = f.read().split(' ')
            file_num = res[-1]
            print(res)
    except FileNotFoundError:
        break
```

在46145文件出现问题，打开文件

``Collect the comments.``

收集评论？

事实是，comment是zip文件的一个属性，用python zipfile可以读取出来。


## zipfile

https://docs.python.org/zh-cn/3/library/zipfile.html#zipfile.ZipInfo.comment

`zipfile.ZipFile(fileName[, mode[, compression[, allowZip64]]])`
返回一个Zipfile对象，可用在with结构里

`zipfile.extractall([path[, member[, password]]])` 解压缩

`Zipfile.namelist()` 返回文件名列表

`ZipFile.open(name[, mode[, password]])` 打开压缩文档中的某个文件

`ZipFile.getinfo(name)` 返回一个ZipInfo对象，name是Zipfile.namelist()中的元素

ZipInfo的属性有：filename, data_time,comment等


## 最终尝试

```
from zipfile import ZipFile

with ZipFile('./channel.zip') as f:
    file_num = '90052'
    while True:
        try:
            with f.open('{}.txt'.format(file_num)) as f1:
                res = f1.read().decode()
                file_num = res.split(' ')[-1]
                print(f.getinfo('{}.txt'.format(file_num)).comment.decode(), end='')
        except FileNotFoundError:
            break
        except KeyError:
            break
```

先用Zipfile对象读取压缩文件，然后读取压缩文件的内容，并且用Zipfile.read()读取内容，按照上面的
意思进行循环，不同的是这次输出的是文件的comment。

实际中，由于Collect the comments.文件内容的存在，会导致：comments..txt文件不存在和
comments..txt文件无comment，所有要用try except跑抛去两种错误。

对于b' '，采用decode解码

## 结果

hockey

输入网站，得到it's in the air. look at the letters.

原来是组成hockey的词，oxygen

最终是oxygen

## 官方

http://wiki.pythonchallenge.com/level6
