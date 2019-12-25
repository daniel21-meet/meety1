import turtle
from turtle import Turtle

class Ball (Turtle):
	def __init__(self, R,color,dx,dy):
		Turtle.__init__(self)
		self.penup
		self.R = R
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.color = color
		self.shapesize(R/10)
	def move (self, screen_width,screen_high):
	
		screen_height = turtle.getcanvas().winfo_height()/2
		screen_width = turtle.getcanvas().winfo_width()/2

		current_x = self.xcor()
		new_x = current_x + self.dx

		current_y = self.ycor()
		new_y = current_y + self.dy

		right_side_ball = new_x + self.R
		left_side_ball = new_x - self.R
		upper_side_ball = new_y + self.R
		lower_side_ball = new_y - self.R

		self.goto(new_x,new_y)

		#if screen_high or screen_width =>  :

		#while 1 == 1:
			#self.move
ball1 = Ball(5,"yellow", 5, 4)
ball1.move(10,10)





