import arcade

arcade.open_window(800, 800, "Mushroom House")
arcade.set_background_color((222, 184, 135))

# color for stem: LINEN, LIGHT-YELLOW, BEIGE
# color for top: FIREBRICK, DARK-RED, FERRARI-RED

arcade.start_render()

# (STEM)
# color = LINEN
arcade.draw_ellipse_filled(400, 250, 250, 70, (245, 245, 220))
arcade.draw_lrtb_rectangle_filled(320, 460, 420, 250, (245, 245, 220))
arcade.draw_triangle_filled(275, 250, 360, 390, 525, 250, (245, 245, 220))
arcade.draw_ellipse_filled(350, 220, 50, 20, (245, 245, 220))
arcade.draw_ellipse_filled(450, 225, 70, 20, (245, 245, 220))
arcade.draw_ellipse_filled(390, 440, 250, 80, (245, 245, 220))


# (MUSHROOM TOP)
arcade.draw_ellipse_filled(390, 460, 300, 90, (123, 182, 97))
arcade.draw_arc_filled(390, 460, 270, 240, (123, 182, 97), 0, 180)
arcade.draw_triangle_filled(525, 450, 540, 460, 508, 515, (123, 182, 97))
arcade.draw_triangle_filled(240, 460, 270, 515, 280, 460, (123, 182, 97))
arcade.draw_text("o", 500, 460, (172, 225, 175), font_size=10)
arcade.draw_text("o", 495, 470, (172, 225, 175), font_size=8)
arcade.draw_text("o", 487, 455, (172, 225, 175), font_size=11)

arcade.draw_ellipse_filled(290, 480, 35, 15, (255, 255, 255), tilt_angle=-70)

# (DOOR)
arcade.draw_ellipse_filled(410, 290, 40, 60, (75, 83, 32))
arcade.draw_ellipse_outline(410, 290, 40, 60, (0, 66, 37))
arcade.draw_text("o", 410, 280, (237, 145, 33), font_size=17)

# (SPARKLES)
arcade.draw_text("o", 263, 275, (255, 255, 255), font_size=10)
arcade.draw_text("o", 260, 260, (255, 255, 255), font_size=7)
arcade.draw_text("o", 270, 265, (255, 255, 255), font_size=9)
arcade.draw_text("o", 275, 275, (255, 255, 255), font_size=7)

arcade.draw_text("o", 470, 300, (255, 255, 255), font_size=11)
arcade.draw_text("o", 480, 295, (255, 255, 255), font_size=8)
arcade.draw_text("o", 465, 315, (255, 255, 255), font_size=9)

# ("BRANCH")
arcade.draw_triangle_filled(260, 380, 350, 400, 350, 300, (245, 245, 220))
arcade.draw_ellipse_filled(300, 375, 100, 30, (245, 245, 220))
arcade.draw_ellipse_filled(300, 380, 120, 30, (123, 182, 97))
arcade.draw_ellipse_filled(350, 350, 80, 20, (123, 182, 97))

arcade.finish_render()

arcade.run()
