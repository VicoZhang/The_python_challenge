## 已知信息

三组对应关系，k->m, o->q, e->g，并且给出了一串字符

## 对应语法

ord() 返回字符的ASCII码

chr() 返回ASCII码对应的字符

所以找到字符背后ASCII码的对应关系，做一个翻译即可。

```
print(ord('k')-ord('m'))
print(ord('o')-ord('q'))
print(ord('e')-ord('g'))
```

返回结果都是-2

注意一个小细节：y+2=a, z+2=b, a+2=c, 需要自洽

```
for s in ss:
    if ord('a') <= ord(s) <= ord('z'):
        temp = ord(s)+2
        if temp > ord('z'):
            temp -= 26
        print(chr(temp), end='')
    else:
        print(s, end='')
```

## 结果
``
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why 
this text is so long. using string.maketrans() is recommended. now apply on the url
``
## 官方做法
在python3中，string.maketrans()已被取代，变成str.maketrans(intab, outtab)

Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

最终


**这个代码写的很漂亮！**
```
trantab = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print(ss.translate(trantab))
```

url 的翻译结果是 ocr

