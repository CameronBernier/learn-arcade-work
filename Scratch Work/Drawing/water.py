import arcade

arcade.open_window(600, 600, "Ocean Backdrop")
arcade.set_background_color((156, 213, 217))

arcade.start_render()

# Orange fish: body
arcade.draw_ellipse_filled(150, 150, 100, 60, (255, 127, 80))
arcade.draw_triangle_filled(150, 150, 220, 125, 220, 175, (255, 127, 80))
# Orange fish: stripes
arcade.draw_line(125, 176, 125, 124, arcade.csscolor.WHITE)
arcade.draw_line(150, 180, 150, 120, arcade.csscolor.WHITE)
arcade.draw_line(175, 176, 175, 124, arcade.csscolor.WHITE)
# Orange fish: eye
arcade.draw_circle_filled(120, 150, 7, arcade.csscolor.BLACK)

# Puffer fish: body
arcade.draw_circle_filled(400, 400, 50, (255, 191, 0))
arcade.draw_triangle_filled(400, 400, 325, 365, 325, 435, (255, 191, 0))
# Puffer fish: eyes
arcade.draw_circle_filled(420, 400, 7, arcade.csscolor.BLACK)

# Bubbles
arcade.draw_circle_outline(490, 490, 16, (240, 255, 255))
arcade.draw_circle_outline(450, 450, 10, (240, 255, 255))
arcade.draw_circle_outline(480, 410, 8, (240, 255, 255))

arcade.draw_circle_outline(300, 300, 16, (240, 255, 255))
arcade.draw_circle_outline(400, 120, 18, (240, 255, 255))
arcade.draw_circle_outline(440, 140, 12, (240, 255, 255))
arcade.draw_circle_outline(200, 400, 10, (240, 255, 255))
arcade.draw_circle_outline(100, 500, 14, (240, 255, 255))
arcade.draw_circle_outline(190, 190, 12, (240, 255, 255))

# Sand floor
arcade.draw_lrtb_rectangle_filled(0, 600, 60, 0, (250, 214, 165))

# Rocks
arcade.draw_ellipse_filled(540, 50, 100, 50, arcade.csscolor.GREY)
arcade.draw_ellipse_filled(450, 40, 80, 30, arcade.csscolor.GREY)


arcade.finish_render()

arcade.run()
