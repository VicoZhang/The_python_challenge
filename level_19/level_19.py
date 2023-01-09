import gzip
from difflib import Differ

left_data = []
right_data = []
file = open("file.png", "wb")
file1 = open("file1.png", "wb")
file2 = open("file2.png", "wb")

with gzip.open('deltas.gz') as f:
    for line in f.readlines():
        left_data.append(line.decode()[:53]+'\n')
        right_data.append(line.decode()[56:])
    differ = Differ()
    res = differ.compare(left_data, right_data)
    for line in res:
        bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])  # 如果这一行有数字，按照16进制编码并转成字节
        if line[0] == '+':
            file1.write(bs)
        elif line[0] == '-':
            file2.write(bs)
        else:
            file.write(bs)


