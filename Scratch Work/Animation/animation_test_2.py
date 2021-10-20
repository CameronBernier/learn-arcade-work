import arcade

SCROLL_BEIGE = (219, 209, 175)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WATER = (162, 210, 219, 100)
RIPPLE_COLOR = (143, 176, 201, 150)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def water():
    """Base water"""
    arcade.draw_ellipse_filled(400, 150, 300, 60, WATER)


def water_ripples(x, y):
    arcade.draw_ellipse_outline(400, 150, 50 + x, 10 + y, RIPPLE_COLOR)


def crane():
    """Crane body"""
    # crane legs

    arcade.draw_line(390, 300, 400, 150, BLACK, 6)
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
    arcade.draw_ellipse_filled(390, 310, 60, 40, WHITE, tilt_angle=42)
    arcade.draw_ellipse_filled(300, 490, 15, 30, WHITE, 155)

    # crane eye
    arcade.draw_ellipse_filled(305, 497, 30, 20, BLACK, 110)
    arcade.draw_text("o", 298, 490, WHITE, 10)


def on_draw(delta_time):
    """Draw everything"""
    arcade.start_render()

    water()
    water_ripples(0, 0)
    crane()


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Animation Base")
    arcade.set_background_color(SCROLL_BEIGE)

    arcade.schedule(on_draw, 1/60)
    arcade.run()


main()
