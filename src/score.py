from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 15, "normal"

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.scr = 0
        # with open("dat.txt") as data:
        #     self.high_scr = int(data.read())
        self.high_scr = 0
        self.color("white")
        self.penup()
        self.goto(0,225)
        self.Update_score()
        self.hideturtle()
    
    def Update_score(self):
        self.write(f"Score:{self.scr} | High-Score:{self.high_scr}", align=ALIGNMENT, font=FONT)
    
    def reset_scr(self):
        self.clear()
        if self.scr > self.high_scr:
            self.high_scr = self.scr
            with open("data_file.txt", mode="w") as data:
                data.write(f"{self.high_scr}")                
        self.scr = 0
        self.Update_score()

    def increase_score(self):
        self.clear()
        self.scr += 1
        self.Update_score()
