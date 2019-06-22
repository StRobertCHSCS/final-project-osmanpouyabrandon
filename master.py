import random
import arcade


WIDTH = 640
HEIGHT = 480

left_pressed=False
right_pressed=False
up_pressed=False
down_pressed=False
collision=False
shoot=False

player_x = 250
player_y = 100


texture_spaceship = arcade.load_texture("spaceship2 (1).jpg")
texture_background = arcade.load_texture("TWGty9.jpg")
texture_gameover= arcade.load_texture("background.png")
texture_ALien= arcade.load_texture("ALIEN2.png")
ALIEN = arcade.ShapeElementList()

texture_ALien_x_positions = []
texture_ALien_y_positions = []

for _ in range(20):
   x = random.randrange(0, WIDTH)
   y = random.randrange(HEIGHT, HEIGHT*2)

   texture_ALien_x_positions.append(x)
   texture_ALien_y_positions.append(y)


def setup():
   arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
   arcade.draw_texture_rectangle(320, 240, 640, 480, texture_background, 0)
   arcade.schedule(update, 1/30)

   window = arcade.get_window()
   window.on_draw = on_draw
   window.on_key_press = on_key_press
   window.on_key_release = on_key_release

   arcade.run()


def update(delta_time):
   global left_pressed, right_pressed,player_x, player_y, collision, up_pressed,down_pressed,shoot
   for index in range(len(texture_ALien_y_positions)):
       texture_ALien_y_positions[index] -= .3

       if texture_ALien_y_positions[index] < 0:
           texture_ALien_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
           texture_ALien_x_positions[index] = random.randrange(0, WIDTH)
   if right_pressed:
       player_x += 6
   if left_pressed:
       player_x -= 6
   if up_pressed:
       player_y+= 6
   if down_pressed:
       player_y-=6



   for index in range(len(texture_ALien_y_positions)):
       texture_ALien_y_positions[index] -= 4
       if ((texture_ALien_x_positions[index] - player_x) ** 2 + (texture_ALien_y_positions[index] - player_y) ** 2) <= 500:
           collision = True
       if texture_ALien_y_positions[index] < -25:
           texture_ALien_x_positions[index] = random.randrange(525, 1475)
           texture_ALien_y_positions[index] = random.randrange(0, 475)



def on_draw():
   arcade.start_render()
   arcade.draw_texture_rectangle(320, 240, 640, 480, texture_background, 0)

   arcade.draw_texture_rectangle(player_x,player_y,45,45,texture_spaceship,0)

   for x, y in zip(texture_ALien_x_positions, texture_ALien_y_positions):
       arcade.draw_texture_rectangle(x, y, 40,40, texture_ALien, 0)
   if collision==True:
       arcade.draw_texture_rectangle(300,250,800,500,texture_gameover,0)



def on_key_press(key, modifiers):
   global left_pressed,right_pressed,up_pressed,down_pressed
   if key==arcade.key.A:
       left_pressed = True
   if key==arcade.key.D:
       right_pressed = True
   if key==arcade.key.W:
       up_pressed=True
   if key==arcade.key.S:
       down_pressed=True



def on_key_release(key, modifiers):
   global left_pressed,right_pressed,down_pressed,up_pressed
   if key==arcade.key.A:
       left_pressed = False
   if key==arcade.key.D:
       right_pressed = False
   if key==arcade.key.W:
       up_pressed=False
   if key==arcade.key.S:
       down_pressed=False


if __name__ == '__main__':
   setup()
