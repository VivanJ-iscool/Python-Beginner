import turtle
sam = turtle.Turtle()
sam.shape ("turtle")

print("enter 1 for triangle\nenter 2 for square\nenter 3 for circle ")
shape = input("Chose which shape you like 1,2 or 3: ")

if shape == "1":
    l = int(input("enter lenght of your square: "))
    for i in range(4):
        sam.forward(l)
        sam.left(90)

elif shape == "2":
    l = int(input("enter lenght of your triangle: "))
    for i in range(3):
        sam.forward(l)
        sam.left(120)

elif shape == "3":
    r = int(input("enter radius of your circle: "))
    sam.circle(r)

else:
    print("Pick between 1,2,3 ")


print("enter 1 for red\nenter 2 for blue\nenter 3 for yellow ")
fill_color = int(input("Choose a color: "))

if fill_color == 1:
    sam.fillcolor("red")
elif fill_color == 2:
    sam.fillcolor("blue")
elif fill_color == 3:
    sam.fillcolor("yellow")

print("Think of a polygon")
side_of_shape = int(input("How many sides does your shape have?"))
lenght = float(input("How long is each side"))

for i in range(side_of_shape):
    sam.forward(lenght)
    sam.left(360/side_of_shape)

sam.end_fill()


