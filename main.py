from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()  # refresh screen
    time.sleep(0.1)  # delay for 0.1
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


############  SNAKE GAME READ ME
#  Developed a python program based on the infamous mobile snake game
#  Developed the program through oop, the turtle and time module.
#  The game runs just like how the snake game runs

#### SCOREBOARD CLASS
# The scoreboard class is used to right the score at the top of the screen. This also uses the turtle module
# It has the update_score function to delete the score and update it with score + 1 whenever the turtle eats the food
# I have the reset function that opens the highscore.txt file, compares the value in there with the current score.
    #If the current score is higher than the value in the txt file, it replaces the value in there with the current score
      #which then becomes the new highscore. Therefore, the user has a way to track their highscores instead of it
        # reseting each time the program is ran again.
# I have the increase_score which increases the score by one each time the snake eats a food

###### SNAKE CLASS
#The snake class was used to create the starting snake, and be able to increase its length each time the snake eats a food

#The create_snake function creates the starting snake. It consists of 3 blocks of turtles with predeterminded starting positions
  #one with another rright next to it along the x axis. It uses those positions then passes it into the the add_segment function
    #where the turtle is created

#The add_segment function is where the turtle is actually created. Once its created we add it into the list containting
  #all the turtles called "segments"


#The reset function is used to reset the snake back to its initial starting position once the user hits a wall or its own tail.
    #We did this by sending the previous snake before the user crashed to a position way outside the screen area. so it cant be seen
        #then created the snake again

#The extend function is simply used to add another turtle to the back of the snake once the snake eats the food

#The move function is used to move the snake the moment the game starts and when a user decides. It does this by using
  # the turtles to move to the position of the one on its right excluding the head snake.
    # So the turtle we are on in the for loop will extract the xcor and the ycor of the one next to it and go to that position,
      # and so on. So in realit, only the head turtle is the one moving up, down left or right. whereas the other turtles are just
        #going to the positions of the others


# We then have the up, down, left and right funcitons which moves the head of the snake to its respected position based on the
    #angle value


#####FOOD CLASS
#The food class is used to create the food and change its position randomly each time its eaten. Its also created through the turtle
    #module














screen.exitonclick()

