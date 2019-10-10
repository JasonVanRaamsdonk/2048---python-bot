from PIL import ImageGrab, ImageOps
import pyautogui

print(pyautogui.displayMousePosition())

currentGrid = [0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0]


class Coordinates:  # @TODO add all tile coordinates
    cord11 = (260, 420)
    cord12 = (400, 420)
    cord13 = (530, 420)
    cord14 = (660, 420)
    cord21 = (260, 550)
    cord22 = (400, 550)
    cord23 = (530, 550)
    cord24 = (660, 550)
    cord31 = (260, 700)
    cord32 = (400, 700)
    cord33 = (530, 700)
    cord34 = (660, 700)
    cord41 = (260, 820)
    cord42 = (400, 820)
    cord43 = (530, 820)
    cord44 = (660, 820)

    cordArray = [cord11, cord12, cord13, cord14,
                 cord21, cord22, cord23, cord24,
                 cord31, cord32, cord33, cord34,
                 cord41, cord42, cord43, cord44]


image = ImageGrab.grab()  # get value of every colour on the screen
grayImage = ImageOps.grayscale(image)  # converts image to greyscale

for cord in Coordinates.cordArray:
    pixel = grayImage.getpixel(cord)  # get the value of a pixel at any coordinate
    print(pixel)
