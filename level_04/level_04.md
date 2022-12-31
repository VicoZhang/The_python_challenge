## 获取信息

网页标题叫 re，说明要用正则

One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

应该是：三个大写字母+一个小写字母+三个大写字母 的样式

在源码中，又有一段文字，放在 page_source 中

想到的第一种做法就是遍历，按照unicode编码找。

```
arr = ''
with open('./page_source.txt') as f:
    for s in f.readlines():
        arr += s.replace('\n', '')

for s in range(len(arr[:-7])):
    if ord('A') <= ord(arr[s]) <= ord('Z'):
        if ord('A') <= ord(arr[s+1]) <= ord('Z'):
            if ord('A') <= ord(arr[s+2]) <= ord('Z'):
                if ord('a') <= ord(arr[s + 3]) <= ord('z'):
                    if ord('A') <= ord(arr[s + 4]) <= ord('Z'):
                        if ord('A') <= ord(arr[s + 5]) <= ord('Z'):
                            if ord('A') <= ord(arr[s + 6]) <= ord('Z'):
                                print(arr[s:s+7])
```

无脑if判断，找到的结果是有一堆……

发现是题中：EXACTLY 这个词出现了问题！每个小写字母完全被三个大写字母包括。
这就说明，只有AAAaAAA才可以，而上面的循环程序，无法保证AAAAaAAAA的情况被排除。
所以，应该找的是9个字符，aAAAaAAAa，这样才能保证找到的是EXACTLY的情况。

```
for s in range(len(arr[:-9])):
    if ord('a') <= ord(arr[s]) <= ord('z'):
        if ord('A') <= ord(arr[s+1]) <= ord('Z'):
            if ord('A') <= ord(arr[s+2]) <= ord('Z'):
                if ord('A') <= ord(arr[s + 3]) <= ord('Z'):
                    if ord('a') <= ord(arr[s + 4]) <= ord('z'):
                        if ord('A') <= ord(arr[s + 5]) <= ord('Z'):
                            if ord('A') <= ord(arr[s + 6]) <= ord('Z'):
                                if ord('A') <= ord(arr[s + 7]) <= ord('Z'):
                                    if ord('a') <= ord(arr[s + 8]) <= ord('z'):
                                        print(arr[s+4], end='')


```

输出结果是 linkedlist

## 方法升级

显然需要用到正则，循环的方式不合理。

正则：

```
pattern = r'[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]'
result = re.finditer(pattern, arr)
for item in result:
    print(item.group()[4], end='')
```

可见如此简洁。

## 关于re

| 字符     | 意义             |
|--------|----------------|
| .      | 匹配任意字符（不包括换行）  |
| *      | 匹配任意多次         |
| +      | 匹配多次，不包含0次     |
| ？      | 匹配0或1次，采用非贪婪模式 |
| .*?    | 常用             |
| [a-z]  | 匹配小写字母         |
| [^a-z] | 匹配除小写字母外的所有字符  |
更详细内容：

https://www.byhy.net/tut/py/extra/regex/

https://docs.python.org/3/howto/regex.html

## 官方

http://wiki.pythonchallenge.com/level3

