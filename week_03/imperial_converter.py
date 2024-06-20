feet = int(input("Feet: "))
inches = int(input("Inches: "))
x = feet / 3280.84
y = inches / 39370.1
km = x + y
print("Height in kilometres:", round(km, 6))
m = km * 1000
print("Height in metres:", round(m, 4))
cm = m * 100
print("Height in centimetres:", round(cm, 4))
mm = cm * 10
print("Height in millimetres:", round(mm, 2))

