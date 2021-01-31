
# Chapter 3
# LESSON 4
# Constructors 
# This are objects that get called when calling an object
# Each object is a different instance of a class

class Coordinates:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def drawPoints(self):
        print("draw")
    def plotPoints(self):
        print("Ploted")
points1 = Coordinates(20,40)
print(points1.x, points1.y)

# chalenge 2 
# create a new type person,has name attribure and talk method
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("I am talking")
person = Person("Timz Owen")
person.talk()
print(person.name)

# Challenge 3
# create a new animal class, with two methods, legs and eating, and contatente variables
class Animal:
    def __init__(self,name_,leg,food):
        self.leg = leg
        self.food = food
        self.name_ = name_
    def name(self):
        print("")   
    def eating(self):
        print(f"Hello I am {self.name_} and i eat {self.food} ")
    def legs(self):
        print(f"I have {self.leg} legs ")
cow = Animal("Cow",4,"grass")  
cow.eating()      
cow.legs() 
lion = Animal("Lion", 4, "Meat")
lion.eating()
lion.legs()


# INHERITANCE
# helps avoid code duplication by allowing reusable code
class Vehicles:
    def speed(self):
        print("Highest speed is 200km/hr")
class Bmw(Vehicles):
    pass
class Subaru(Vehicles):
    pass



# challenge
# add methods to display specific models and the highest speed

class Vehicles:
    def highest_speed(self,speed):
        self.speed = speed
        print(f"Highest speed is {self.speed}")
class Bmw(Vehicles):
    def bmw_model(self,model_bmw):
        self.model_bmw = model_bmw
        print(f"The model is {self.model_bmw}")
class Subaru(Vehicles):
    def subaru_model(self, model_subaru):
        self.model_subaru = model_subaru
        print(f"The Subaru model is {self.model_subaru}")
bmw1 = Bmw()
bmw1.bmw_model("BMW x3")
bmw1.highest_speed("400km/hr")
subaru1 = Subaru()
subaru1.subaru_model("Subaru Forester")
subaru1.highest_speed("350km/hr")


