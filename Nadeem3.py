# num = 4
# match(num):
#     case 0:
#         print("value 0")

#     case 12:
#         print("value 0")

#     case 04:
#         print("value 0")


# a = 5
# b = 10
# print (b,a)




# number = int(input("Enter the table to be print: "))




# for i in range(1, 21):
#     print(f"{number} x {i} = {number * i}")


# make 100 

# number = int(input("Enter the Dragon: "))


# for i in range(2, 101, 2):

#     if number * i == 80:
#        break 

#     print(f"{number} x {i} = {number * i}")





# cities = ["Faisalabad","Lahore","Jaranwala"]


# task 1
# cities = ["Faisalabad","Lahore","Jaranwala"]
# cities2 = []
# cities.append("Islamabad")
# cities.append("Multan")
# print(len(cities))
# print(cities)

# #Task 3
# datalist = []
# datalist.extend([10, "Chacha G ki Jhonpaari", False, 2.5])
# print(datalist)

# Task 4 create list of 10 values 
# datalist = []
# datalist.extend([10, "Jhonpaari", False, 2.5, "habro", 20,80,900, -3,-999])

# print(datalist[-2:])
# print(datalist[7:])

# # Task 2
# del cities2
# print(cities2)


# List

# cleancities = ["Lahore", "Islamabad", "Karachi", "Jaranwala", "faisalabad"]

# city = input("Enter a city name: ").lower()


# if city in cleancities:
#     print("Clean")
# else:
#     print("Not Clean")

# cleancities = ["Lahore", "Islamabad", "Karachi", "Jaranwala", "faisalabad"]

# city = input("Enter a city name: ").lower()
# for i in cleancities:
#     city2 =[i for i in cleancities if i == city]
# if city2:
#     print("Clean")
#     # break
# else:
#     print("Not Clean")


# cleancities = ["Lahore", "Islamabad", "Karachi", "Jaranwala", "Faisalabad"]

# city = input("Enter a city name: ").lower()


# city2 = [c for c in cleancities if c.lower() == city]

# if city2:
#     print(city2, "is Clean")
# else:
#     print("Not Clean")

# for loop
# fruits = ["apple", "banana", "mango", "orange"]
# user = input("Enter a fruit: ").lower()

# found = False
# for f in fruits:
#     if f == user:
#         found = True

# if found:
#     print("Yes Available")
# else:
#     print("No")

# # List comprehension

# fruits = ["apple", "banana", "mango", "orange"]
# user = input("Enter a fruit: ").lower()

# print("Yes" if [f for f in fruits if f == user] else "No")

# # animals for loop
# animals = ["dog", "cat", "lion", "tiger"]
# user = input("Enter an animal: ").lower()

# found = False
# for a in animals:
#     if a == user:
#         found = True

# if found:
#     print("Yes")
# else:
#     print("No")

# # animals list comprehension
# animals = ["dog", "cat", "lion", "tiger"]
# user = input("Enter an animal: ").lower()
# print("Yes" if [a for a in animals if a == user] else "No")


# # things comprehension
# Things =["Pen", "Pencil", "Eraser", "Sharpener", "Notebook"]
# user = input("Enter a thing: ").lower()
# print("Yes" if [t for t in Things if t == "Eraser"] else "No")

# Things =["Pen", "Pencil", "Eraser", "Sharpener", "Notebook"]
# user = input("Enter a thing: ").lower()
# if user in Things:
#     print("Yes Available")
# else:
#     print("No") 


# vehicles = ["car", "bike", "bus", "truck"]
# user = input("Enter a vehicle: ").lower()

# print("Yes" if [v for v in vehicles if v == user] else "No")


# vehicles = ["car", "bike", "bus", "truck"]
# user = input("Enter a vehicle: ").lower()

# found = False
# for v in vehicles:
#     if v == user:
#         found = True

# if found:
#     print("Yes")
# else:
#     print("No")

#  find even number 

# Even= [0,2,4,6,8,10]
# user = input("enter even number")
# print("even" if [e for e in Even if e == user] else "not even")


# tup = ("atif",)
# print(tup, type(tup))

# tup = ("atif","Nadeem", "Aslam")
# # print(len,(tup))

# print(tup[1:2])

# tup = ("car", "bike", "bus", "truck")
# user = input("Enter a vehicle: ").lower()
# # print("Yes" if [v for v in tup if v == user] else "No")

# print("yes found" if user in tup else "not found")


# Percentage fall 
# tup = ("English", "Urdu", "Maths", "Physics", "Biology", "Chemistry")
# Eng = int(input("Enter a English: "))
# urdu = int(input("Enter a Urdu: "))
# Maths = int (input("Enter a Maths: "))
# Phy = int (input("Enter a Physics: "))
# Bio = int(input("Enter a Biology: "))
# Chem = int(input("Enter a Chemistry: "))
# Per= float((Eng+urdu+Maths+Phy+Bio+Chem)/600*(100))
# print("Percentage = ", round(Per, 2), "%")


tup = ("English", "Urdu", "Maths", "Physics", "Biology", "Chemistry")
Eng = int(input("Enter a English: "))
urdu = int(input("Enter a Urdu: "))
Maths = int (input("Enter a Maths: "))
Phy = int (input("Enter a Physics: "))
Bio = int(input("Enter a Biology: "))
Chem = int(input("Enter a Chemistry: "))
Per= float((Eng+urdu+Maths+Phy+Bio+Chem)/600*(100))
print("Percentage = ", Per , "%")

print("Grade A Outstanding" if Per >= 90 else "Grade B Good" 
      if Per >= 80 else "Grade C Average" if Per >= 70 else "Grade D Poor" 
      if Per >= 60 else "Grade F Fail Better Luck Next Time")