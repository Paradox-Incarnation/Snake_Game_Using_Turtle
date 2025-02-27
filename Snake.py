from turtle import Turtle

class Snake:
    def __init__(self):
        self.Squares = []
        self.create_snake(3)
        self.head = self.Squares[0]
        self.head.color("yellow")
        self.current_direction = "right"  
        self.next_direction = "right"     
    
    def create_snake(self, n):
        pos_init = 0
        for i in range(n):
            Turtle_Object = Turtle("square")
            Turtle_Object.color("white")
            Turtle_Object.penup()
            Turtle_Object.goto(pos_init, 0)
            self.Squares.append(Turtle_Object)
            pos_init -= 21
            
    
    def add_segment(self):
        last_segment = self.Squares[-1]
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_segment.position())
        self.Squares.append(new_segment)
    
    def following(self):
        # First update the positions of all segments
        for i in range(len(self.Squares) - 1, 0, -1):
            self.Squares[i].goto(self.Squares[i-1].pos())
        
        # Now update the direction only once per game loop
        self.current_direction = self.next_direction
        
        # Set the actual heading based on current_direction
        if self.current_direction == "up":
            self.head.setheading(90)
        elif self.current_direction == "down":
            self.head.setheading(270)
        elif self.current_direction == "left":
            self.head.setheading(180)
        elif self.current_direction == "right":
            self.head.setheading(0)
        
        self.head.fd(21)
    
    def up(self):
        if self.current_direction != "down":
            self.next_direction = "up"
            
    def down(self):
        if self.current_direction != "up":
            self.next_direction = "down"
            
    def left(self):
        if self.current_direction != "right":
            self.next_direction = "left"
            
    def right(self):
        if self.current_direction != "left":
            self.next_direction = "right"