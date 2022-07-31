from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
	def __init__(self):
		self.segments=[]

		for i in POSITIONS:
			new_segment=Turtle()
			new_segment.penup()
			new_segment.color("white")
			new_segment.goto(i)
			new_segment.shape("square")
			new_segment.speed(0)
			self.segments.append(new_segment)
		self.head=self.segments[0]
	
	def move(self):
		for i in range(len(self.segments)-1,0,-1):
			self.segments[i].goto(self.segments[i-1].xcor(),self.segments[i-1].ycor())
		self.segments[0].forward(MOVE_DISTANCE)
	
	def up(self):
		if self.head.heading()!=DOWN:
			self.head.setheading(UP)
	def down(self):
		if self.head.heading()!=UP:
			self.head.setheading(DOWN)
	def left(self):
		if self.head.heading()!=RIGHT:
			self.head.setheading(LEFT)
	def right(self):
		if self.head.heading()!=LEFT:
			self.head.setheading(RIGHT)
	
	def inc_len(self):
		new_segment=Turtle()
		new_segment.penup()
		new_segment.color("white")
		new_segment.shape("square")
		new_segment.speed(0)
		self.segments.append(new_segment)
		if self.segments[len(self.segments)-2].heading()==UP:
			new_segment.goto(self.segments[len(self.segments)-2].xcor(),self.segments[len(self.segments)-2].ycor()-20)
		elif self.segments[len(self.segments)-2].heading()==DOWN:
			new_segment.goto(self.segments[len(self.segments)-2].xcor(),self.segments[len(self.segments)-2].ycor()+20)
		elif self.segments[len(self.segments)-2].heading()==LEFT:
			new_segment.goto(self.segments[len(self.segments)-2].xcor()+20,self.segments[len(self.segments)-2].ycor())
		elif self.segments[len(self.segments)-2].heading()==RIGHT:
			new_segment.goto(self.segments[len(self.segments)-2].xcor()-20,self.segments[len(self.segments)-2].ycor())
			
	def check_col_wall(self):
		if self.head.xcor()>300 or self.head.xcor()<-300 or self.head.ycor()>300 or self.head.ycor()<-300:
			return True
		else:
			return False
			
	def check_col_itself(self):
		for i in range(2,len(self.segments)):
			if self.head.distance(self.segments[i])<=10:
				return True
		return False
		
