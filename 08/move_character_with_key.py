from pico2d import *

def handle_events():
    global running
    global dir_x
    global dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
    pass


open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 50
frame = 0
dir_x = 0
dir_y = 0
d = 1

while running:
    clear_canvas()
    grass.draw(400, 300)
    handle_events()

    if (dir_x == 0 and dir_y != 0):
        y += dir_y * 5
    elif (dir_y == 0 and dir_x != 0):
        x += dir_x * 5

    if (x > 800):
        x -= dir_x * 5
    elif (x < 0):
        x -= dir_x * 5
    if (y > 600):
        y -= dir_y * 5
    elif (y < 0):
        y -= dir_y * 5

    if(dir_x > 0):
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        d = 1
    elif (dir_x < 0):
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        d = 0
    elif(dir_x == 0 and dir_y == 0):
        if(d == 1):
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
        elif (d == 0):
            character.clip_draw(frame * 100, 200, 100, 100, x, y)
    elif(dir_y != 0):
        if(d == 1):
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif(d == 0):
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    update_canvas()

    frame = (frame + 1) % 8
    delay(0.01)

close_canvas()
