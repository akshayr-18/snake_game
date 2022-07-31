from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
s=Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
segments=[]
positions=[(0,0),(-20,0),(-40,0)]
sss=Snake()
f=Food()
score=Scoreboard()
s.listen()
s.onkey(sss.up,"Up")
s.onkey(sss.down,"Down")
s.onkey(sss.left,"Left")
s.onkey(sss.right,"Right")
s.update()
game_is_on=True
while game_is_on:
	s.update()
	time.sleep(0.1)
	sss.move()
	if sss.head.distance(f)<=15:
		f.ht()
		f=Food()
		sss.inc_len()
		score.inc_score()
	if sss.check_col_wall():
		game_is_on=False
	if sss.check_col_itself():
		game_is_on=False
score.gameover()



s.exitonclick()
