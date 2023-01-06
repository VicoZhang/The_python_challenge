## 信息

`phone that evil`

一张图片，网页标题：`call him`

点击5键，会有一个页面弹出

```
<methodResponse>
<fault>
<value>
<struct>
<member>
<name>faultCode</name>
<value>
<int>105</int>
</value>
</member>
<member>
<name>faultString</name>
<value>
<string>XML error 5: empty document</string>
</value>
</member>
</struct>
</value>
</fault>
</methodResponse>
```

标题是`phonebook.php`， 那就是一个电话簿？

## 这一关有些专业难度

直接查网，过程如下：

```
import xmlrpc.client
with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as pb:
    print(pb.system.listMethods())
    print(pb.system.methodHelp('phone'))
    print(pb.phone('evil'))
```
引入xmlrpc库，打开所谓电话簿。电话铺中的方法列表包括：

`['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']`

发现有一个phone的方法。

用 `methodHelp` 查询phone的使用方法：

`Returns the phone of a person`

因此直接 `phone evil`

结果发现：`He is not the evil` ?

这时，需要回到上一题中，虽然上一题的evil3.jpg说没有evil了，但是evil4.jpg还是存在的。

打开它

```
with open('evil4.jpg') as f:
    de = f.read()
    print(de)
```

发现：`Bert is evil! go back!`

所以最后 `pb.phone('Bert')`

得到结果：`555-ITALY`

输入ITALY，提示是小写，所以最终的结果是：
http://www.pythonchallenge.com/pc/return/italy.html

## 官方解释

http://www.pythonchallenge.com/pcc/return/italy.html

## xmlrpc 库

https://docs.python.org/zh-cn/3/library/xmlrpc.html