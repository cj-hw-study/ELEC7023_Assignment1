# Assignment One
# Name: CHEN Ji

import turtle

# Task A: Turtle Drawing
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colourful Turtle Drawing")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

colors = ["red", "orange", "yellow", "green",
          "cyan", "blue", "purple", "pink"]

for i in range(120):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(40 + i * 2)
    pen.right(144)

pen.hideturtle()
screen.exitonclick()

# Task B: Question Answering Bot

print("Welcome to the QA Bot!")
print("You can ask me about HKU, robot, jetson, ai, or human.")
print("Type 'exit' to quit.")

while True:
    question = input("Ask me something: ").lower()

    if question == "exit":
        print("Bot: Goodbye!")
        break
    elif "hku" in question:
        print("Bot: HKU stands for the University of Hong Kong.")
    elif "robot" in question:
        print("Bot: A robot is a machine that can perform tasks automatically.")
    elif "jetson" in question:
        print("Bot: Jetson Nano is a small computer used for AI applications.")
    elif "ai" in question:
        print("Bot: AI stands for Artificial Intelligence.")
    elif "human" in question:
        print("Bot: Humans can think, learn, and make decisions.")
    else:
        print("Bot: Sorry, I don't understand your question.")
