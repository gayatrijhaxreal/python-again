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



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"hello your name is {self.name}")


# class Human(Animal):
#     def __init__(self, name ,age):
#         super().__init__(name)
#         self.age = age
        
#     def show(self):
#         print(f"hello your name is {self.name} , {self.age}")



# Animal1 = Animal("lion")
# person1 = Human("gayatri", 18)

# person1.show()

# Animal1.show()

# class Animal:

#     def  __init__(self,name):
#      pass 

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robots(Human,Animal):
#     name3 = "charli123"

# obj = Robots()

# print(obj.name3)

# class Factory :
#     def __init__(self ,material,zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory(Factory):
#         def __init__(self,material,zips,color):
#              super().__init__(material,zips)
#              self.color = color

# class PuneFactory(Factory):
#         def __init__(self,material,zips,color,pockets):
#              super().__init__(material,zips,color)
#              self.pockets = pockets

# def show():
#     print("how are you")

# def show():
#     print("you are best")

# show()


# class Animal :
#     def show():
#         print("hello i am aakarsh")

 
        
# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj =Human()

# obj.Show()


# class Animal:
#     def show(self):
#         print("i am showing")

# class human:
#     def show(self):
#         print("hello I am also showing")

# obj = Animal()
# obj2 = human()

# obj.show()
# obj2.show()
  


  

 
# from abc import ABC, abstractmethod


# class abstract(ABC):
    
#     @abstractmethod
#     def perimeter(self):
#         pass


#     @abstractmethod
#     def area(self):
#         pass 



# class Square(abstract):
#     def __init__(self,side):
#         self.side = side 
    
#     def perimeter(self):
#         print("i have perimeter")

#     def area(self):
#         print("i have created this")
# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius =radius
    

#     def perimeter(self):
#         print("i have perimeter")

#     def area(self):
#         print("i have created this")

# obj = Circle(7)
# obj = Square(12)


# // Dunder menthods


# class Animal :
#     def __init__(self, name):
#         self.name = name 

#     def __str__(self):
#         print("hello how are you ")

# obj = Animal("lion")

# print(obj)



# class Animal:
#     @property 
#     def show(self):
#         print("hello how are you ")

# obj = Animal()

# obj.show 

