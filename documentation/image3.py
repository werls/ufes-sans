from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

import subprocess
import argparse

WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 1024, 96, 1

FONTS = [
    "fonts/variable/UfesSans-Roman[wght].ttf",
    "fonts/variable/UfesSans-Italic[wght].ttf",
    ]

WEIGHTS = {
        "100": "Thin",
        "200": "ExtraLight",
        "300": "Light",
        "400": "Regular",
        "500": "Medium",
        "600": "SemiBold",
        "700": "Bold",
        "800": "ExtraBold",
    }

LETTER = "a"

parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(1)
    rect(0, 0, WIDTH, HEIGHT)

def draw_main_text():
    fill(28 / 255, 47 / 255, 255 / 255)
    stroke(None)

    cols = len(WEIGHTS)
    rows = len(FONTS)
    
    for col in range(cols):
        for row in range(rows):
            font(FONTS[1 - row])

            x = MARGIN + (col * (WIDTH - (MARGIN * 2)) / cols)
            y = MARGIN + (row * (HEIGHT - (MARGIN * 2)) / rows)
            fontSize(HEIGHT / 3)
            weight_keys = list(WEIGHTS.keys())
            variation_value = int(weight_keys[col])
            fontVariations(wght=variation_value)
            text(LETTER, (x + ((WIDTH - (MARGIN * 2)) / 16), y + ((HEIGHT - (MARGIN * 2)) / 4)), align="center")

            fontSize(40)
            VARIATION_WEIGHT = WEIGHTS.get(str(int(variation_value)), "Unknown") 
            text('Ufes Sans', (x + ((WIDTH - (MARGIN * 2)) / 16), y + ((HEIGHT - (MARGIN * 2)) / 4) - 96), align="center")

            text(VARIATION_WEIGHT, (x + ((WIDTH - (MARGIN * 2)) / 16), y + ((HEIGHT - (MARGIN * 2)) / 4) - 144), align="center")


if __name__ == "__main__":
    draw_background()
    draw_main_text()
    saveImage(args.output)
    print("DrawBot: Done")
