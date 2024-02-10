# Snake Game in Python

A classic console-based Snake game implemented using the Curse library in Python. The game offers various difficulty levels, scoring mechanics, and improved visuals through colored characters.

## Features
- Three difficulty levels to choose from
  - **Level 1**: Slow speed & smaller board
  - **Level 2**: Medium speed & medium board
  - **Level 3**: Fast speed & larger board
- Scoring system with automatic level progression based on points earned.
- Colored characters representing the snake, food, border, and background.


## Requirements
Python >= 3.6

Curse Library (Should come preinstalled with Python distribution for Unix systems including Linux and Mac OS X. For Windows users, run `pip install windows-curses`).


## How to Play

1) Run the program using `python snake_game.py` in your terminal or command prompt.
2) Use arrow keys to control the movement of the snake and eat the food represented by the pi symbol (π). Each eaten piece increases the length of the snake and grants one point.
3) Avoid colliding with the walls or the snake's own body parts. Doing so ends the game.
4) Progressively harder levels unlock automatically once enough points are achieved.


## Controls

| Key        | Function      |
| ------|-----|
| Arrow Keys  	| Change Direction 	|
| Q / Escape  	| Quit Application 	|


## Source Code Structure
- `init_colors()`: Initializes the colors used throughout the application.
- `raw_border(window)`: Renders a border surrounding the play area within the specified dimensions.
- `print_center(window, txt, attr=None)`: Prints centered text inside a given window object. Optionally accepts custom attributes such as color pairs.
- `check_for_next_level(current_score)`: Verifies whether the provided score surpasses the minimum requirement necessary for advancing to the subsequent level. Returns true if the conditions are met and false otherwise.



## **Notes**
**Feel free to further customize the gameplay experience by modifying the existing codebase. Additions might involve introducing powerups, varying food types, incorporating high scores, and more. Have fun!**
