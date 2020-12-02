from bleak import *

from source.average import average
from source.decode_bytes import decode_bytes
from source.move_mouse import move_mouse


def handle_data(data, old_data):
    ax, ay, az = decode_bytes(data)
    # print(old_data)
    # print('updated')
    if len(old_data[0]) == 5:
        ax_old_av = average(old_data[0])
        ay_old_av = average(old_data[1])
        az_old_av = average(old_data[2])
        new_x = old_data[0][1:]
        new_y = old_data[1][1:]
        new_z = old_data[2][1:]
        new_x.append(ax)
        new_y.append(ay)
        new_z.append(az)
        ax_new_av = average(new_x)
        ay_new_av = average(new_y)
        az_new_av = average(new_z)
        dt = 0.1
        move_mouse(ax_new_av - ax_old_av, ay_new_av - ay_old_av, az_new_av - az_old_av, dt)
        return [ax, ay, az]
    else:
        old_x = old_data[0][1:]
        old_y = old_data[1][1:]
        old_z = old_data[2][1:]
        return [old_x.append(ax), old_y.append(ay), old_z.append(az)]
