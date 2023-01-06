with open('evil2.gfx', 'rb') as f:
    content = f.read()
    for i in range(5):
        with open('result_{}.jpg'.format(i), 'wb') as img:
            img.write(content[i::5])

