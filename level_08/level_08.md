## 已知信息

一张图片，中有马赛克

网页标题smarty

## 初步尝试

看一下马赛克的rgb值

目测，马赛克在图像最中间的几行，因此输出这些地方的rgb信息值

```
from PIL import Image
import numpy as np

with Image.open('./oxygen.png') as img:
    m, n = img.size
    img_array = np.array(img)
    for px in img_array[n // 2]:
        print(px[0], end=' ')
```

发现除了最后一些像素点外，其他的rgb值都一样，且相邻几个点的rgb值也一样，
那么，是不是这些rgb值是ASCII码？

果真如此，得到：

``smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]``

那么，[105, 10, 16, 101, 103, 14, 105, 16, 121]对应什么呢？

对应：

``egiy``

求助网上，发现是：10显然不是一个字母的ascii，要改成110才能对应上…………

因此修改后的答案是[105, 110, 116, 101, 103, 114, 105, 116, 121]

得到答案：integrity

## 官方

http://www.pythonchallenge.com/pcc/def/integrity.html


## 记录

将图片转成矩阵，用np.array(img)会有警告，该怎样消除？