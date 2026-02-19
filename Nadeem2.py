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

# table 100 even number print


# number = int(input("Enter the table to be print: "))

# for i in range(2, 21, 2):
#     print(f"{number} x {i} = {number * i}")


# number = int(input("Enter the table to be printed: "))

# for i in range(2, 21, 2):   # even numbers: 2, 4, 6, ..., 20
#     print(f"{number} x {i} = {number * i}")

n = (input("Enter the Dragon: "))
for n in range(2, 101, 2):   # even numbers from 2 to 100
    if n * n > 100:
        break
    print(f"{n}*{n}={n*n}")
    