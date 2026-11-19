##classes and objects constructor init() method
# class Student:
#     def __init__(self,name,cgpa):
#         self.name=name
#         self.cgpa=cgpa
#     def get_cgpa(self):
#         return self.cgpa
# stu1=Student("Suraj",9.3)
# stu2=Student("tanmay",8.5)
# print(stu1.name,"has cgpa:",stu1.get_cgpa())
# print(stu2.name,"has cgpa:",stu2.get_cgpa())


##instance methods
# class laptop:
#     storage_type="ssd"

#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage

#     def get_info(self):
#         print("laptop has",self.RAM,"RAM &",self.storage," ",self.storage_type)

# l1=laptop("16gb","512gb")
# l2=laptop("8gb","256gb")

# l1.get_info()


##class methods and static methods
# class laptop:
#     storage_type="ssd"

#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage

#     def get_info(self):
#         print("laptop has",self.RAM,"RAM &",self.storage," ",self.storage_type)

#     @staticmethod
#     def calc_discount(price,discount):
#        final_price=price-(discount*price/100)
#        print("Discounted price=",final_price)

# l1=laptop("16gb","512gb")

# l1.calc_discount(80000,10)   


##all three attributes example
#design and create an online store for products(name,price)
#track total products being created
#create a static method to calculate discount on each product based on a %parameter
# class Product:
#     count=0

#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Product.count+=1

#     def get_info(self):
#         print("price of",self.name,"is Rs.",self.price)

#     @classmethod
#     def get_count(cls):
#         print("total products in store=",cls.count)

#     @staticmethod
#     def calc_discount(price,discount):
#         print("discount price=",price-(price*discount/100))

# p1=Product("phone",10_000)
# p2=Product("laptop",50_000)
# p3=Product("pen",10)

# p1.get_info()  #Instance method
# Product.get_count()  #class method
# p1.calc_discount(p1.price,12) #Static method


##encapsulatio in oops
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name   #public
#         self.__balance=balance   #private

#     def get_balance(self):  #getter
#         return self.__balance

#     def set_balance(self,newbalance):   #setter
#         self.__balance=newbalance

# acc1=BankAccount("Suraj Somuse",10_000)

# acc1.set_balance(23_000)
# print(acc1.name,acc1._BankAccount__balance)


##inheritance in oops
# class Employee:
#     start_time="10am"
#     end_time="6pm"

#     def change_time(self,new_end_time):
#         self.end_time=new_end_time

# class Adminstaff(Employee):
#     def __init__(self,role):
#         self.role=role

# staff1=Adminstaff("manager")
# print(staff1.role,staff1.start_time,staff1.end_time)    


##multiple inheritance type
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary

# class Student:
#     def __init__(self,gpa):
#         self.gpa=gpa

# class TA(Teacher,Student):
#     def __init__(self,salary,gpa,name):
#         super().__init__(salary)
#         Student.__init__(self,gpa)
#         self.name=name

# ta1=TA(15_000,8.5,"Suraj")    
# print(ta1.name,ta1.gpa,ta1.salary)    


##abstraction
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")

# lion=Lion()
# lion.make_sound()

# cow=Cow()
# cow.make_sound()


##polymorphism(function overriding)
# class Employee:
#     def get_designation(self):
#         print("designation=Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation=Teacher")

# t1=Teacher()
# t1.get_designation()


##polymorphism(duck)
# class Employee:
#     def get_designation(self):
#         print("designation=Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation=Teacher")

# class Accountant(Employee):
#     def get_designation(self):
#         print("designation=Accountant")

# t1=Teacher()
# t1.get_designation()

# acc1=Accountant()
# acc1.get_designation()
