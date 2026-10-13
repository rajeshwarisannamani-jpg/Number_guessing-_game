# Number Guessing Game

A beginner-friendly Python command-line game created for the CodeOrbit
internship task.

## Features

-   Generates a random number between 1 and 100.
-   Gives hints when a guess is too high or too low.
-   Counts valid guesses.
-   Handles invalid input with `try/except`.
-   Checks that guesses are within the allowed range.
-   Allows the player to play multiple rounds.

## Requirements

-   Python 3.x
-   No external packages are required. The game uses Python's built-in
    `random` module.

## How to Run

1.  Download or clone this repository.

2.  Open a terminal in the project folder.

3.  Run:

    ``` bash
    python number_guessing_game.py
    ```

    If your system uses `python3`, run:

    ``` bash
    python3 number_guessing_game.py
    ```

4.  Follow the prompts in the terminal.

## How to Play

1.  The program chooses a secret number from 1 to 100.
2.  Enter a whole-number guess.
3.  Follow the `Too low` or `Too high` hints.
4.  Continue until you guess correctly.
5.  Choose whether to play another round.

## Project Structure

``` text
number-guessing-game/
├── number_guessing_game.py
├── README.md
└── .gitignore
```

## Concepts Practiced

-   Variables and user input
-   `if` / `elif` / `else` conditions
-   `while` loops
-   Functions
-   The `random` module
-   Exception handling with `try` / `except`

## Author

Created as a Python practice project for the CodeOrbit internship task.
