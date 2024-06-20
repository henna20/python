u = int(input("Enter the Initial velocity(u):"))
t = int(input("Enter the Time Taken(t):"))
a = int(input("Enter the acceleration(a):"))

s = (u * t) + (1 / 2 * (a * t ** 2))

print("------Calculate the distance-------")
print("The total distance is:" + str(int(s)), "meters")

