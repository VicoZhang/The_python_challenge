from PIL import Image
import numpy as np

with Image.open('mozart.gif') as img:
    m, n = img.size
    data = np.asarray(img.getdata()).reshape([n, m])
    for i in range(n):
        inx = np.argwhere(data[i] == 195)[0][0]
        data[i] = np.concatenate((data[i][inx:], data[i][:inx]))
    new_img = Image.fromarray(data)
    new_img.save('result.gif', 'gif')

