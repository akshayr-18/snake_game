from turtle import Turtle
class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score=0
		self.speed(0)
		self.goto(0,260)
		self.color("white")
		self.penup()
		self.update_scoreboard()
		self.hideturtle()
	
	def update_scoreboard(self):
		self.write(f"SCORE : {self.score}",align="center",font=("Arial",24,"normal"))
		
	def inc_score(self):
		self.score+=1
		self.clear()
		self.update_scoreboard()
	
	def gameover(self):
		self.goto(0,0)
		self.write(f"GAME OVER.",align="center",font=("Arial",24,"normal"))
