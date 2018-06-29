# -*- coding: utf-8 -*-
'''生成字母验证码图片'''
from PIL import ImageFilter,Image,ImageDraw,ImageFont
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65,90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

size = (60 * 4,60)
image = Image.new('RGB',size,(255,255,255))

font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',36)
draw = ImageDraw.Draw(image)

for x in range(size[0]):
    for y in range(size[1]):
        draw.point((x,y),fill =rndColor())

for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('Code.jpg','jpeg')