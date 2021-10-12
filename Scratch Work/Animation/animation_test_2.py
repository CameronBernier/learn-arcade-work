import arcade

arcade.open_window(800, 800, "Animation Base")
SCROLL_BEIGE = (219, 209, 175)

arcade.set_background_color(SCROLL_BEIGE)

arcade.start_render()

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

# water
WATER = (162, 210, 219, 100)

arcade.draw_ellipse_filled(400, 150, 300, 60, WATER)
arcade.draw_ellipse_outline(400, 150, 200, 40,(143, 176, 201, 150))
arcade.draw_ellipse_outline(400, 150, 100, 20, (143, 176, 201, 150))
arcade.draw_ellipse_outline(400, 150, 50, 10, (143, 176, 201, 150))

# crane legs

arcade.draw_line(390, 300, 400,  150, BLACK, 6)
arcade.draw_ellipse_filled(395, 450 / 2, 22, 12, BLACK, tilt_angle=85)

arcade.draw_line(380, 300, 370, 235, BLACK, 6)
arcade.draw_line(370, 230, 420, 180, BLACK, 6)
arcade.draw_ellipse_filled(370, 230, 22, 12, BLACK, tilt_angle=45)

# crane beak

arcade.draw_triangle_filled(260, 460, 330, 490, 300, 500, BLACK)

# crane body
arcade.draw_ellipse_filled(400, 370, 200, 130, WHITE, 45)
arcade.draw_text("2", 315, 425, WHITE, 110, 10)
arcade.draw_circle_filled(320, 500, 25, WHITE)
arcade.draw_triangle_filled(450, 290, 470, 360, 510, 300, WHITE)
arcade.draw_ellipse_filled(390, 310, 60, 40, WHITE, tilt_angle = 42)
arcade.draw_ellipse_filled(300, 490, 15, 30, WHITE, 155)

# crane eye
arcade.draw_ellipse_filled(305, 497, 30, 20, BLACK, 110)
arcade.draw_text("o", 298, 490, WHITE, 10)

arcade.finish_render()

arcade.run()
