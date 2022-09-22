from pico2d import *

open_canvas()

grass = load_image('white.png')
character = load_image('g_run.png')

while(True):
    frame = 0
    # 앞으로 가는 부분
    for x in range(0, 30):
        clear_canvas()
        grass.draw(400, 300)
        character.clip_draw(frame * 63, 0, 63, 60, 30, 60)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.05)
        get_events()

    frame = 0
    x = 30
    # 오른쪽으로 가는 부분
    while (x < 751):
        clear_canvas()
        grass.draw(400, 300)
        character.clip_draw(10 + frame * 63, 61, 63, 60, x, 60)
        update_canvas()
        frame = (frame + 1) % 8
        x += 10
        delay(0.05)
        get_events()

    frame = 0
    # 뒤로 오는 부분
    for x in range(0, 30):
        clear_canvas()
        grass.draw(400, 300)
        character.clip_draw(5 + frame * 63, 188, 63, 62, 750, 60)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.05)
        get_events()

    frame = 0
    x = 750

    # 왼쪽으로 가는 부분
    while (x > 29):
        clear_canvas()
        grass.draw(400, 300)
        character.clip_draw(6 + frame * 63, 123, 63, 61, x, 60)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 10
        delay(0.05)
        get_events()

close_canvas()

