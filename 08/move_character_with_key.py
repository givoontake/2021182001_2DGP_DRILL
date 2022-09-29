from pico2d import *

right = False
left = False
up = False
down = False
def handle_events():
    global running
    global dir
    global dir2
    global right
    global left
    global up
    global down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                right = True
                left = False
                up = False
                down = False
                dir += 1
            elif event.key == SDLK_LEFT:
                right = False
                left = True
                up = False
                down = False
                dir -= 1
            elif event.key == SDLK_UP:
                right = False
                left = False
                up = True
                down = False
                dir2 += 1
            elif event.key == SDLK_DOWN:
                right = False
                left = True
                up = False
                down = False
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += -1
    pass


open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
frame = 0
dir = 0
dir2 = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    if(right == True):
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif (left == True):
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x+=dir*5
    y+=dir2*5

    delay(0.01)

close_canvas()
