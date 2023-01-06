## 信息

网页标题 `dealing evil`, 一张图片

看上去还是图片处理

但是怎么处理？

## 网上思路

居然不是处理图片。下载到的图片是evil1.jpg，尝试改url为evil2.jpg，得到

得到新的图片，图片上说：not.jpg -.gfx

改后缀为evil2.gfx，下载得到一个文件。

改后缀为evil3.jpg，得到图片，显示没有evil了。也就是不必要在修改了。

所以是处理文件。

按照二进制读入可以读入文件。但是读入后发现，找不到对应的编码方式。遂上网寻求帮助。

发现：图片中将扑克分成5分，按照分扑克的方法，将文件分成五份，每一份存成jpg，得到5张图。

5张图共同组成了一个字符：`disproportional`

即为答案

http://www.pythonchallenge.com/pc/return/disproportional.html

## 二进制文本

with open('file', 'wb'/'rb') as f:

注意格式一定有b

## 官方解释

http://www.pythonchallenge.com/pcc/return/disproportional.html

