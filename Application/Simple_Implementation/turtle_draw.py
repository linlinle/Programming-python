# -*- coding: utf-8 -*-
'''利用turtle实现移动画图'''
import turtle # 乌龟

def draw_square(turtle_name):
    for i in range(1,5):
        turtle_name.forward(100)
        turtle_name.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(10)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

    window.exitonclick()

draw_art()