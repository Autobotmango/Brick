from cmu_graphics import *

app.background = 'black'
# creates a ball
ball = Circle(20,180,10,fill='white')
# setting ball speed
ball.dx = 7
ball.dy = 7
# creating boundries
bottom = Rect(0,400,400,1)
top = Rect(0,0,400,1)
left = Rect(0,0,1,400)
right = Rect(400,0,1,400)
# draws a grey bar for the player to control
bar = Rect(144,360,80,20,fill='grey')
# creates group for the bricks
row = Group()
# defines the level and lives
level = Label(1,401,401)
lives = Label(3,46,6, fill='white')
Label('Lives:',23,6, fill='white')
# ends the game
def gameEnd(state):
    app.stop()
    Rect(80,170,240,20)
    if(state == 'win'):
        Label('You Win!',200,200,fill='white',size=60)
    else:
        Label('Game Over!',200,200,fill='white',size=60)
# resets ball
def resetBall():
    ball.centerX = 20
    ball.centerY = 180
    ball.dx = 5 + (level.value *2)
    ball.dy = 5 + (level.value *2)
# makes a new row of bricks
def nextLevel():
    level.value += 1
    lives.value += 1
    makeRow(level.value)
    resetBall()
# makes a row of bricks
def makeRow(level):
    for x in range(7):
        for y in range(level+1):
            brick = Rect(x*60,20+(y*30),50,20,fill=rgb(255,0,0))
            row.add(brick)
# creates the bricks to break
makeRow(1)
def onStep():
# moves the ball according to defined speed
    ball.centerX += ball.dx
    ball.centerY += ball.dy
    bar.centerX = ball.centerX
# bounces ball when it hits left, top, and right sides
    if(ball.hitsShape(bottom)):
        resetBall()
        lives.value -= 1
    if((ball.hitsShape(bar)) or (ball.hitsShape(top))):
        ball.dy = -ball.dy
    if((ball.hitsShape(left)) or (ball.hitsShape(right))):
        ball.dx = -ball.dx
    # stops app when out of lives
    if(lives.value == 0):
        gameEnd('lose')
#removes a brick when hit and moves the ball accordingly and sets color of rows
    for brick in row.children:
        if(brick.centerY > 50):
            brick.fill="orange"
        if(brick.centerY > 80):
            brick.fill='yellow'
        if(brick.centerY > 110):
            brick.fill='limeGreen'
        if(brick.centerY > 140):
            brick.fill='cornFlowerBlue'
        if(ball.hitsShape(brick)):
            ball.dy = -ball.dy
            row.remove(brick)
# progresses the level when it has been cleared    
    if(row.children == []):
        nextLevel()
# causes a game win when level 5 is reached
    if(level.value == 5):
        gameEnd('win')
# moves the bar according to mouse position
#def onMouseMove(mouseX,mouseY):
   # bar.centerX = mouseX

def onKeyPress(key):
    if(key == 'space'):
        if(app.paused):
            app.paused = False
        else:
            app.paused = True
