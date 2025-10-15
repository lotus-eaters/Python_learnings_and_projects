# Classic Snake Game

This is a classic Snake game implemented using the Python `turtle` module. The game features a snake that moves around the screen, eating food to grow longer. The player controls the snake's direction using the arrow keys. The game ends if the snake collides with itself or the walls.

## Features

*   Snake movement and control
*   Food generation and consumption
*   Collision detection
*   Score tracking and high score saving
*   Game reset
*   Customizable game settings (width, height, delay, food size)

## Data Structures Used

*   **2D Lists:**
    *   The `snake` variable is a list of lists, representing the snake's body. Each inner list contains the x and y coordinates of a snake segment: `snake = [[x1, y1], [x2, y2], ...]`.
*   **Dictionaries:**
    *   The `offset` dictionary stores the direction vectors for snake movement. It maps direction names (e.g., "up", "down", "left", "right") to coordinate offsets: `offset = {"up": (0, SNAKE_SIZE), "down": (0, -SNAKE_SIZE), ...}`.

## Event Listening and Handling

*   The game uses the `turtle` module's event listening system to detect key presses.
*   `screen.listen()`: Starts listening for keyboard events.
*   `screen.onkey(function, key)`: Binds a function to a specific key press.  For example, `screen.onkey(lambda: set_snake_direction("up"), "Up")` calls the `set_snake_direction` function with the argument "up" when the "Up" arrow key is pressed.
*   `set_snake_direction(direction)`: This function updates the `snake_direction` variable based on the key pressed, ensuring that the snake cannot immediately reverse direction into itself.

## File Operations

*   **High Score Storage:** The game uses file operations to save and load the high score.
*   `open("high_score.txt", "r")`: Opens the "high_score.txt" file in read mode (`"r"`).
*   `open("high_score.txt", "w")`: Opens the "high_score.txt" file in write mode (`"w"`). This will create the file if it doesn't exist or overwrite it if it does.
*   `file.read()`: Reads the entire content of the file.
*   `file.write(str(highscore))`: Writes the high score (converted to a string) to the file.
*   The `try...except` block handles the case where the "high_score.txt" file does not exist when the game starts.

## Exceptions

*   **`IOError` (or `FileNotFoundError` in Python 3.3+):** The code uses a `try...except` block to handle potential `IOError` exceptions that might occur when trying to read the high score from the "high_score.txt" file. This is important because the file might not exist the first time the game is played.

## Math Concepts for Collision Detection

*   **Distance Calculation:** The `get_distance(pos1, pos2)` function calculates the Euclidean distance between two points (positions) using the distance formula:  `distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)`.  This is used to determine if the snake has collided with the food.
*   **Boundary Checks:** The game checks if the snake's head has gone beyond the screen boundaries (walls) by comparing the head's x and y coordinates with the `WIDTH` and `HEIGHT` constants.
*   **Self-Collision:** The game checks if the snake's head has collided with its own body by iterating through the snake's body segments and comparing their coordinates with the head's coordinates.

## Modules Used

*   **`turtle`:**  Provides the graphics and event handling for the game.  It's used for creating the screen, drawing the snake and food, and handling keyboard input.
*   **`random`:**  Used to generate random positions for the food.

## Program Constants

*   `WIDTH`: The width of the game window (800 pixels).
*   `HEIGHT`: The height of the game window (600 pixels).
*   `DELAY`: The delay in milliseconds between screen updates (100 ms).  This controls the speed of the game.
*   `FOOD_SIZE`: The size of the food item (32 pixels).
*   `SNAKE_SIZE`: The size of each snake segment (20 pixels).

## Game Logic

1.  **Initialization:**
    *   The game initializes the screen, snake, food, and score.
    *   It loads the high score from the "high_score.txt" file, if it exists.
2.  **Game Loop (`game_loop()`):**
    *   Clears the previous snake segments.
    *   Calculates the new position of the snake's head based on the current direction.
    *   Checks for collisions (wall or self). If a collision occurs, the game resets.
    *   Adds the new head to the snake's body.
    *   Checks for food collision. If the snake eats the food:
        *   The score is incremented.
        *   The high score is updated if necessary.
        *   The food is moved to a new random position.
    *   If no food is eaten, the last segment of the snake is removed (to maintain the snake's length).
    *   Draws the snake and food on the screen.
    *   Updates the screen title with the current score and high score.
    *   Sets a timer to call the `game_loop()` function again after a delay (`DELAY`).
3.  **Food Collision (`food_collision()`):**
    *   Calculates the distance between the snake's head and the food.
    *   If the distance is less than a threshold, it's considered a collision.
4.  **Reset (`reset()`):**
    *   Resets the score, snake position, and snake direction.
    *   Starts a new game loop.

## Assets

The game uses the following image assets:

*   `assets/bg2.gif`: Background image.
*   `assets/snake-food-32x32.gif`: Food image.
*   `assets/snake-head-20x20.gif`: Snake head image.

Make sure these files are present in the `assets/` directory relative to the Python script.