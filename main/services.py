from .models import Circle
from PIL import Image, ImageDraw

# создает небольшую рамку около схемы длиной FRAME / 2
FRAME = 100


def paint():
    circles = Circle.objects.all()
    is_first = True
    maxx = minx = 0
    maxy = miny = 0
    for circle in circles:
        if is_first:
            maxx = circle.x + circle.r
            maxy = circle.y + circle.r
            minx = circle.x - circle.r
            miny = circle.y - circle.r
            is_first = False
        else:
            # нахождение левого верхнего и правого нижнего угла схемы
            maxx = max(maxx, circle.x + circle.r)
            maxy = max(maxy, circle.y + circle.r)
            minx = min(minx, circle.x - circle.r)
            miny = min(miny, circle.y - circle.r)
    # создание изображения
    lenx = int(maxx - minx)
    leny = int(maxy - miny)
    image = Image.new("RGB", (lenx + FRAME, leny + FRAME), (0, 0, 255))
    draw = ImageDraw.Draw(image)
    # отрисовка изображения
    for circle in circles:
        x = circle.x
        y = circle.y
        r = circle.r
        draw.ellipse((x - r - minx + FRAME / 2,  maxy - (y + r) + FRAME / 2, x + r - minx + FRAME / 2,  maxy - (y - r) + FRAME / 2), fill="white")
    # сохраняем статический файл, который будем выводить пользователям
    del draw
    image.save("main/static/main/circles.png", "PNG")
    return


def clear():
    # создаем небольшую картинку, для отобрадения на сайте
    # можно сделать прозрачной, для более удобного отображения
    # и удаляем все элементы, считая что ввод завершен
    circles = Circle.objects.all().delete()
    image = Image.new("RGB", (100,100), (255, 255, 255))
    image.save("main/static/main/circles.png", "PNG")
    return