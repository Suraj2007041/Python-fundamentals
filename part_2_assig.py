##program that takes salary as input and find tax
# salary=int(input("Enter your salary:"))
# if salary<30000:
#     salary1=salary*12*5/100
#     print("your yearly tax is",salary1)
# elif salary>=30000 or salary<=70000:
#     salary2=salary*12*15/100
#     print("your yearly tax is",salary2)
# elif salary>70000:
#     salary3=salary*12*25/100
#     print("your yearly tax is",salary3)
# else:
#     print("your yearly tax is",salary3)


##take two integer and print all even number between them
# a=int(input("Enter a first num:"))
# b=int(input("Enter a second num:"))
# for i in range(a,b+1):
#     if i%2==0:
#         print(i)


##prints digit of a number as a output
# n=int(input("Enter a number:"))
# while n>0:
#     digit=n%10
#     n=n//10
#     print(digit)
# n = input("Enter a number: ")
# for i in n:
#     print(i)

##return count of number of digits in a number
# n = input("Enter a number: ")
# count=0
# for i in n:
#     count=count+1
# print(count)
# n = input("Enter a number: ")
# print(len(n))

##return sum of digit which taken as input
# n = int(input("Enter a number: "))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print("Sum of a number",sum)

##program of a number from 1 to 100 which are divisible by 3 and 5
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)


##program that take continously a number from user and print it is + or - until user enters quit
# while True:
#     n=input("Enter a number(or Quit to stop):")
#     if n=="Quit":
#         print("code stop successfully")
#         break
#     n=int(n)
#     if n>0:
#         print("positive number")
#     elif n<0:
#         print("negative number")
#     else:
#         print("zero")

##build a calculator using function
# a=int(input("Enter a first number:"))
# b=int(input("Enter a second number:"))
# operation=input("Enter a operation (+,-,*,/):")
# def calculator(a,b,operation):
#     if operation=="+":
#        return a+b
#     elif operation=="-":
#         return a-b
#     elif operation=="*":
#         return a*b
#     elif operation=="/":
#         return a/b
#     else:
#         print("Invalid operation ")
# print("Result:",calculator(a,b,operation))


##write a function is_prime(n) that returns true if n is prime no and false otherwise using loop
# n=int(input("Enter a number:"))
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# if is_prime(n):
#     print("Prime number")
# else:
#     print("Not a prime number")    

##number guessing game
# import random
# computer=random.randint(1,100)
# tries=0
# while True:
#     tries=tries+1
#     human=int(input("Enter a number between 1 to 100:"))
#     if human==computer:
#         print("Congratuation you win")
#         break
#     elif human>computer:
#         print("Sorry num is too high")
#     elif human<computer:
#         print("Sorry num is too low")
#     else:
#         print("invalid input")









