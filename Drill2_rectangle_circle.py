from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    for i in range(400, 750, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(i, 90)
        delay(0.01)
    for i in range(90, 550, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, i)
        delay(0.01)
    for i in range(750, 50, -2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(i, 550)
        delay(0.01)
    for i in range(550, 90, -2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, i)
        delay(0.01)
    for i in range(50, 400, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(i, 90)
        delay(0.01)
    for i in range(0, 200, 1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(math.sin(i*math.pi/100)*230+400, math.cos(i*math.pi/100)*230+320)
        delay(0.01)