#Import Turtle graphics module
import turtle
#Import random module to generate food at random position
import random

#define program constants
WIDTH = 800
HEIGHT = 600
DELAY = 100 # milliseconds between screen updates
FOOD_SIZE = 32 #10 pixels dot to be as food
SNAKE_SIZE=20

offset={
    "up":(0,SNAKE_SIZE),
    "down":(0,-SNAKE_SIZE),
    "left":(-SNAKE_SIZE,0),
    "right":(SNAKE_SIZE,0)
}

#Highscore feature to the game
highscore=0

#load the highscore if it exists
try:
    with open("high_score.txt","r") as file:
        highscore=int(file.read())
except IOError:
    pass

def update_high_score():
    global highscore
    if score>highscore:
        highscore=score
        with open("high_score.txt","w") as file:
            file.write(str(highscore))

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"),"Up")
    screen.onkey(lambda: set_snake_direction("down"),"Down")
    screen.onkey(lambda: set_snake_direction("right"),"Right")
    screen.onkey(lambda: set_snake_direction("left"),"Left")

def set_snake_direction(direction):
    global snake_direction
    if direction=="up":
        if snake_direction!="down": #No self-collision simply by pressing the wrong key
            snake_direction="up"
    elif direction=="down":
        if snake_direction!="up":
            snake_direction="down"
    elif direction=="left":
        if snake_direction!="right":
          snake_direction="left"
    elif direction=="right":
        if snake_direction!="left":
            snake_direction="right"


def game_loop(): #move_snake
    stamp.clearstamps() #Remove existing stamps made by stamper
    # new_head = snake[-1].copy() #copy so you don't modify the original
    new_head = list(snake[-1])
    # new_head[0] += 1 
    # Modify the new head
    new_head[0]+=offset[snake_direction][0]
    new_head[1]+=offset[snake_direction][1]

    #Check for collisions with itself and all four sides of wall
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 or \
    new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2:
        reset() #end the program
    else :
        #Add new head to the snake body
        snake.append(new_head)
        if not food_collision(): #keep the length same unless fed
            #Remove last element of the snake
            snake.pop(0)
        
        stamp.shape("assets/snake-head-20x20.gif")
        stamp.goto(snake[-1][0],snake[-1][1]) #Place the image in the head segment of the list
        stamp.stamp()
        stamp.shape("circle")
        for segment in snake[:-1]: #Head is from right to left, negative indices in python take you from the end of the list
            stamp.goto(segment[0],segment[1]) #x,y co-ordinates
            stamp.stamp()
        #Refresh the screen, Render
        screen.title("Classic Snake Game Score: {} High Score {}".format(score, highscore))
        screen.update()
        #Rinse and repeat
        turtle.ontimer(game_loop,DELAY) #specify which function is to be called i.e., calls itself in a timer

def food_collision():
    global food_pos, score
    if get_distance(snake[-1],food_pos)<20:
        score+=1
        update_high_score()
        food_pos=get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(-WIDTH/2 + FOOD_SIZE, WIDTH/2 -FOOD_SIZE) #lower bound for randint - left wall, upper bound - right wall 
    y = random.randint(-HEIGHT/2 + FOOD_SIZE, HEIGHT/2-FOOD_SIZE) #lower bound for randint - bottom wall, upper bound - upper wall
    return (x,y)

def get_distance(pos1,pos2):
    x1,y1=pos1
    x2,y2=pos2
    distance = ((x2-x1)**2 + (y2-y1)**2 ) ** 0.5
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    score =0
    #Create snake as a list of coordinate pairs
    snake = [[0,0],[SNAKE_SIZE,0],[SNAKE_SIZE*2,0],[SNAKE_SIZE*3,0]]
    snake_direction="up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    #set animation in motion
    game_loop()

# Create a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Classic Snake Game")
screen.bgpic("assets/bg2.gif")
screen.register_shape("assets/snake-food-32x32.gif")
screen.register_shape("assets/snake-head-20x20.gif")
screen.tracer(0) #Turn off automatic animation

#Event Handlers
screen.listen()
bind_direction_keys()

# Create a turtle to do your bidding
stamp=turtle.Turtle()
stamp.shape("circle")
stamp.color("#009ef1")
stamp.penup()

#Draw snake for the first time
# for segment in snake:
#     stamp.goto(segment[0],segment[1]) #x,y co-ordinates
#     stamp.stamp()

#Food creation
food = turtle.Turtle()
food.shape("assets/snake-food-32x32.gif")
# food.shape("square")
# food.color("black")
food.shapesize(FOOD_SIZE/20)
food.penup()

#set things in motion
reset()

# below statement needed at the end of all turtle programs
turtle.done()

