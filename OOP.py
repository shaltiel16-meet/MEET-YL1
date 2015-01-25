class Animal:
	def __init__ (self, name, age, color, size):
		self.name = name
		self.age = age
		self.color = color
		self.size = size
	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)
	def eat(self, food):
		print("The Animal " + self.name + " is eating " + food)
	def sleep(self, dream):
		print("The Animal " + self.name + " is sleeping for " + str(dream) + " hours")

a = Animal("me", 22, "red", "tiny")
a.print_all()
a.eat("pizza")
a.sleep(2)
