##create bankaccount class with attributes account number,owner name,and balance add method to deposit,withdraw and check balance
# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number=account_number
#         self.owner_name=owner_name
#         self.__balance=balance

#     def deposit(self,amount):
#         self.__balance+=amount
#         print("₹",amount,"deposited successfully")

#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             print("₹",amount,"withdraw successfully")
#         else:
#             print("Insufficient Balance!")

#     def check_balance(self):  
#         return self.__balance      

# acc1=BankAccount("101","Suraj Somuse",10_000)
# acc1.deposit(5000)
# acc1.withdraw(2000)
# print("Current Balance:",acc1.check_balance())


##create class book with attributes title,author,list of reviews and add methods to add new review,count reviews,and display all reviews
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         self.reviews=[]

#     def add_review(self,review):
#         self.reviews.append(review)

#     def count_reviews(self):
#         return len(self.reviews)

#     def display_reviews(self):
#         if not self.reviews:
#             print("No reviews available.")
#         else:
#             print("Reviews for",self.title,":")
#             for i,review in enumerate(self.reviews,start=1):
#                 print(f"{i}.{review}")

# book1=Book("secrets of richness","Suraj Somuse")
# book1.add_review("very helpfull book")
# book1.add_review("comedy book")
# print("Total Reviews:",book1.count_reviews())
# book1.display_reviews()


##create class student with private attribute name,roll no and marks provide getter and sette method with validation
# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.__name=name
#         self.__roll_no=roll_no
#         self.__marks=marks

#     def get_name(self):
#         return self.__name

#     def get_roll_no(self):
#         return self.__roll_no

#     def get_marks(self):
#         return self.__marks

#     def set_name(self,new_name):
#         if new_name!="":
#             self.__name=new_name
#         else:
#             print("Name cannot be empty!")

#     def set_roll_no(self,new_roll_no):
#         if 1<=new_roll_no<=100:
#             self.__roll_no=new_roll_no
#         else:
#             print("Roll no must be between 1 and 100")

#     def set_marks(self,new_marks):
#         if new_marks>=0:
#             self.__marks=new_marks
#         else:
#             print("marks cannot be negative")

# stu1=Student("Suraj",25,85)
# stu1.set_name("Rahul")
# stu1.set_roll_no(50)
# stu1.set_marks(90)
# print("Name:",stu1.get_name())
# print("Roll no:",stu1.get_roll_no())
# print("Marks:",stu1.get_marks())    


##create class shape with method area create subclasses circle,rectangle and triangle that override area method
# class Shape:
#     def area(self):
#         print("Area of shape")

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print("Area of circle:",3.14*self.radius*self.radius)

# class Rectangle(Shape):
#     def __init__(self,length,width):
#          self.length=length
#          self.width=width
#     def area(self):
#         print("Area of rectangle:",self.length*self.width)
            
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         print("Area of Triangle:",0.5*self.base*self.height)

# c=Circle(5)  
# r=Rectangle(10,4)
# t=Triangle(8,6)

# c.area()
# r.area()
# t.area()


##create base class vehicle with attibutes like brand and model create two subclasses car and bike that add extra attribute seats and engines
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# class Car(Vehicle):
#     def __init__(self, brand, model,seats):
#         super().__init__(brand,model)
#         self.seats=seats

# class Bike(Vehicle):
#     def __init__(self, brand, model,engine_cc):
#         super().__init__(brand, model)        
#         self.engine_cc=engine_cc

# car1=Car("Tata","maruti",6)
# bike1=Bike("duke","fz",350)

# print("car details")
# print("Brand:",car1.brand)
# print("Model:",car1.model)
# print("Seats:",car1.seats)
# print("\nBike details")
# print("Brand:",bike1.brand)
# print("Model:",bike1.model)
# print("Engine cc:",bike1.engine_cc)


