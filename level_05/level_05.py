# from urllib import request
import requests

s = '12345'
for i in range(400):
    url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(s)
    # res = request.urlopen(url).read().decode()
    res = requests.get(url).text
    s = res.split(' ')[-1]
    break
