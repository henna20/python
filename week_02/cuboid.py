length_cuboid = int(input("Enter the length of cuboid:"))
width_cuboid = int(input("Enter the width of cuboid:"))
height_cuboid = int(input("Enter the height of cuboid:"))

surface_area = 2*((length_cuboid*width_cuboid)+(width_cuboid*height_cuboid)+(length_cuboid*height_cuboid))
volume_cuboid = length_cuboid*width_cuboid*height_cuboid

print("Surface area of cuboid:" + str(surface_area))
print("Volume of cuboid:" + str(volume_cuboid))


