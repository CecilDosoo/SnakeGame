# Snake Game

This project is a Python program inspired by the classic Snake game. It uses object-oriented programming (OOP) principles along with the Turtle graphics and Time modules to create an engaging and authentic gameplay experience.

![Game Screenshot](https://github.com/user-attachments/assets/3db9a863-d9d5-4090-a5bd-827e0cd83a34)


https://github.com/user-attachments/assets/4c4b7938-bdc4-4033-9aee-cb192cc4b95a


## Components

### Scoreboard Class

The `Scoreboard` class manages and displays the score at the top of the screen.

- **`update_score()`**: Deletes the current score and updates it by incrementing the score by 1 whenever the snake eats food.
  
- **`reset()`**: Opens the `highscore.txt` file to compare and update the high score if the current score is higher. This feature allows users to track high scores across multiple game sessions.
  
- **`increase_score()`**: Increases the score by one each time the snake consumes food.

### Snake Class

The `Snake` class creates and manages the snake’s behavior.

- **`create_snake()`**: Initializes the snake with three segments positioned along the x-axis at predefined locations.
  
- **`add_segment()`**: Creates a new turtle segment and adds it to the list of segments, representing the snake’s body.
  
- **`reset()`**: Moves the existing segments off-screen and recreates the snake from scratch if it collides with a wall or its own tail.
  
- **`extend()`**: Adds a new segment to the end of the snake when it eats food.
  
- **`move()`**: Updates the position of each segment to follow the segment in front, with the head moving in the specified direction.
  
- **`up()`, `down()`, `left()`, `right()`**: Adjust the direction of the snake’s head based on user input, ensuring the snake cannot reverse direction.

### Food Class

The `Food` class handles the creation and placement of food objects.

- **`create_food()`**: Generates a food item at a random location on the screen.
  
- **`move_food()`**: Changes the food’s position randomly each time it is eaten by the snake.

## How to Run

To play the game, ensure you have Python installed on your system. Execute the main Python script to start the game.
