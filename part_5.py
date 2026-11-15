##file operations
# f=open("sample.txt","r")
# data=f.read()
# print(data)

# f=open("sample.txt","r")
# data=f.readline()
# print(data)
# f.close()

# f=open("sample.txt","w")
# f.write("1234")
# f.close()

# f=open("sample.txt","a")
# data=f.write("\nhappy birthday tanmay")
# print(data)
# f.close()

# f=open("sample2.txt","x")
# data=f.write("hi hello how are you")
# print(data)
# f.close()

# f=open("sample.txt","a+")
# f.write("happy suraj")
# print(f.read())
# f.close()

##with keyword
# with open("sample.txt","r") as f:
#     data=f.read()
#     print(len(data))

##delete files
# import os
# os.remove("sample2.txt")

##word search practice problem
# data=True
# line=1
# word="blinkit"
# with open("sample.txt","r") as f:
#     while data:
#         data=f.readline()
#         if(word in data):
#             print(word,"found at line",line)
#             break
#         line+=1

##exception handling
# try:
#     x=int(input("enter x:"))
#     ans=10/x
# except ZeroDivisionError:
#     print("divide by 0 is not allowed")
# except ValueError:
#     print("Invalid input")
# else:
#     print("ans=",ans)
# finally:
#     print("End of program")

##list comprehensions
# sq=[i*i for i in range(10)]
# print(sq)

# nums=[-3,2,-1,-2,5,3]
# nums=[0 if val<0 else val for val in nums]
# print(nums)

# words=["hello","python","apnacollege"]
# words=[val.upper() for val in words]
# print(words)

##working with java script object notation(json) module
# import json
# json_str='{"name":"Shradha","isTeacher":true}'
# py_obj=json.loads(json_str)
# print(type(py_obj),py_obj)

# import json
# py_obj={"name":"Shradha","isTeacher":True}
# json_str=json.dumps(py_obj)
# print(type(json_str),json_str)

# import json
# with open("data.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)

# import json
# data={"name":"Shradha","age":27,"isTeacher":True}
# with open("data.json","w") as f:
#     json.dump(data,f,indent=4,sort_keys=True)





