#!/usr/local/bin/python3
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageChops, ImageFilter, ImageColor
import requests
from io import BytesIO
import numpy as np
import os


class ProfilImage():
    __coords = {
        'profilPicture': {'x': 186, 'y': 35},
        'name': {'x': 186, 'y': 155},
        'userName': {'x': 190, 'y': 195},
        'level': {'x': 250, 'y': 224},
        'badge': {'x': 150, 'y': 5},
        'levelBar': {'x': 0, 'y': 254}
    }

    def __init__(self,
                 profilPath: str,
                 userName: str,
                 userProfilPicture: str,
                 level: int,
                 xp: int,
                 display_name: str,
                 coords: dict = __coords,
                 badge: dict = [],
                 background: str = "",
                 textColor: str = "#0000FF",
                 barColor: str = "#ADFF2F"
                 ):

        img = Image.open(background).convert('RGBA').resize((500, 281))

        _textColor = ImageColor.getcolor(str(textColor), "RGBA")
        _barColor = ImageColor.getcolor(str(barColor), "RGBA")

        # image
        response = requests.get(userProfilPicture)
        pic = Image.open(BytesIO(response.content)).convert(
            'RGBA').resize((128, 128))

        h, w = pic.size

        pic = self.__crop_max_square(pic).resize((w, h), Image.LANCZOS)
        pic = self.__mask_circle_transparent(pic, 1)

        img.paste(pic, (coords["profilPicture"]['x'],
                  coords["profilPicture"]['y']), pic)

        # text
        d = ImageDraw.Draw(img)

        # name
        d.multiline_text((coords["name"]['x'], coords["name"]['y']), display_name, font=ImageFont.truetype(
            "data/font/ancientMedium.ttf", 45), fill=_textColor)

        d.multiline_text((coords["userName"]['x'], coords["userName"]['y']), userName, font=ImageFont.truetype(
            "data/font/LiberationSans-Regular.ttf", 20), fill=_textColor)

        # level
        d.multiline_text((coords["level"]['x'], coords["level"]['y']), str(
            level), font=ImageFont.truetype("data/font/LiberationSans-Regular.ttf", 30), fill=_barColor)

        # badge

        badgeNumber = 0
        for i in badge:
            tempImg = Image.open(i).convert('RGBA')
            tempImg.thumbnail((32, 32), Image.ANTIALIAS)
            img.paste(
                tempImg, (coords['badge']['x']+(34*badgeNumber), coords['badge']['y']), tempImg)
            badgeNumber += 1

        # badge

        progress = (xp * 100 / (level * 200))/100

        bar = self.__new_bar(1, 1, 500, 25, progress, fg=_barColor)

        img.paste(bar, (coords['levelBar']['x'], coords['levelBar']['y']), bar)

        img.save(profilPath)

        self.__profilPath = profilPath

    def ProfilPath(self):
        return self.__profilPath

    # Private Methods
    def __crop_center(self, pil_img, crop_width, crop_height):
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    def __crop_max_square(self, pil_img):
        return self.__crop_center(pil_img, min(pil_img.size), min(pil_img.size))

    def __mask_circle_transparent(self, pil_img, blur_radius, offset=0):
        offset = blur_radius * 2 + offset
        mask = Image.new("L", pil_img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse(
            (offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

        result = pil_img.copy()
        result.putalpha(mask)

        return result

    def __new_bar(self, x, y, width, height, progress, bg=(0, 0, 0, 0), fg=(173, 255, 47, 255), fg2=(15, 15, 15, 0)):
        bar = Image.new(mode="RGBA", size=(width+(x*2)*2, height+(y*2)*2))
        draw = ImageDraw.Draw(bar)

        # Draw the background
        draw.rectangle((x+(height/2), y, x+width+(height/2),
                       y+height), fill=fg2, width=10)
        draw.ellipse((x+width, y, x+height+width, y+height), fill=fg2)
        draw.ellipse((x, y, x+height, y+height), fill=fg2)
        width = int(width*progress)

        # Draw the part of the progress bar that is actually filled
        draw.rectangle((x+(height/2), y, x+width+(height/2),
                       y+height), fill=fg, width=10)
        draw.ellipse((x+width, y, x+height+width, y+height), fill=fg)
        draw.ellipse((x, y, x+height, y+height), fill=fg)

        return bar
    # Private Methods
