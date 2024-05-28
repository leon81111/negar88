import turtle
import random

# تنظیمات بازی
wn = turtle.Screen()
wn.title("Turtle Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)
wn.tracer(0)

# امتیاز کاربر و تایمر و جون‌ها
score = 0
lives = 3

# ایجاد لاک‌پشت
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# ایجاد غذا
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# نمایش اطلاعات
info_pen = turtle.Turtle()
info_pen.speed(0)
info_pen.color("black")
info_pen.penup()
info_pen.hideturtle()
info_pen.goto(0, 260)
info_pen.write("Score: {} Lives: {}".format(score, "❤️" * lives), align="center", font=("Courier", 24, "normal"))

# حرکت لاک‌پشت
def go_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def go_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def go_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def go_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# مدیریت حرکت با کلید‌های جهتی
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# حلقه اصلی بازی
while True:
    wn.update()

    # اگر لاک‌پشت و غذا برخورد کنند
    if player.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        score += 1
        info_pen.clear()
        info_pen.write("Score: {} Lives: {}".format(score, "❤️" * lives), align="center", font=("Courier", 24, "normal"))

    # بررسی بیرون رفتن از کادر
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        lives -= 1
        player.goto(0, 0)
        info_pen.clear()
        info_pen.write("Score: {} Lives: {}".format(score, "❤️" * lives), align="center", font=("Courier", 24, "normal"))

        # اگر جون تموم شد، بازی تموم می‌شه
        if lives == 0:
            info_pen.clear()
            info_pen.write("Game Over! Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            break

wn.mainloop()
