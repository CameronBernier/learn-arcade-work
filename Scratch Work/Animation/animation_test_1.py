import arcade

arcade.open_window(800, 800, "Bulb Flower")

SCROLL_COLOR = (204, 194, 161)

arcade.set_background_color(SCROLL_COLOR)

arcade.start_render()

# flower base
FLOWER_COLOR = (92, 229, 229)
arcade.draw_circle_filled(400, 400, 40, FLOWER_COLOR)
arcade.draw_circle_filled(325, 450, 35, FLOWER_COLOR)
arcade.draw_circle_filled(410, 500, 35, FLOWER_COLOR)
arcade.draw_circle_filled(330, 540, 35, FLOWER_COLOR)
arcade.draw_circle_filled(380, 600, 30, FLOWER_COLOR)
# flower shadow
FLOWER_HIGHLIGHT = (195, 245, 248)
arcade.draw_ellipse_filled(385, 415, 20, 35, FLOWER_HIGHLIGHT, 45)

arcade.finish_render()

arcade.run()
