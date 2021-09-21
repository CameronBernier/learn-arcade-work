
import arcade

arcade.open_window(600, 600, "Turtle")
arcade.set_background_color((172, 229, 238))

arcade.start_render()
# head
arcade.draw_ellipse_filled(200, 300, 80, 60, (119, 179, 105))
# legs (front)
arcade.draw_ellipse_filled(260, 300, 80, 220, (119, 179, 105))
# legs (back)
arcade.draw_ellipse_filled(340, 300, 80, 220, (119, 179, 105))
# tail
arcade.draw_triangle_filled(390, 320, 390, 280, 420, 300, (119, 179, 105))
# shell
arcade.draw_circle_filled(center_x=299,
                          center_y=299,
                          radius=100,
                          color=(199, 138, 74))
# shell detail
arcade.draw_circle_outline(299, 299, 100, arcade.csscolor.SADDLE_BROWN)
arcade.draw_circle_filled(299, 299, 80, (207, 170, 116))
arcade.draw_circle_outline(299, 299, 80, arcade.csscolor.SADDLE_BROWN)

arcade.finish_render()

arcade.run()
