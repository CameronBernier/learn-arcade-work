import arcade
import random


def lavender():
    lavender_color = (175, 184, 222)
    arcade.draw_lrtb_rectangle_filled(0, 90, 800, 0, lavender_color)
    arcade.draw_lrtb_rectangle_filled(510, 600, 800, 0, lavender_color)


def deep_maroon():
    width = 0
    height = 0
    deep_maroon_color = (55, 29, 43)
    while width < 450 and height < 750:
        arcade.draw_rectangle_filled(300, 400, width, height, deep_maroon_color)
        width += 1.5
        height += 2


def deep_purple():
    tri_w = 100
    tri_h = 70
    deep_purple_color = (56, 47, 91)
    for x in range(0, 600, 70):
        w = tri_w + random.randrange(-50, 50)
        h = tri_h + random.randrange(-50, 50)
        left = x
        right = x + w
        mid = x + w / 2
        arcade.draw_triangle_filled(left, 550, right, 550, mid, 550 + h, deep_purple_color)

    arcade.draw_lrtb_rectangle_filled(76, 524, 550, 100, deep_purple_color)


def royal_blue():
    tri_w = 100
    tri_h = 70
    royal_blue_color = (61, 71, 159)
    for x in range(0, 600, 70):
        w = tri_w + random.randrange(-50, 50)
        h = tri_h + random.randrange(-50, 50)
        left = x
        right = x + w
        mid = x + w / 2
        arcade.draw_triangle_filled(left, 250, right, 250, mid, 250 + h, royal_blue_color)

    arcade.draw_lrtb_rectangle_filled(76, 524, 250, 100, royal_blue_color)


def protector():
    protector_body_color = (50, 32, 60)
    protector_head_color = (52, 34, 62)
    arcade.draw_rectangle_filled(300, 200, 20, 10, protector_body_color, tilt_angle=- 40)
    arcade.draw_ellipse_filled(310, 213, 20, 20, protector_head_color)
    arcade.draw_line(305, 214, 295, 230, protector_head_color, 2)
    arcade.draw_line(315, 214, 325, 230, protector_head_color, 2)
    arcade.draw_text("/ |", 286, 183, protector_body_color, 12)
    arcade.draw_text("( \ ", 299, 190, protector_body_color, 12, 12)
    arcade.draw_text("o o", 300, 213, (255, 255, 255), 10)


def draw_eyes(x, y):
    eye_color = (255, 255, 255, random.randrange(20, 255))
    arcade.draw_text("o o", x, y, eye_color, 10)


def main():

    arcade.open_window(600, 800, "Forest")
    arcade.set_background_color((175, 184, 222))

    arcade.start_render()

    deep_maroon()
    deep_purple()
    royal_blue()
    lavender()
    protector()
    draw_eyes(200, 400)
    draw_eyes(450, 450)
    draw_eyes(300, 500)
    draw_eyes(410, 150)

    arcade.draw_text("Forest", 255, 400, (107, 124, 198), 24, 12)

    arcade.finish_render()

    arcade.run()


main()
