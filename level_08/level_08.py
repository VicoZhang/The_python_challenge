from PIL import Image
import numpy as np

with Image.open('./oxygen.png') as img:
    arr = []
    temp = ''
    m, n = img.size
    img_array = np.array(img)
    for px in img_array[n // 2]:
        if px[0] == px[1]:
            if px[0] != temp:
                arr.append(px[0])
                temp = px[0]

for s in arr:
    print(chr(s), end='')

print()
arr2 = [105, 110, 116, 101, 103, 114, 105, 116, 121]
[print(chr(_), end='') for _ in arr2]
