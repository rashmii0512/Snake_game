from turtle import Turtle
ALIGN = "center"
BIG_FONT = ("Courier", 30, "normal")
SMALL_FONT = ("Courier", 18 , "normal")

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

    def for_replay(self):
        self.write("Game Over", False, align=ALIGN, font=BIG_FONT)
        self.goto(0,-25)
        self.write("Press enter to replay", False, align=ALIGN, font=SMALL_FONT)
