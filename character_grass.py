from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
while x >= 0:
    if x < 750:
        if y == 90:
            while(x < 750):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x = x + 2
                delay(0.01)
        elif y > 90:
            while (y > 90):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y = y - 2
                delay(0.01)
    

    elif x >= 750:
        if(y < 550):
            while(y < 550):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(750,y)
                y = y + 2
                delay(0.01)
        elif (y >= 550):
            while(x > 0):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x = x - 2
                delay(0.01)
  
close_canvas()
