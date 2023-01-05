## 信息

网页标题：`odd even`

这张图片看上去很奇怪，发现它每隔一个像素都是黑色的。把像素隔一个拆分开

## 初步尝试

```
with Image.open('cave.jpg') as img:
    m, n = img.size
    img_data = np.asarray(img)
    img_redata = np.asarray(img).reshape(m*n, 3)
    img_odd = img_redata[0::2, :]
    img_even = img_redata[1::2, :]
```
发现似乎行不通？但是不应该的呀

## 换思路

把奇偶分开，按照网上的思路，是把坐标都为奇数和坐标都为偶数的坐标分开？

但是分开之后，发现两幅图片是一样的，和网上很多结果是不同。区别在于怎样衡量所谓的奇偶。

尽管如此，先得出结果，看一下官方的解释。

```
from PIL import Image


with Image.open('cave.jpg') as img:
    m, n = img.size
    odd_img = Image.new('RGB', (m//2, n//2))
    even_img = Image.new('RGB', (m//2, n//2))
    for x in range(m//2):
        for y in range(n//2):
            odd_img.putpixel((x, y), img.getpixel((2*x+1, 2*y+1)))
            even_img.putpixel((x, y), img.getpixel((2*x, 2*y)))
    odd_img.show()
    even_img.show()
```

得到一副有evil的图像

## Image的一些方法

Image.new(mode=, size=) 生成一个新的图片对象，给定mode('RGB')及尺寸。

ImageObject.putpixel((x, y), value) 将value的像素数值（rgb）赋给ImageObject的xy位置处像素

ImageObject.getpixel((x, y)) 获取ImageObject的xy处的像素数值。

## 官方解释

http://www.pythonchallenge.com/pcc/return/evil.html

官方的解释是需要四张图片？？？