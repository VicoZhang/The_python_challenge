from PIL import Image


with Image.open('./wire.png') as img:
    new_img = Image.new('RGB', (100, 100))
    num = 0
    x = y = k = 0
    while num < 100*100:
        for x in range(k, 100-k):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        for y in range(k, 99-k):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        for x in range(99-k, k, -1):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        for y in range(98-k, k, -1):
            new_img.putpixel((x, y), img.getpixel((num, 0)))
            num += 1
        k += 1
    new_img.show()
