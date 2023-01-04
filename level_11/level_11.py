from itertools import groupby

arr_0 = '1'

for _ in range(31):
    print(len(arr_0))
    arr = ''
    for key, group in groupby(arr_0):
        arr += str(len(list(group)))+str(key)
    arr_0 = arr

