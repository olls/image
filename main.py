from PIL import Image
import random as rand
from math import *


SIZE = 512

MAX_R = (0.5 * sqrt(2) * SIZE)


fib = lambda n: ((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5))

flatten = lambda x, f1=128, f2=None: int( (f1 if f2 is None else f2) * int(x * (1.0 / f1)) )

radfade = lambda cx, cy, x, y: int(256 * car_pol(cx - x, cy - y)[0] / MAX_R)
circle = lambda cx, cy, x, y, r=128: flatten(radfade(cx, cy, x, y), r)

car_pol = lambda x, y: (sqrt((x**2) + (y**2)), atan2(y, x)) # returns r, theta
pol_car = lambda r, theta: (r * cos(theta), r * sin(theta)) # returns x, y


def spiral(cx, cy, x, y, off, spr, fade=None):
    r, theta = car_pol(cx - x, cy - y)
    return int( sin((spr*r) + (theta+off)) * 128 ) + 128


red = lambda x, y: int(sum((
    circle(SIZE*.5, SIZE*.5, x, y),
    circle(SIZE*.2, SIZE*.2, x, y),
    circle(SIZE*.2, SIZE*.8, x, y),
    circle(SIZE*.8, SIZE*.2, x, y),
    circle(SIZE*.8, SIZE*.8, x, y)
)) * .2)

green = lambda x, y: int(
    blue(x, y)
    and
    sum((
        flatten(spiral(SIZE*.25, SIZE*.25, x, y, 0, 3.0/12)),
        flatten(spiral(SIZE*.25, SIZE*.75, x, y, 0, 3.0/12)),
        flatten(spiral(SIZE*.75, SIZE*.25, x, y, 0, 3.0/12)),
        flatten(spiral(SIZE*.75, SIZE*.75, x, y, 0, 3.0/12)),
    )) * .25
)

blue = lambda x, y: flatten(spiral(SIZE*.5, SIZE*.5, x, y, 0, 3.0/12))


def main():
    img = Image.new('RGB', (SIZE, SIZE))
    pixels = img.load()

    for y in range(SIZE):
        for x in range(SIZE):
            pixels[x, y] = (
                red(x, y),
                green(x, y),
                blue(x, y)
            )

    img.save('img.png')


if __name__ == '__main__':
    main()
