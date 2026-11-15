##strings in python
# word="Python"
# print(len(word))

# word1="i love"
# word2="python"
# print(word1+" "+word2)

# word="python"
# for ch in word:
#     print(ch)

##slicing in string
# word="python"
# print(word[2:len(word)])
# print(word[-4:len(word)-1])

##string formatting
# a=2
# b=5
# print(f"avg of {a} and {b} is {a+b/2}")

##list in python with methods
# list=[344,2345,23,134.23]
# list.append(245)
# print(list)
# list.insert(2,2123)
# print(list)
# list.sort()
# print(list)

##using for loop with list
# list=[12,2223,2,3,2,12]
# for val in list:
#     print(val)

# list=[1,2,4,23,134,3,33]
# x=134
# index=0
# for val in list:
#     if val==x:
#         print(index)
#         break
#     index+=1

##tuples in python
# tuple=(92,34,234,2,341)
# sum=0
# for val in tuple:
#     sum+=val
# print(sum)

##dictionary in python
# info={"name":"Suraj","age":19,"sub":"python"}
# print(info["name"])
# info["age"]=22
# print(info["age"])

##sets in python
# set={1,2,23,2,23,24}
# print(set)
# print(len(set))
# set.add(45)
# print(set)
# set.pop()
# print(set)

# s1={1,3,4,5,2,6}
# s2={2,4,7,8,4}
# print(s1.union(s2))
# print(s1.intersection(s2))

##given list of tuples with info(name,subject) in that list all unique code and list students enrolled in english and create dictionary(student,set of courses)
# info=[("Alice","Maths"),("Bob","Science"),("Alice","Science"),("Charlie","Maths"),("Bob","Maths"),("Alice","English"),("Charlie","English")]
# unique_courses=set()
# for tup in info:
#          unique_courses.add(tup[1])
# print(unique_courses)        

# info=[("Alice","Maths"),("Bob","Science"),("Alice","Science"),("Charlie","Maths"),("Bob","Maths"),("Alice","English"),("Charlie","English")]
# for name,course in info:
#         if course=="English":
#                 print(name)

# info=[("Alice","Maths"),("Bob","Science"),("Alice","Science"),("Charlie","Maths"),("Bob","Maths"),("Alice","English"),("Charlie","English")]
# dict={}
# for name,courses in info:
#     if (dict.get(name)==None):
#         dict.update({name:set()})
#         dict[name].add(courses)
#     else:
#         dict[name].add(courses)
# print(dict)



