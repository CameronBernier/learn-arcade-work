import random

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# function that draws grass
x = 0
y = 0
row = 0
column = 0


def draw_grass():
    while row in range(0, 15):
        for column in range(125):
            x = 5
            y = 220
            i = random.randint(100, 500)
            arcade.draw_rectangle_filled(x + i * column, y + 10, 3, 15, arcade.color.DARK_GREEN)


# function that draws clouds
def draw_cloud(x, y):
    arcade.draw_circle_filled(300 + x, 500 + y, 40, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(249 + x, 480 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(348 + x, 483 + y, 30, arcade.csscolor.WHITE)



def draw_sun():
    arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

    arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

    arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)



# draw_grass()

def the_chest():
    arcade.draw_rectangle_filled(290, 250, 100, 70, arcade.csscolor.GRAY)
    arcade.draw_rectangle_filled(290, 250, 7, 15, arcade.csscolor.BLACK)
    arcade.draw_line(240, 250, 340, 250, arcade.csscolor.BLACK)
    arcade.draw_text("chest", 270, 260, arcade.csscolor.BLACK, 12)

def head_of_man():
    arcade.draw_circle_filled(100, 300, 20, arcade.color.BEIGE)

def body_of_man():
    arcade.draw_rectangle_filled(100, 250, 30, 50, arcade.color.VIOLET)
    arcade.draw_rectangle_filled(100, 250, 30, 50, arcade.color.VIOLET)
    arcade.draw_rectangle_filled(90, 212, 10, 30, arcade.color.VIOLET)
    arcade.draw_rectangle_filled(110, 212, 10, 30, arcade.color.VIOLET)
    arcade.draw_rectangle_filled(80, 260, 10, 30, arcade.color.VIOLET)
    arcade.draw_rectangle_filled(120, 260, 10, 30, arcade.color.VIOLET)

def main():
    # opens the window and draws the ground, sky
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Camel Game Adaptation')
    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

    arcade.start_render()

    arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.csscolor.SIENNA)
    arcade.draw_rectangle_filled(300, 200, 600, 50, arcade.csscolor.TAN)
    # draws a bunch of clouds and also the grass
    draw_cloud(-200, 50)
    draw_cloud(150, -50)
    draw_cloud(100, 50)
    draw_cloud(0, 0)
    draw_cloud(-100, 30)

    draw_sun()

    the_chest()
    head_of_man()
    body_of_man()

    arcade.finish_render()

    arcade.run()


main()
