##take string from user and check it is pakindrome or not
# s=input("Enter a string:")
# rev=""
# for ch in s:
#     rev=ch+rev
# if s==rev:
#       print("Palindrome")
# else:
#       print("Not a Palindrome")
    
##list is given of integer compute average of all numbers in list
# list=[1,2,3,4,5,6,7]
# sum=0
# for i in list:
#     sum=i+sum
# avg=sum/len(list)
# print(avg)

##take two list of integer from user and merge them into one list and sort them
# list1=input("Enter a list integers:").split()
# list2=input("Enter a list integers:").split()
# result=[]
# for i in list1:
#     result.append(int(i))
# for i in list2:
#     result.append(int(i))
# result.sort()
# print(result)

##given a uple of integer create tuple of even and odd number
# tuple=(12,34,33,11,2,45,33,67,54)
# even=()
# odd=()
# for i in tuple:
#     if i%2==0:
#         even=even+(i,)
#     else:
#         odd=odd+(i,)
# print(even)
# print(odd)

##create code for student name and marks and update it by choice
# students = {}
# while True:
#     print("\nA. Add a student")
#     print("B. Update marks")
#     print("C. Search for a student")
#     print("D. Display all students and marks")
#     print("E. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "A":
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         students[name] = marks
#     elif choice == "B":
#         name = input("Enter student name: ")
#         if name in students:
#             marks = int(input("Enter new marks: "))
#             students[name] = marks
#         else:
#             print("Student not found")
#     elif choice == "C":
#         name = input("Enter student name: ")
#         if name in students:
#             print("Marks =", students[name])
#         else:
#             print("Student not found")
#     elif choice == "D":
#         for name, marks in students.items():
#             print(name, ":", marks)
#     elif choice == "E":
#         print("Program stopped")
#         break
#     else:
#         print("Invalid choice")


##list of words given create dictionary that maps each word with its length
# words=["apple","banana","kiwi","cherry","mango"]
# d={}
# for i in words:
#     d[i]=len(i)
# print(d)   


##takes string from user and print number of spaces in string
# s=input("Enter a string:")
# count=0
# for i in s:
#     if i==" ":
#         count+=1
# print("Number of spaces in string is",count)        


##check whether two lisis share no common element
# list1=[1,2,3,5,34]
# list2=[1,4,6,34,2]
# s1=set(list1)
# s2=set(list2)
# if s1.intersection(s2):
#     print("Common elements found")
# else:
#     print("no common elements found")


##list is given print all element that appear more than one in list
# list=[1,2,2,3,4,5,3,4,6,7,54,65,54,754,3,2,23,4342]
# dublicate=set()
# for i in list:
#     if list.count(i)>1:
#         dublicate.add(i)
# print("repeated values in list are:",dublicate)  


##take string from user and print all unique characters and count of unique characters
# string1=input("Enter a string which carries all characters:")
# unique=set()
# for i in string1:
#     if string1.count(i)<=1:
#         unique.add(i)
# print(unique)
# print(len(unique))
    

