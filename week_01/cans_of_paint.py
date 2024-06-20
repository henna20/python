length_of_wall = 40
width_of_wall = 30
height_of_wall = 3.4
surface_area_of_wall = (2*length_of_wall*height_of_wall) + (2*width_of_wall*height_of_wall)
each_can_of_paint_covers = 5.1
cans_required = surface_area_of_wall/each_can_of_paint_covers
if(cans_required % 2) == 0:
    print("Number of cans required: " + str(cans_required))
else:
    print("Number of cans required: " + str(int(cans_required) + 1))


diameter_can = 15
height_can = 30

length_box = 60
width_box = 30
height_box = 35

long = length_box/diameter_can
wide = width_box/diameter_can
height = height_box/height_can

# Number of cans in box:
x = int(long)*int(wide)*int(height)
print("Number of cans in box:" + str(int(x)))

# Number of full boxes:
y = cans_required/x
print("Number of full boxes:" + str(int(y)))

# Number of full boxes:
if(cans_required % 2) == 0:
    z = cans_required % x
    print("Cans not packed in boxes:" + str(int(z)))

else:
    z = (int(cans_required) + 1) % x
    print("Cans not packed in boxes:" + str(int(z)))







