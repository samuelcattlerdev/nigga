import turtle
import time

# Configurar la pantalla
screen = turtle.Screen()
screen.bgcolor("black")

# Crear el lápiz para dibujar el corazón
pen = turtle.Turtle()
pen.speed(3)
pen.width(3)
pen.color("red")

def draw_heart():
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    
    pen.begin_fill()
    pen.fillcolor("red")
    
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Dibujar el corazón
draw_heart()

# Escribir mensaje
pen.penup()
pen.goto(-90, 20)
pen.color("white")
pen.write("Te amo, mi amor!", font=("Arial", 18, "bold"))

pen.goto(-80, -10)
pen.write("Eres la mejor mujer del mundo!", font=("Arial", 14, "italic"))

# Ocultar la tortuga y esperar antes de cerrar
pen.hideturtle()

time.sleep(5)
screen.bye()
