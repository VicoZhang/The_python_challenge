import pickle
from urllib import request

url = r'http://www.pythonchallenge.com/pc/def/banner.p'

with request.urlopen(url) as f:
    obj = pickle.load(f)

for line in obj:
    for colum in line:
        print(colum[0]*colum[1], end='')
    print()


