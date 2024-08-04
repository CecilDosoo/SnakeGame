# SnakeGame

- Developed a Python program inspired by the classic mobile Snake game. The game functions similarly to the original Snake game, providing an authentic gameplay experience.
  
- Utilized object-oriented programming (OOP), along with the Turtle graphics and Time modules.
- 
![image](https://github.com/user-attachments/assets/3db9a863-d9d5-4090-a5bd-827e0cd83a34)


# SCOREBOARD CLASS
- The scoreboard class is used to right and update the score at the top of the screen. This also uses the turtle module
  
- The update_score function within the Scoreboard class deletes the current score and updates it by incrementing the score by 1 whenever the turtle eats the food.
  
- I have implemented a reset function that opens the highscore.txt file and compares the stored high score with the current score. If the current score is higher, it updates the file with the new high score. This allows users to track their high scores across multiple gameplays, rather than resetting each time the program runs.
  
- I have the increase_score which increases the score by one each time the snake eats a food

# SNAKE CLASS
- The Snake class creates and manages the snake's behavior in the game. It initializes the snake with three segments, controls movement, and handles growth when the snake eats food. The class includes methods to reset the snake, extend its length, and change its direction while ensuring it does not reverse.

- The create_snake function initializes the starting snake, consisting of three turtle blocks positioned along the x-axis at predetermined locations. It uses these positions and passes them to the add_segment function, where each turtle segment is created

- The add_segment function is responsible for creating each turtle segment of the snake. Once a turtle is created, it is added to the list called segments, which contains all the turtle segments of the snake.

- The reset function is used to return the snake to its initial starting position if it collides with a wall or its own tail. It does this by moving the existing segments off-screen and then recreating the snake from scratch.

- The extend function is simply used to add another turtle to the back of the snake once the snake eats the food

- The move function controls the snake's movement. When the game starts or the user directs the snake, the function updates each segment’s position to match the segment directly in front of it, except for the head. The head moves in the specified direction (up, down, left, or right), while the other segments follow the previous segment’s position, creating the illusion of continuous movement.

- The up, down, left, and right functions adjust the direction of the snake's head based on the angle values. They change the heading of the head to the respective direction while ensuring that the snake cannot reverse direction.


# FOOD CLASS
- The Food class is used to create the food object and change its position randomly each time it is eaten. It is implemented using the Turtle module.
