from PIL import Image


def rgb2yuv(rgb):
    yuv = rgb.convert("YCbCr")
    yuv.show()
    return yuv


