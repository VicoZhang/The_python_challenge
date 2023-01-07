## 信息

网页标题，`whom`

源码中`<!-- todo: buy flowers for tomorrow -->`

`<!-- he ain't the youngest, he is the second -->`

这一关略显变态。

## 做法

首先，在图片右下角，明显是1月前后的日历，发现2月有29天，即为闰年。

然后，日历标头上年份那里像是被遮盖了，但是是1开头6结尾，及1006至1996年之间某个以6结尾的年份。

其次，1月1日是周四。

最后，buy flowers for tomorrow，说明某一个满足“然后”内年份条件的1月27日发生一件事情。

找这是哪一年：

```
from datetime import datetime

for year in range(1006, 1996 + 1, 10):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        week = datetime.strptime("{}0101".format(year), "%Y%m%d").weekday()
        print(year, end=' ') if week == 3 else ...
```

得到：``1176 1356 1576 1756 1976  ``

按照第二年轻的，1756

查1756年1月27日发生了什么

https://baike.baidu.com/item/%E6%B2%83%E5%B0%94%E5%A4%AB%E5%86%88%C2%B7%E9%98%BF%E7%8E%9B%E5%A4%9A%E4%BC%8A%E6%96%AF%C2%B7%E8%8E%AB%E6%89%8E%E7%89%B9/6129936

答案是莫扎特出生了，所以结果是 Mozart

m要小写

## 知识点

判断闰年：能够被400整除，或者能够被4整除但不能被100整除

`if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):`

datetime.strptime()  将日期转换成datatime对象，类似于编码，编码对象是第一个参数，编码方案是第二个参数。

datatime对象.weekday()返回周几，`Return day of the week, where Monday == 0 ... Sunday == 6`

## 官方

http://www.pythonchallenge.com/pcc/return/mozart.html