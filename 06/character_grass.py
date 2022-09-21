from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

delay(1)

while(True):
    x=400
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)

    y=30
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y=y+2
        delay(0.01)

    x=800
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x=x-2
        delay(0.01)

    y=600
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y=y-2
        delay(0.01)

    x=0
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)

close_canvas()
