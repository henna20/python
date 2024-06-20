import math
from tabulate import tabulate

i = int(input("Enter a positive integer number of seconds:"))

if i >= 0:
    print("")
else:
    print("Invalid number")

hours = i / 3600
x = math.modf(hours)
min = list(x)[0]
minute = min * 60
y = math.modf(minute)
sec = list(y)[0]
second = sec * 60
mydata = [["Input", "Hours", "Minutes", "Seconds"],
          [str(int(i)),  str(int(hours)),  str(round(minute)),  str(round(second))]
          ]
print(tabulate(mydata))


