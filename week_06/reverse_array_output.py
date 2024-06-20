a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))
e = int(input("Enter the fifth number:"))

arr = [str(a), str(b), str(c), str(d), str(e)]

print("Array is :",arr)

res = arr[::-1]  #reversing using list slicing
print("Resultant new reversed array:",res)
