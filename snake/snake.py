from turtle import Turtle
start_positions = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self):
        #ukuran 20x20 pixel
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in start_positions:
            self.add_body(position)
    
    def add_body(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snakes.append(body)

    def extend(self):
        #menambahkan badan baru pada list ular dengan posisi yang sama dengan posisi badan terakhir
        self.add_body(self.snakes[-1].position())


    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def move(self):
        for body_num in range(len(self.snakes) - 1, 0, -1):
            #buat variabel untuk menampung posisi badan di depan
            new_x = self.snakes[body_num - 1].xcor()
            new_y = self.snakes[body_num - 1].ycor()
            self.snakes[body_num].goto(new_x,new_y)
        self.head.forward(20)