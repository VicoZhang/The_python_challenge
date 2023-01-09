## 信息

网页标题`can you tell the difference?`

一张图片

`<!-- it is more obvious that what you might think -->`

很明显，两边的亮度不一致。

## 初步尝试

试一下brightness

得到一样的网页内容，再看源码：`<!-- maybe consider deltas.gz -->`

得到一个文件。

gz是gzip文件，这是一种压缩文件，https://baike.baidu.com/item/gzip/4487553

在python中可以用gzip库读取该文件。

https://docs.python.org/zh-cn/3/library/gzip.html

读入后，发现文件在中间有明显空格，分成左右两部分，所以是要比较这两部分内容。

先把内容分开

```
import gzip

left_data = []
right_data = []
with gzip.open('deltas.gz') as f:
    for line in f.readlines():
        left_data.append(line.decode()[:53]+'\n')
        right_data.append(line.decode()[56:])
```

再进行比较，需要用到difflib
https://docs.python.org/zh-cn/3/library/difflib.html

生成一个Differ实例differ，用compare方法比较。

```
differ = Differ()
res = differ.compare(left_data, right_data)
```
比较的结果如下：

| 符号  | 含义     |
|-----|--------|
| '-' | 第一个序列有 |
| '+' | 第二个序列有 |
| ' ' | 两个序列都有 |
| '?' | 两个序列都无 |

按照网上的意思，将左边有的、右边有的和左右都有的分别放到三个文件里，每个文件保存成png
写入时转换成字节写入

```
    for line in res:
        bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])  # 如果这一行有数字，按照16进制编码并转成字节
        if line[0] == '+':
            file1.write(bs)
        elif line[0] == '-':
            file2.write(bs)
        else:
            file.write(bs)
```

int(a, 16) 将a变成16进制

bytes(a) 将字符串a变成b''，即字节

这里不转成字节是可以的吗？经过尝试，不可以。因为图片里读入的字符都是b''，不是''，所以写入时也要用
bytes转成b''

这样，得到三张图片，第一张内有：`../hex/bin.html`

第二张 `butter`

第三张 `fly`

依次是下一关、账户、密码

## 官方

http://wiki.pythonchallenge.com/level18
