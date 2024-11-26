# code credit: https://www.geeksforgeeks.org/turtle-race-game-using-python-turtle-graphics-library/

from record_game import record_game_data


import random
from turtle import Turtle, Screen

Race = False

s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Make your Bet", prompt="Which turtle which win ? Enter Color : ")
X = -230
Y = -100
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
if bet not in colors:
    print(f"Invalid input: '{bet}'. Please enter one of the following colors: {', '.join(colors)}")
    exit()


turtles = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=X, y=-100 + 50 * i)
    turtles.append(t)

if bet:
    Race = True

while Race:

    for turtle in turtles:

        if turtle.xcor() >= 230:
            Race = False
            winning = turtle.pencolor()
            if winning == bet:
                print(f"You have Won the bet on {winning} turtle! The {winning} is the winner")
            else:
                print(f"You lose! {winning} turtle is the winner")

            record_game_data(bet, winning)


        distance = random.randint(0, 10)
        turtle.forward(distance)

s.exitonclick()
