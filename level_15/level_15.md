## 信息

一个面包图片，网页标题`walk around`, 还有一个看不清的图片，以及源码中
`<!-- remember: 100*100 = (100+99+99+98) + (...  -->`

还有一个100*100的wire的图片

## 初步尝试

突破口在wire中，面包的旋向可能是一种方向的指示

100*100 = (100+99+99+98) + (...

意思是100分组求和？同时wire打开后是一个一维图像。

100 + 99 + 99 + 98 正好是一圈！

按照这个规律来给图像赋值！

他人的程序：

```
from PIL import Image


with Image.open('./wire.png') as img:
    new_img = Image.new('RGB', (100, 100))
    num = 0
    x = y = k = 0
    while num < 100*100:
        for x in range(k, 100-k):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        for y in range(k, 99-k):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        for x in range(99-k, k, -1):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        for y in range(98-k, k, -1):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        k += 1
    new_img.show()

```

这样子似乎有一些问题，但是能够得出最后的结论。是一张cat的图片。

得到：`and its name is uzi. you'll hear from him later.`

最终答案是uzi

## 官方解释

http://www.pythonchallenge.com/pcc/return/uzi.html

## 备注

这一关的编程很具有技巧性，需要认真看一下。

