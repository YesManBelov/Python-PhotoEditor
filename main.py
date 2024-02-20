from PIL import Image, ImageFilter, ImageOps, ImageEnhance

while True:
    print('''
    1 - вывести
    2 - вывести перевернутое на заданное кол-во градусов
    3 - Размытие (доработать)
    4 - Обесцветить
    5 - Негатив
    6 - Сепия (с запросом глубины)
    7 - Каналы
    8 - белый
    9 - псевдо
    
    ''')
    import numpy as np
    import itertools
    image = Image.open('test2.jpg')
    image = Image.open('non_color.jpg')
    # x = list(image.getdata())
    # print(len(x))
    # x = list(itertools.zip_longest(*list(image.getdata())))
    # print(len(x))


    answer = input()
    # image.show()

    from colorsys import hsv_to_rgb
    def pseudocolor(val, minval, maxval):
        """ Convert val in range minval..maxval to the range 0..120 degrees which
            correspond to the colors Red and Green in the HSV colorspace.
        """
        h = (float(val - minval) / (maxval - minval)) * 120

        # Convert hsv color (h,1,1) to its rgb equivalent.
        # Note: hsv_to_rgb() function expects h to be in the range 0..1 not 0..360
        r, g, b = hsv_to_rgb(h / 360, 1., 1.)
        return r, g, b

    if answer == '1':
        image = image.convert('RGB')
        image.show()
        pix = list(itertools.zip_longest(*list(image.getdata())))
        min_r = min(pix[0])
        max_r = max(pix[0])
        min_g = min(pix[1])
        max_g = max(pix[1])
        min_b = min(pix[2])
        max_b = max(pix[2])
        print(min_r, max_r)
        print(min_g, max_g)
        print(min_b, max_b)
        for i in range(0, image.size[0] - 1):
            for j in range(0, image.size[1] - 1):
                r,g,b = image.getpixel((i, j))
                r = (r-min_r)*255//(max_r-min_r)
                g = (g-min_g)*255//(max_g-min_g)
                b = (b-min_b)*255//(max_b-min_b)
                image.putpixel((i, j), (r, g, b))
        image.show()
        # print(min_r, max_b)
        # x = ImageOps.autocontrast(image, 40)
        # x.show()
    elif answer == '2':
        n = int(input('Введите граудсы: '))
        rotated = image.rotate(n)
        rotated.show()

    elif answer == '3':
        x = int(input())
        blurred = image.filter(ImageFilter.GaussianBlur(x))
        blurred.show()

    elif answer == '4':
        b_w = image.convert('L')
        b_w.show()
        b_w.save('non_color.jpg')

    elif answer == '5':
        for i in range(0, image.size[0] - 1):
            for j in range(0, image.size[1] - 1):
                pixel_color = image.getpixel((i, j))
                r = 255 - pixel_color[0]
                g = 255 - pixel_color[1]
                b = 255 - pixel_color[2]
                image.putpixel((i, j), (r, g, b))
        image.show()

    elif answer == '6':
        depth = int(input('Depth: '))
        for i in range(0, image.size[0] - 1):
            for j in range(0, image.size[1] - 1):
                r, g, b = image.getpixel((i, j))
                S = (r + g + b) // 3
                r = S + depth * 2
                g = S + depth
                b = S
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                image.putpixel((i, j), (r, g, b))
        image.show()

    elif answer == '7':
        canal = input('Выберете канал (r/g/b): ')
        if canal == 'r':
            for i in range(0, image.size[0] - 1):
                for j in range(0, image.size[1] - 1):
                    pixel_color = image.getpixel((i, j))
                    r = pixel_color[0]
                    image.putpixel((i, j), (r, 0, 0))
            image.show()
        elif canal == 'g':
            for i in range(0, image.size[0] - 1):
                for j in range(0, image.size[1] - 1):
                    pixel_color = image.getpixel((i, j))
                    g = pixel_color[1]
                    image.putpixel((i, j), (0, g, 0))
            image.show()
        elif canal == 'b':
            for i in range(0, image.size[0] - 1):
                for j in range(0, image.size[1] - 1):
                    pixel_color = image.getpixel((i, j))
                    b = pixel_color[2]
                    image.putpixel((i, j), (0, 0, b))
            image.show()

    elif answer == '8':
        image2 = ImageEnhance.Color(image)
        image2.show()



    elif answer == '9':
        image.show()
        image = image.convert('RGB')
        for i in range(0, image.size[0] - 1):
            for j in range(0, image.size[1] - 1):
                r, g, b = image.getpixel((i, j))
                r, g, b = pseudocolor(r, 0, 100)
                r = int(r*255)
                g = int(g*255)
                b = int(b*255)
                image.putpixel((i, j), (r, g, b))
        image.show()

    elif answer =='10':
        def change_contrast(img, level):
            factor = (259 * (level + 255)) / (255 * (259 - level))

            def contrast(c):
                value = 128 + factor * (c - 128)
                return max(0, min(255, value))

            return img.point(contrast)
        level = int(input())
        x = change_contrast(image, level)
        x.show()

    elif answer == '11':
        def change_contrast(img):

            def contrast(c):
                value = 255 - c
                return value

            return img.point(contrast)


        x = change_contrast(image)
        x.show()


    elif answer.lower() == 'exit':
        exit()
    else:
        print('Command Error\n\n')
    print()
