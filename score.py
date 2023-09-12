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
        """Whenever the score increments, the previous score is erased and new score is written"""
        self.clear()
        self.goto(0, -280)
        self.write("Press Space to end game", False, align=ALIGN, font=SMALL_FONT)
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def reset(self):
        """If the score is above high score, update the highscore"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highScore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.show_score()#this function increases the score by 1 so


    def end_game(self):
        self.game_is_on = False



