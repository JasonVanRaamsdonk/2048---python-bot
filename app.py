from PIL import ImageGrab, ImageOps
import pyautogui
import time

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

# score_grid = [40, 30, 15, 5,
#               30, 20, 10, 0,
#               15, 10, -10, 0,
#               5, 0, 0, 0]

# score_grid = [50, 40, 30, 30,
#               15, 15, 15, 15,
#               0, 0, 0, 0,
#               0, 0, 0, 0]

score_grid = [60, 30, 15, -20,
              30, 15, 5, -20,
              15, 5, 5, -20,
              -10, -10, -10, -20]  # @EuricoC


def get_grid():
    image = ImageGrab.grab()  # get value of every colour on the screen
    gray_image = ImageOps.grayscale(image)  # converts image to greyscale

    # enumerate to keep index to update grid
    for index, cord in enumerate(Coordinates.cordArray):  # get all pixels at once (in grayscale)
        pixel = gray_image.getpixel(cord)  # get the value of a pixel at any coordinate
        # print(f'pixel = {pixel}')
        pos = Values.valueArray.index(pixel)  # find index of value in array based on grayscale value
        # print(f'pos = {pos}')
        # print(f'tile {cord}, grayscale value: {pixel}')
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


def get_grid_score(grid):
    score = 0
    for i in range(4):
        for j in range(4):
            score += grid[4*i+j] * score_grid[4*i+j]
    return score


def get_best_move(grid):
    """
    get the next grid in all directions
    and then compute the score
    :param grid:
    :return:
    """
    score_up = get_grid_score(get_next_grid(grid, UP))
    score_down = get_grid_score(get_next_grid(grid, DOWN))
    score_left = get_grid_score(get_next_grid(grid, LEFT))
    score_right = get_grid_score(get_next_grid(grid, RIGHT))

    if not move_validation(grid, UP):
        score_up = 0
    if not move_validation(grid, DOWN):
        score_down = 0
    if not move_validation(grid, LEFT):
        score_left = 0
    if not move_validation(grid, RIGHT):
        score_right = 0

    # max_score = max(score_up, score_down, score_left, score_right)
    max_score = max(score_up, score_left, score_right)

    if score_up == max_score:
        return UP
    elif score_down == max_score:
        return DOWN
    elif score_left == max_score:
        return LEFT
    else:
        return RIGHT


def perform_move(move):
    """
    functionality to allow the bot to move the grid
    :param move:
    :return:
    """
    if move == UP:
        pyautogui.keyDown('up')
        print('UP')  # @FIXME - grid get caught in UP move loop
        time.sleep(0.05)
        pyautogui.keyUp('up')
    elif move == DOWN:
        pyautogui.keyDown('down')
        print('DOWN')
        time.sleep(0.05)
        pyautogui.keyUp('down')
    elif move == LEFT:
        pyautogui.keyDown('left')
        print('LEFT')
        time.sleep(0.05)
        pyautogui.keyUp('left')
    else:
        pyautogui.keyDown('right')
        print('RIGHT')
        time.sleep(0.05)
        pyautogui.keyUp('right')


def main():
    time.sleep(3)
    while True:
        get_grid()
        perform_move(get_best_move(currentGrid))
        time.sleep(0.1)


def move_validation(grid, move):
    """
    check whether the return value of perform_move
    is actually a valid move
    :param grid:
    :param move:
    :return:
    """
    if get_next_grid(grid, move) == grid:
        return False
    else:
        return True


if __name__ == '__main__':
    main()


# get_grid()
# display_grid(currentGrid)
# print('-'*20)
# # display_grid(get_next_grid(currentGrid, RIGHT))
# # print('-'*20)
# print(get_grid_score(currentGrid))
# perform_move(UP)


# @TODO - add pyautogui move invokes to interact with browser game

