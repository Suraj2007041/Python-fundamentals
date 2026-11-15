##condition statement
# age=int(input("Enter age:"))
# if age>=18:
#     print("you are eligible for vote")
# else:
#     print("you are not eligible for vote you can vote after,",18-age)

# user=input("Enter red,yellow and green:")
# if user=="red":
#     print("stop")
# elif user=="yellow":
#     print("ready")
# else:
#     print("go") 

# login=input("Enter a username:")
# password=input("Enter a password:")
# if login=="user" and password=="pass@123":
#     print("login successfully")
# elif login!="user":
#     print("wrong username")
# else:
#     print("wrong password")

# num=int(input("Enter a number:"))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")

##match case
# color=input("Enter color:")
# match color:
#     case "Green":
#         print("Go")
#     case "Yellow": 
#         print("look")
#     case "Red":
#         print("Stop")
#     case _:
#         print("Wrong color!")
   
##loops using while
# count=1
# while count<=5:
#     print("hello",count)
#     count+=1

# i=0
# while i<=10:
#     print(i)
#     i+=1

# i=6
# while i>=1:
#     print(i)
#     i-=1

##multiplication table for n
# n=int(input("Enter a number"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

##break using
# i=1
# while i<=10:
#     if i%6==0:
#         break
#     print(i)
#     i+=1

##continue using
# i=0
# while i<10:
#     i+=1
#     if i%3==0:
#         continue
#     print(i)
# print("outside the loop now")

##for loops
# char=input("Enter a character:")
# count=0
# for ch in char:
#     if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
#         count+=1
# print(count)

##range() function     
# n=int(input("Enter a value:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum:",sum)    

##Functions in python
# def sum(a,b):    #funiction definition
#     s=a+b
#     return s
# print(sum(43,34))   #function call

# def avg(a,b,c):
#     sum=a+b+c
#     return sum/3
# print(avg(2,12,453))

##lambda function
# sum = lambda a,b: a+b
# print(sum(34,23))

##factorial of n
# num=int(input("Enter a number:"))
# def fact(num):
#     fact=1
#     for i in range(1,num+1):
#        fact=fact*i
#     return fact
# print(fact(num))

