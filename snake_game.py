#Snake v1.0
#by Dixel

import os
import time
import random
import curses

SCORE_COLOR = curses.color_pair(1)
SNAKE_COLOR = curses.color_pair(2)
FOOD_COLOR = curses.color_pair(3)
BACKGROUND_COLOR = curses.A_NORMAL | curses.color_pair(0)
levels = {
    1: {'delay': 200, 'height': 15, 'width': 45},
    2: {'delay': 150, 'height': 20, 'width': 60},
    3: {'delay': 100, 'height': 25, 'width': 75}
}
score = 0
difficulty = 1
snake = []

def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

def draw_border(window):
    h, w = window.getmaxyx()
    window.attron(BACKGROUND_COLOR)
    window.hline(h, 0, 0, w)
    window.hline(0, 0, 0, w)
    window.vline(0, 0, 0, h)
    window.vline(h, 0, 0, w)
    window.attroff(BACKGROUND_COLOR)

def print_center(window, txt, attr=None):
    x = (window.getmaxyx()[1] // 2) - len(txt) // 2
    y = window.getcuryx()[0]
    window.attron(attr if attr else BACKGROUND_COLOR)
    window.addstr(y, x, txt)
    window.attroff(attr if attr else BACKGROUND_COLOR)

init_colors()
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(levels[difficulty]['height'], levels[difficulty]['width'], 0, 0)
w.keypad(1)
w.timeout(levels[difficulty]['delay'])
draw_border(w)
print_center(w, f"Level: {difficulty}", SCORE_COLOR)
print_center(w, f"Score: {score}", SCORE_COLOR)

snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh//2, sw//2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or \
        snake[0][1]  in [0, sw] or \
        snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        score += 1
        print_center(w, f"Score: {score}", SCORE_COLOR)
        if check_for_next_level(score):
            difficulty += 1
            print_center(w, f"Level: {difficulty}", SCORE_COLOR)
            w.timeout(levels[difficulty]['delay'])
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

def check_for_next_level(current_score):
    lvl_threshold = sum([l['height'] * l['width'] for l in levels]) + (len(levels)-1)*5
    return current_score > lvl_threshold
