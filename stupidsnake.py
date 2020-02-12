import turtle
import random

CELL_SIZE = 8

themap=[]
theframe=[]
for counteri in range(-1,51):
    if counteri==-1 or counteri==50:
        for counterj in range(-1,51):
            theframe.append((counteri,counterj))
    else:
        theframe.append((counteri,-1))
        theframe.append((counteri,50))
#themap=theframe[:]
themap = theframe[:] + [(20, 5),(20, 6),(20, 7),(20, 8),(20, 9),(20, 10),(20, 44),(20, 43),(20 ,42),(20, 41),(20, 40),(20, 39),(20, 38),(20, 37),(20, 36),(20, 35),(20, 11),(20, 12),(20, 13),(20 ,14),(20, 15)]

class LifeBoardsnake:
    "Game of Life board, a rectangular board with live and dead cells"

    def __init__(self, width, height):
        "Create a new Game of Life board of specified size."
        self.body = []
        self.width, self.height = width, height
        self.head=(2,2)
        self.food=(8,8)
        self.generator=0
        self.direction=None
        self.switch=1
        
        ##############################################################################
        mapdrawer= turtle.Turtle()
        mapdrawer.hideturtle()
        mapdrawer.clear()
        mapdrawer.color('red')
        mapdrawer.setheading(0)
        for [x, y] in themap:
            mapdrawer.penup()
            mapdrawer.setpos(x * CELL_SIZE, y * CELL_SIZE)
            mapdrawer.pendown()
            mapdrawer.begin_fill()
            for i in range(4):
                mapdrawer.forward(CELL_SIZE - 1)
                mapdrawer.left(90)
            mapdrawer.end_fill()
        mapdrawer.penup()
        turtle.update()
        ##############################################################################
        
    def newfood(self):
        "Fill the board with a random pattern"
        if self.generator==1:
            j, k = random.randint(0,self.width), random.randint(0,self.height)
            if (j,k) in self.body or (j,k)==self.head or (j,k) in themap:
                self.newfood()
            else:
                self.food=(j,k)
                self.generator=0
    
    #def eatfood(self):
        #return self.head==self.food

    def a(self):
        if self.direction!='right' and self.direction!='left': self.direction='left'
    def d(self):
        if self.direction!='right' and self.direction!='left': self.direction='right'
    def s(self):
        if self.direction!='up' and self.direction!='down': self.direction='down'
    def w(self):
        if self.direction!='up' and self.direction!='down': self.direction='up'
    def q(self):#######
        turtle.bye()##############
    def step(self):
        "Compute the next generation according to Conway's rule."
        ###########
        if self.head in self.body or self.head in themap:
            self.switch=0
        #############
        #if self.head in self.body or self.head[0]<0 or self.head[0]>=self.width or \
        #self.head[1]<0 or self.head[1]>=self.height:
        #    self.switch=0
        self.body.insert(0,self.head)
        if self.direction=='up':
            self.head=(self.head[0],self.head[1]+1)
        if self.direction=='down':
            self.head=(self.head[0],self.head[1]-1)
        if self.direction=='left':
            self.head=(self.head[0]-1,self.head[1])
        if self.direction=='right':
            self.head=(self.head[0]+1,self.head[1])
        if self.head==self.food:
            self.generator =1
        else:
            self.body.remove(self.body[-1])
    
    def display(self):
        "Draw the whole board"
        turtle.clear()
        turtle.color('black')
        turtle.setheading(0)
        for [x, y] in self.body:
            turtle.penup()
            turtle.setpos(x * CELL_SIZE, y * CELL_SIZE)
            turtle.pendown()
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE - 1)
                turtle.left(90)
            turtle.end_fill()
        turtle.penup()
        turtle.setpos(self.head[0] * CELL_SIZE, self.head[1] * CELL_SIZE)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(CELL_SIZE - 1)
            turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.setpos(self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(CELL_SIZE - 1)
            turtle.left(90)
        turtle.end_fill()
        turtle.update()

def main():
    # set up window
    #######
    #screen = turtle.Screen()
    #############
    turtle.screensize(400,420,'white')
    width, height = 400,400
    turtle.setworldcoordinates(0, -20, width, height)
    turtle.title('Game of Snake')

    # write instructions
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.setposition(5, -15)
    writer.write("W)move to upsite   S)move to downsite   A)move to leftsite\
        D)move to rightsite    Q)uit", font=('sans-serif', 14, 'normal'))    

    # set up board
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0) # turn off animation; update() needs to be called
    board = LifeBoardsnake(width // CELL_SIZE, height // CELL_SIZE)
    #board.makeRandom()
    board.display()


    # set up key bindings
    def w():
        board.w()
    turtle.onkey(w, 'w')
    def a():
        board.a()
    turtle.onkey(a, 'a')
    def s():
        board.s()
    turtle.onkey(s, 's')
    def d():
        board.d()
    turtle.onkey(d, 'd')
    turtle.onkey(turtle.bye, 'q')

    def perform_step():
        board.step()
        board.newfood()
        board.display()
        if board.switch==1:
            turtle.ontimer(perform_step, 200)# do again after 25 ms
        else:
            writer.penup()
            writer.pencolor('brown')
            writer.clear()
            writer.setposition(80,100)
            writer.write("GAME OVER", font=('sans-serif', 72, 'normal'))
            writer.penup()
            writer.setposition(145,45)
            writer.write('Press (Q) to quit\nPress (Z) to replay', font=('sans-serif', 18, 'normal'))
    perform_step()
    
    def newgame():
        if board.switch==0:
            writer.clear()
            writer.pencolor('black')
            writer.penup()
            writer.setposition(5, -15)
            writer.write("W)move to upsite   S)move to downsite   A)move to leftsite\
            D)move to rightsite    Q)uit", font=('sans-serif', 14, 'normal'))
            board.__init__(width // CELL_SIZE, height // CELL_SIZE)
            perform_step()
    turtle.onkey(newgame,'z')
    # set focus on screen and enter the main loop
    turtle.listen()
    turtle.mainloop()
main() 
