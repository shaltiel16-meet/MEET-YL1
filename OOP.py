class Animal:
	def __init__ (self, name, age, color, size):
		self.name = name
		self.age = age
		self.color = color
		self.size = size

a = Animal("me", 22, "red", "tiny")
print(a.name)
