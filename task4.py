#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

radius = input("please enter the value of height")
height = input("please enter the value of radius")
radius = int(radius)
height = int(height)
sh = ((height**2+radius**2)**0.5)
sa = (3.14159265359*height*(height+sh))
print(f"so the surface area is {sa}")