##create abstract class employee with abstract method calculate_salalry calculate subclasses intern,fulltimeemployee and contractEmployee that implement method differently
# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Intern(Employee):
#     def __init__(self, stipend):
#         self.stipend=stipend
#     def calculate_salary(self):
#         return self.stipend

# class FullTimeEmployee(Employee):
#     def __init__(self,monthly_salary):
#         self.monthly_salary=monthly_salary
#     def calculate_salary(self):
#         return self.monthly_salary

# class ContractEmployee(Employee):
#     def __init__(self,hours,rate_per_hour):
#         self.hours=hours
#         self.rate_per_hour=rate_per_hour
#     def calculate_salary(self):
#         return self.hours*self.rate_per_hour

# i=Intern(10000)
# f=FullTimeEmployee(50000)
# c=ContractEmployee(120,500)
# print("Intern salary:",i.calculate_salary())
# print("Full Time Salary:",f.calculate_salary())
# print("Contract Employee Salary:",c.calculate_salary())


##create class person that allows constructor to work with name only name+age name+age+address
# class Person:
#     def __init__(self,name,age=None,address=None):
#         self.name=name
#         self.age=age
#         self.address=address
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Address:",self.address)
#         print()

# p1=Person("Suraj")
# p2=Person("Rahul",21)
# p3=Person("Amit",22,"pune")

# p1.display()
# p2.display()
# p3.display()


##create class player with class variable player_count instance variables name and level track how many players were created
# class Player:
#     player_count=0

#     def __init__(self,name,level):
#         self.name=name
#         self.level=level

#         Player.player_count+=1

# p1=Player("Suraj",4)
# p2=Player("Sayali",6)
# p3=Player("cat",3)

# print(p1.name,p1.level)
# print(p2.name,p2.level)
# print(p3.name,p3.level)
# print("Total no of players created:",Player.player_count)


##create classes herbivore carnivore omnivore with some attributes and methods then create class bear that inherits from all above classes to showcase how multiple inheritance works
# class Herbivore:
#     def __init__(self):
#         self.plant_food="Plants"
#     def eat_plants(self):
#         print("Eats plants.")

# class Carnivore:
#     def __init__(self):
#          self.meat_food="Meat"
#     def eat_meat(self):
#         print("Eats meat.")

# class Omivore:
#     def __init__(self):
#         self.food_type="Plants and Meat"
#     def eat_both(self):
#         print("Eats both plants and meat.")

# class Bear(Herbivore,Carnivore,Omivore):
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print("Animal:",self.name)

# bear=Bear("Brown Bear")
# bear.display()
# bear.eat_plants()
# bear.eat_meat()
# bear.eat_both()        


##create chat system using oops concept create classes user message chatroom and implement functions sending messages viewing chat history and user joining and leaving chatroom
# class User:
#     def __init__(self,username):
#         self.username=username
#     def __str__(self):
#           return self.username

# class Message:
#      def __init__(self,sender,text):
#           self.sender=sender
#           self.text=text
#      def display(self):   
#           print(self.sender,":",self.text)

# class ChatRoom:
#      def __init__(self,room_name):
#           self.room_name=room_name
#           self.users=[]
#           self.messages=[]
#      def join(self,user):
#           self.users.append(user)
#           print(user,"joined chat room") 
#      def leave(self,user):
#           if user in self.users:
#              self.users.remove(user)
#              print(user,"left the room")
#      def send_message(self,user,text):
#           if user in self.users:
#                msg=Message(user,text)
#                self.messages.append(msg)
#           else:
#                print(user,"is not in chat room")
#      def view_chat_history(self):
#           print("\n----Chat History----")
#           for msg in self.messages:
#                msg.display()

# user1=User("Suraj")
# user2=User("Sayali")
# chatroom=ChatRoom("General") 
# chatroom.join(user1)
# chatroom.join(user2)
# chatroom.send_message(user1,"Hello eyeryone")
# chatroom.send_message(user2,"Hi suraj")
# chatroom.view_chat_history()
# chatroom.leave(user2)


