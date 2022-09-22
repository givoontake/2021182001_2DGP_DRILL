from pico2d import *

open_canvas()

grass = load_image('white.png')
character = load_image('run.png')

x = 0
frame = 0
while (x < 900):
    clear_canvas()
    grass.draw(400, 300)
    character.clip_draw(frame * 120, 0,  120, 120, x, 60)
    update_canvas()
    frame = (frame + 1) % 10

    x += 20
    delay(0.05)
    get_events()

close_canvas()

