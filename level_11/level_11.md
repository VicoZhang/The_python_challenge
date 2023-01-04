## 信息

`len(a[30]) = ?`

点击图片，是

`a = [1, 11, 21, 1211, 111221, `

看上去a是一个有规律的数组，找到第30个元素即可。

## 规律

第一个数是一个1，所以第二个数是11（1个1）

第二个数是两个1，所以第三个数是21（2个1）

第三个数是一个2和一个1，所以第四个数是1211（1个2，1个1）

第四个数是1个1，1个2，2个1，所以第五个数是111221…………

## 方法

采用itertools.groupby()方法！

```
from itertools import groupby

arr_0 = '1'

for _ in range(31):
    print(len(arr_0))
    arr = ''
    for key, group in groupby(arr_0):
        arr += str(len(list(group)))+str(key)
    arr_0 = arr
```

https://www.geeksforgeeks.org/itertools-groupby-in-python/

itertools.groupby(iterable, key_func)方法将iterable对象按照key_func
方法进行分类，缺省时以相邻且相同元素分类返回。

例如：

```
arr = '121122'
for key, group in groupby(arr):
    print(key, list(group))
```
的输出结果是：
```
1 ['1']
2 ['2']
1 ['1', '1']
2 ['2', '2']
```

这样，将其进行计数和字符拼接即可！

得到a的第31个元素长度为5808，答案为5808
http://www.pythonchallenge.com/pc/return/5808.html

## 官方
http://www.pythonchallenge.com/pcc/return/5808.html