from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
# from game_over import GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
# game_is_on = True
food = Food()
score = Score()


# game_over = GameOver()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="space", fun=score.end_game)



# def new_game():
#     snake.resetscreen()
#     score.resetscreen()
#     game_over.clear()
#     screen.update()
#     time.sleep(0.1)
#     global game_is_on = True


while score.game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend( )


   #detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        score.reset()
        snake.reset()
        screen.update()
        time.sleep(0.5)
        # game_over.for_replay()
        # screen.onkey(key="space", fun=new_game)

    #detect collision with tail
    for seg in snake.snake[3:]:
       if snake.head.distance(seg) < 15:
            # game_is_on = False
            score.reset()
            snake.reset()
            screen.update()
            time.sleep(0.5)


# screen.exitonclick()