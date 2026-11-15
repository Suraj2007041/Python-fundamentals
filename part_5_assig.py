##open file in write mode write 5 names by user and then open same file in read mode and print all names
# with open("names.txt","w") as file:
#     for i in range(5):
#         name=input("Enter name"+str(i+1)+":")
#         file.write(name + "\n")
# with open("names.txt","r") as file:
#     print("\nNames in file:")
#     for name in file:
#         print(name.strip())

##open file in append mode adds new log entry and open file in read mode and print log
# with open("log.txt","a") as file:
#     file.write("Program run successfully\n")
# with open("log.txt","r") as file:
#     print("All Logs:")
#     for log in file:
#         print(log.strip())


##use list comprehension to create a new list with no greater than 15 print new list
# nums=[5,10,15,20,25]
# nums=[0 if val<15 else val for val in nums]
# print(nums)

##create python dictionary of 3 cities and their population save in cities file then load json and print cities with population and ask user for new cities and population and update it in file
# import json
# with open("cities.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)
# city=input("Enter city name:")
# population=int(input("Enter population:"))
# py_obj[city]=population
# with open("cities.json","w") as f:
#     json.dump(py_obj,f,indent=4)
# print("city data updated successfully!")
# for city, population in py_obj.items():
#     print(city,":",population)

##write program that tries to open file in read mode if file not exist catch exception and print file not found
# try:
#     file=open("data.txt","r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("File not found!")
