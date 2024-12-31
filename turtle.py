import turtle

# Create turtle and screen objects
t = turtle.Turtle()
s = turtle.Screen()

# Set screen and turtle properties
s.bgcolor("black")
t.width(2)
t.speed(0)  # Set to fastest drawing speed

# Define color palette
col = ('white', 'pink', 'cyan')

# Drawing loop
for i in range(300):
    t.pencolor(col[i % len(col)])  # Ensure safe indexing
    t.forward(i * 4)
    t.right(121)

# Keep the window open until the user closes it
turtle.done()
