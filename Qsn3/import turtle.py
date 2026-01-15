import turtle

# Recursive edge function
def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)
        turtle.left(120)
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)

def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.left(angle)

# User input
sides = int(input("Enter the number of sides: "))
length = float(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

# Turtle setup
turtle.speed(0)
turtle.hideturtle()

# Draw pattern
draw_polygon(sides, length, depth)

turtle.done()
