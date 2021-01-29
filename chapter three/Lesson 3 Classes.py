
# LESSON 3
# Classes in Python
# Used to define new types and model real tasks
# uses Pascal naming convention "FirtWordAlwaysCapital"

# Object is an instance of a class

class ComputeEngine:
    def cloud(self):
        print("Welcome to Google Cloud")
    def vm_instance(self):
        print("Create VM instance")
cloud_vm = ComputeEngine() # object of type Compute Engine and store in a variable name
cloud_vm.cloud() # calls the draw method on the cloud method
cloud_vm.vm_instance() # calls the vm instance method on the vm function


# Class parameters

class Points:
    def draw(self):
        print("draw")
    def plot(self):
        print("plot")
# you can create different objects from same class

point1 = Points()
point1.x = 5
point1.y = 8
point1.z = 9
print(point1.z)

point2 = Points()
point2.x = 2
point2.y = 4
point2.z = 6
print(point2.x)
