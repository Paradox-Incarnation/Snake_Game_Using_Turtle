from turtle import Turtle,Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import json
import os

#Screen Settings
Screen_Object=Screen()
Screen_Object.setup(width=1.0,height=1.0)
Screen_Object.bgcolor("black")
Screen_Object.title("Paradox's Snake Game")

Screen_Object.tracer(0)
strip_colour=Turtle()
strip_colour.hideturtle()
strip_colour.color("grey")
strip_colour.penup()

strip_colour.goto(-350,300)
strip_colour.pendown()
strip_colour.begin_fill()
for _ in range(2):
    strip_colour.forward(700)
    strip_colour.right(90)
    strip_colour.forward(35)
    strip_colour.right(90)
strip_colour.penup()
strip_colour.goto(-350,300)
strip_colour.pendown()
for _ in range(2):
    strip_colour.fd(700)
    strip_colour.right(90)
    strip_colour.fd(600)
    strip_colour.right(90)
Snake_Object=Snake()
Food_Object=Food()
Score_Object=Scoreboard()
leaderboard_path = "Python/Course/Course_Day20/Leaderboard.json"
if os.path.exists(leaderboard_path):
    try:
        with open(leaderboard_path, "r") as file:
            leaderboard = json.load(file)
    except json.JSONDecodeError:
        leaderboard = []
else:
    leaderboard = []

Name = Screen_Object.textinput("Player Name", "Enter Your Name:")
if Name is None:
    Name = "Paradox"  
Screen_Object.delay(2)
Screen_Object.listen()
Screen_Object.onkey(Snake_Object.up,"Up")
Screen_Object.onkey(Snake_Object.down,"Down")
Screen_Object.onkey(Snake_Object.left,"Left")
Screen_Object.onkey(Snake_Object.right,"Right")

Screen_Object.update()
Score_Object.update_display()
game_is_on=True
while game_is_on: 
    Screen_Object.update()
    if (Score_Object.score<5):
          time.sleep(0.1)
    elif (Score_Object.score>=5 and Score_Object.score<10):
          time.sleep(0.09)
    elif (Score_Object.score>=10 and Score_Object.score<15):
          time.sleep(0.08)
    elif (Score_Object.score>=15 and Score_Object.score<20):
          time.sleep(0.07)
    else:
          time.sleep(0.05)


       
    Snake_Object.following()

    if Snake_Object.head.distance(Food_Object) < 15:
        Food_Object.refresh()
        Score_Object.increase_score()
        Snake_Object.add_segment()
    if Snake_Object.head.xcor()>340 or Snake_Object.head.xcor()<-350 or Snake_Object.head.ycor()<-300 or Snake_Object.head.ycor()>300:
        Score_Object.game_over()
        game_is_on=False
    for segment in Snake_Object.Squares:
        if Snake_Object.head==segment:
            pass
        elif Snake_Object.head.distance(segment)<10:
            Score_Object.game_over()
            game_is_on=False
            print("Error")
 
try:
    leaderboard.append({"Name": Name, "Score": Score_Object.score})
    
    leaderboard.sort(key=lambda x: x["Score"], reverse=True)
    
    leaderboard = leaderboard[:10]
    
    with open(leaderboard_path, "w") as file:
        json.dump(leaderboard, file, indent=4)
        
    print("\nLeaderboard:")
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['Name']}: {entry['Score']}")
except Exception as e:
    print(f"Error saving score: {e}")



Screen_Object.mainloop()