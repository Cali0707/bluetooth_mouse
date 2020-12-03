from source.accel import accel_to_position
from pyautogui import *


def move_mouse(ax, ay, az, dt):
    dx = accel_to_position(ax, dt)
    dy = accel_to_position(ay, dt)
    dz = accel_to_position(az, dt)
    x = dx
    y = -dy - dz
    moveRel(3 * x, 3 * y)
    # print('moved mouse by:', x, y)


if __name__ == '__main__':
    move_mouse(20, 1, 0, 1,)
