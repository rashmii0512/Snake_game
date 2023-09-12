from turtle import Screen, Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT =  180
SNAKE_COLOR = "white"

class Snake:
    def __init__(self):
        self.snake = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.snake[0]
        # self.snake[0].color("white")
        # self.snake[1].color("orange")

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        """used to increase the size of the snake one segment at a time"""
        self.segment = Turtle(shape="square")
        self.segment.penup()
        self.segment.speed("slowest")
        self.segment.color(SNAKE_COLOR)
        self.segment.goto(positions[0], positions[1])
        self.snake.append(self.segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        # for seg_num in range(start= 2, stop= -1, step= -1):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            '''all segments except first one move to the position of segment ahead of it,
                that way we ensure that the snake is always moving forward 
                and all segments are in the same direction even if direction of head changes'''
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """reset the snake when a new game starts"""
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]



