from PIL import Image


with Image.open('cave.jpg') as img:
    m, n = img.size
    odd_img = Image.new('RGB', (m//2, n//2))
    even_img = Image.new('RGB', (m//2, n//2))
    for x in range(m//2):
        for y in range(n//2):
            odd_img.putpixel((x, y), img.getpixel((2*x+1, 2*y+1)))
            even_img.putpixel((x, y), img.getpixel((2*x, 2*y)))
    odd_img.show()
    even_img.show()
