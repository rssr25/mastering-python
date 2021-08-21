class Person(object):

	population = 50

	def __init__(self, name, age):

		self.name = name
		self.age = age

	@classmethod
	def getPopulation(cls):
		return cls.population

	@staticmethod
	def isAdult(age):
		return age >= 18

	def display(self):
		print(self.name, ' is ', self.age, ' years old')



newPerson = Person("Rahul", 26)

print(Person.getPopulation())
print(Person.isAdult(10))
print(Person.display())