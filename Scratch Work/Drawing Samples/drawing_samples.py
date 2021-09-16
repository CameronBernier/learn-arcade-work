"""
This is a sample program to test drawing with Python and the Arcade Library.
(Multi-line comments can be surrounded by three double-quote marks)
"""

# Single-line comment sample

import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color((155, 221, 255))

arcade.start_render()
# CSS Color Picker Library doesn't work, use RGB codes
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, (123, 182, 97))

arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

arcade.draw_circle_filled(100, 350, 30, (125, 185, 100))

arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, (123, 182, 97))

arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, (123, 182, 97), 0, 180)

arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, (123, 182, 97))

arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           (123, 182, 97))
# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Arbor Day - Plant a Tree!",
                 150, 230,
                 arcade.color.BLACK, 24)

arcade.finish_render()

arcade.run()
