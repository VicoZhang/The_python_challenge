from collections import Counter

with open('page_source.txt') as f:
    txt = f.readlines()
    arr = ''
    num = {}
    for item in txt:
        arr += item.replace("\n", '')
    # for s in arr:
    #     num[s] = arr.count(s)
    # print(num)
    print(Counter(arr).most_common())

