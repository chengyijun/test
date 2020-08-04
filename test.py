# -*- coding:utf-8 -*-
import numpy
from PIL import Image


def test():
    image = Image.open('./1.png')
    imarr = numpy.array(image)
    imarr.flags.writeable = True
    print(imarr.shape)


def main():
    test()


if __name__ == '__main__':
    main()
