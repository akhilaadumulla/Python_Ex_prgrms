# class Animal: 
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# class Cat(Animal):
#     def purr(self):
#         print("Purr...")
        
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")

# fido = Dog("Fido", "brown")
# print(fido.color)
# fido.bark()

# class Vehicle: 
#     def horn(self):
#         print("Beep!")

# class Car(Vehicle):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# obj = Car("BMW", "red")
# obj.horn( )

class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()