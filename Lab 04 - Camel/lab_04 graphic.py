import arcade
import random


def grass():

    width = 0
    height = 0
    grass_color = (20, 39, 47)
    while width < 600 and height < 300:
        arcade.draw_rectangle_filled(300, 100, width, height, grass_color)
        width += 2
        height += 1


def river():
    x = 300
    width = 225
    river_color = (53, 78, 71)
    for y_pos in range(0, 245):
        arcade.draw_lrtb_rectangle_filled(x - width/2, x + width/2, y_pos + 1, y_pos, river_color)
        width -= 0.5
        if width <= 0:
            break


# base color (28, 46, 50)
def mountain():
    mountain_color = (15, 24, 29)
    arcade.draw_polygon_filled(((120, 249), (210, 420), (320, 470), (440, 330), (460, 249)), mountain_color)


def tree():
    x = 140
    width = 90
    river_color = (53, 78, 71)
    offset = random.randrange(-10, 10)
    step = 5
    for y_pos in range(0, 245, step):
        arcade.draw_lrtb_rectangle_filled(x - width / 2 + offset, x + width / 2 + offset, y_pos + 1, y_pos, arcade.csscolor.WHITE)
        width -= 1
        offset = 0.5 * step
        if width <= 0:
            break


def main():

    arcade.open_window(600, 800, "Forest")
    arcade.set_background_color((181, 171, 167))

    arcade.start_render()

    grass()
    river()
    mountain()

    arcade.finish_render()

    arcade.run()


main()
