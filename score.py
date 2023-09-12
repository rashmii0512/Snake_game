from turtle import Turtle
ALIGN = "center"
SMALL_FONT = ("Courier", 15, "normal")
FONT = ("Courier", 20, "normal")
BIG_FONT = ("Courier", 28, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        with open("highScore.txt") as data :
            self.high_score = int(data.read())
        self.game_is_on = True
        self.hideturtle()
        self.goto(0, -280)
        self.write("Press Space to end game", False, align=ALIGN, font= SMALL_FONT)
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, -280)
        self.write("Press Space to end game", False, align=ALIGN, font=SMALL_FONT)
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align=ALIGN, font= BIG_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # self.goto(0, 100)
            # self.write(f"Congratulations! New Highscore: {self.score}", False, align=ALIGN, font=FONT)
            # self.goto(0,260)
            with open("highScore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.show_score()#this function increases the score by 1 so


    def end_game(self):
        self.game_is_on = False



