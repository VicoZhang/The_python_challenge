## 已知信息

recognize the characters. maybe they are in the book,but MAYBE they are in the page source.

打开页面源码，找到

```html
<!--
find rare characters in the mess below:
-->
```

具体内容太多，在文档page_source.txt中

???

找到最少的字符，那就是先对这些字符做一个文本统计。

## 初步
```
with open('page_source.txt') as f:
    txt = f.readlines()
    arr = ''
    num = {}
    for item in txt:
        arr += item.replace("\n", '')
    for s in arr:
        num[s] = arr.count(s)
    print(num)
```

先把读进来的文档转成一块字符，然后用`count()`方法输出每种字符的出现次数

```
{'%': 6104, '$': 6046, '@': 6157, '_': 6112, '^': 6030, '#': 6115, ')': 6186, '&': 6043, '!': 6079, '+': 6066, ']': 6152, '*': 6034, '}': 6105, '[': 6108, '(': 6154, '{': 6046, 'e': 1, 'q': 1, 'u': 1, 'a': 1, 'l': 1, 'i': 1, 't': 1, 'y': 1}
```

显然，最少的是 equality，因此答案应该就是这个

## 总结

有采用更简单的方法，使用collections的Counter方法，果然运行起来快很多

Counter的使用：Counter实现简单高效的计数。

或在另一篇文章中写出。[见此](https://www.cnblogs.com/VicoZhang/p/17008342.html)

采用Counter，可以这样写程序

```
arr = '一堆字符'
print(Counter(arr).most_common())
```
得到同样结果，如此优雅~

## 官方解法

http://wiki.pythonchallenge.com/level2
