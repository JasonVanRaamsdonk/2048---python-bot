from PIL import ImageGrab, ImageOps
import pyautogui

from coordinates import Coordinates
from values import Values

print(pyautogui.displayMousePosition())

currentGrid = [0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0]

UP = 100
LEFT = 101
DOWN = 102
RIGHT = 103


def get_grid():
    image = ImageGrab.grab()  # get value of every colour on the screen
    gray_image = ImageOps.grayscale(image)  # converts image to greyscale

    # enumerate to keep index to update grid
    for index, cord in enumerate(Coordinates.cordArray):  # get all pixels at once (in grayscale)
        pixel = gray_image.getpixel(cord)  # get the value of a pixel at any coordinate
        # print(f'pixel = {pixel}')
        pos = Values.valueArray.index(pixel)  # find index of value in array based on grayscale value
        # print(f'pos = {pos}')
        print(f'tile {cord}, grayscale value: {pixel}')
        if pos == 0:
            currentGrid[index] = 0
        else:
            currentGrid[index] = pow(2, pos)


def display_grid(grid):
    for i in range(len(grid)):
        if i % 4 == 0:
            print(f'[ {grid[i]}  {grid[i+1]}  {grid[i+2]}  {grid[i+3]} ]')


def swipe_row(row):
    prev = -1
    i = 0
    temp = [0 for x in range(4)]

    for element in row:
        if element != 0:  # never take empty tiles into consideration
            if prev == -1:
                prev = element  # make previous the first non-zero element & first element in temp array
                temp[i] = element
                i += 1
            elif prev == element:  # if current element is equal to prev, then they get added
                temp[i-1] = 2*prev
                prev = -1  # give prev a -1 value as it can no longer can be added to another element
            else:  # else: we just add the element to temp
                prev = element
                temp[i] = element
                i += 1
    return temp


def get_next_grid(grid, move):
    temp = [0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0]

    if move == UP:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + 4*j])  # append elements to the row, splitting the grid vertically
            row = swipe_row(row)  # add the swiped row to temp
            for j, val in enumerate(row):
                temp[i + 4*j] = val
    elif move == LEFT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4*i + j])  # append elements to the row, splitting the grid vertically
            row = swipe_row(row)  # add the swiped row to temp
            for j, val in enumerate(row):
                temp[4*i + j] = val
    elif move == DOWN:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + 4 * (3-j)])  # append elements to the row, splitting the grid vertically
            row = swipe_row(row)  # add the swiped row to temp
            for j, val in enumerate(row):
                temp[i + 4 * (3-j)] = val
    elif move == RIGHT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4 * i + (3-j)])  # append elements to the row, splitting the grid vertically
            row = swipe_row(row)  # add the swiped row to temp
            for j, val in enumerate(row):
                temp[4 * i + (3-j)] = val

    return temp


get_grid()
display_grid(currentGrid)
print('-'*20)
display_grid(get_next_grid(currentGrid, RIGHT))



