from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_display()  
    
    def update_display(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, "center", ("Courier", 20, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_display()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Courier", 24, "normal"))