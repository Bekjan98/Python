class Car:
	name = "My"
	height = 1000
	speed = 200.00

	def __init__(self, name, height):
		self.name = name
		self.height = height
		print (self.name, "has height", self.height)

	def set (self, name, height, speed):
		self.name = name
		self.height = height
		self.speed = speed

class Truck (Car):  #Наследник класса
	wheels = 8

	def __init__(self):  #теперь мы не будем добавлять никаких параметров
		pass

man = Truck ()
man.wheels = 12
man.set ("Man", 5000, 142.05)
print (man.height)

audi = Car ("Audi", 1500)
audi.set ("Audi", 150, 325.12)
print (audi.name)

shoka = Car ("shoka", 1500)
shoka.set ("shoka", 1500, 325.12)
print (shoka.name)

