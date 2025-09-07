# Object orianted approach to handle errors in Python.
# provide security to the code .
# class Factory:
#     a = 12 # /Attribute

#     def hello(self): # /Method
#         print("How are you")

    # print("hello how are you i am getting initilized")

# print(Factory().a)

# Factory().hello()

# obj = Factory() # /Object

# print(obj.a)

# obj.hello()

# class Factory:
#     a = 12 # /Attribute

#     def hello(self): # /Method
#         print("How are you")


# obj = Factory()

# obj2 = Factory()

# obj.hello()

# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print( f"your object details are: {self.material}, {self.zips} , {self.pockets}")

# reebok = Factory("leather",3,2)

# campus = Factory("nylon",3,3)


# reebok.show()

# class Animal :
#     name = " lion " #class attribute 

#     def __init__(self,age):
#         self.age = age # instance attribute

#     def show(self):#/instance method
#         print(f" how RE YOU BROTHER {self.age}")

#     @classmethod
#     def hello(cls): # class method
#         print(f"how are you brother {cls.age}")

#     @staticmethod
#     def static():
#         print("how are you ")

# obj = Animal(12)

# obj.static()

# class Factorymumbai :  #parent class /super class
#     a = "I am an attribute mentioned inside factory"
#     def hello(self):
#         print(" hello i am a method mentioned inside factory")

# class Factorypune(Factorymumbai):#child class /subclass
#     pass

# obj = Factorymumbai()
# obj2 = Factorypune()

# print(obj2.hello())



class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")


class Human(Animal):
    pass
Animal1 = Animal("lion")
person1 = Human("gayatri")

person1.show()