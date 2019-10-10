from PIL import ImageGrab, ImageOps
import pyautogui

print(pyautogui.displayMousePosition())

currentGrid = [0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0]


class Coordinates:  # @TODO add all tile coordinates
    cord11 = (300, 420)
    cord12 = (440, 420)
    cord13 = (575, 420)
    cord14 = (715, 420)
    cord21 = (300, 550)
    cord22 = (440, 550)
    cord23 = (575, 550)
    cord24 = (715, 550)
    cord31 = (300, 700)
    cord32 = (440, 700)
    cord33 = (575, 700)
    cord34 = (715, 700)
    cord41 = (300, 820)
    cord42 = (440, 820)
    cord43 = (575, 820)
    cord44 = (715, 820)

    cordArray = [cord11, cord12, cord13, cord14,
                 cord21, cord22, cord23, cord24,
                 cord31, cord32, cord33, cord34,
                 cord41, cord42, cord43, cord44]


class Values:
    empty = 95
    two = 229
    four = 225
    eight = 190
    sixteen = 172
    thirtyTwo = 157
    sixtyFour = 135
    oneTwentyEight = 205
    twoFiftySix = 201
    fiveOneTwo = 197
    oneZeroTwoFour = 193
    twoZeroFourEight = 189

    valueArray = [empty, two, four, eight, sixteen,
                  thirtyTwo, sixtyFour, oneTwentyEight,
                  twoFiftySix, fiveOneTwo, oneZeroTwoFour,
                  twoZeroFourEight]  # similar to cordArray for easier interaction


def get_grid():
    image = ImageGrab.grab()  # get value of every colour on the screen
    gray_image = ImageOps.grayscale(image)  # converts image to greyscale

    # enumerate to keep index to update grid
    for index, cord in enumerate(Coordinates.cordArray):  # get all pixels at once (in grayscale)
        pixel = gray_image.getpixel(cord)  # get the value of a pixel at any coordinate
        pos = Values.valueArray.index(pixel)

