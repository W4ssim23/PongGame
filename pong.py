import turtle
import winsound

#the value of the acceleration depends on the power of your cpu
DefaultAcceleration = 0.08

#a function that makes pabbles and ball 
def make_stuff(x : int , y : int , is_paddle : bool) -> turtle:
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    if is_paddle :
        paddle.shapesize(stretch_wid=5,stretch_len=1)
    else :
        #the same as the default acceleration
        paddle.dx = 0.08
        paddle.dy = 0.08
    paddle.penup()
    paddle.goto(x,y)
    return paddle


# a function to control the paddle
def up(paddle):
    if paddle.ycor() <= 225 :
        paddle.sety(paddle.ycor() + 20)

def down(paddle):
    if paddle.ycor() > -225 :
        paddle.sety(paddle.ycor() - 20)

def controll(paddle, button_up, button_down):
    window.listen()
    window.onkeypress(lambda: up(paddle), button_up)
    window.onkeypress(lambda: down(paddle), button_down)


#setting up the game window 
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)


#setting up paddles and the ball

paddle_a = make_stuff(-350,0,True)
paddle_b = make_stuff(350,0,True)
ball = make_stuff(0,0,False)


#setting controll for each paddle 

controll(paddle_a,"z","s")
controll(paddle_b,"Up","Down")


#setting up the score bar
a,b = (0,0)
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score.goto(0,260)
score.write(f"Player A : {a}    Player B : {b}",align=("center") , font=("Courier",24,"normal"))



while True :
    window.update()

    #ball movemen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #place check
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 
    if ball.xcor() > 390 :
        ball.setx(0)
        ball.sety(0)
        ball.dy = DefaultAcceleration
        ball.dx = - DefaultAcceleration
        a += 1
        score.clear()
        score.write(f"Player A : {a}    Player B : {b}",align=("center") , font=("Courier",24,"normal"))
    if ball.xcor() < -390 :
        ball.setx(0)
        ball.sety(0)
        ball.dy = - DefaultAcceleration
        ball.dx = DefaultAcceleration
        b += 1
        score.clear()
        score.write(f"Player A : {a}    Player B : {b}",align=("center") , font=("Courier",24,"normal"))
    if ball.xcor() > paddle_b.xcor() -10 and paddle_b.ycor() -50 < ball.ycor() < paddle_b.ycor() + 50 :
        ball.setx(paddle_b.xcor() -10)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor() < paddle_a.xcor() +10 and paddle_a.ycor() -50 < ball.ycor() < paddle_a.ycor() + 50 :
        ball.setx(paddle_a.xcor() +10)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)