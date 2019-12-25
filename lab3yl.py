class animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print ("yummy!! " + self.name + " is eating" + food)
	def description (self):
		print(self.name + " are " + str(self.age) + " years old when they die and they loves the color " + self.favorite_color)
animal1 = animal("mo", "cows", 12, "red")

animal1.eat(" humus")
animal1.description()

