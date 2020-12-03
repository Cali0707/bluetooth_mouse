from bleak import *
from copy import deepcopy

from source.average import average
from source.decode_bytes import decode_bytes
from source.move_mouse import move_mouse


def handle_data(data, old_data):
    old_data_copy = deepcopy(old_data)
    ax, ay, az = decode_bytes(data)
    # print(old_data)
    # print('updated')
    # print(type(old_data_copy[0]))
    # print('len =', len(old_data_copy[0]))
    if len(old_data_copy[0]) < 5:
        old_x = old_data_copy[0]
        old_x.append(ax)
        # print(old_x)
        old_y = old_data_copy[1]
        old_y.append(ay)
        old_z = old_data_copy[2]
        old_z.append(az)
        return [old_x, old_y, old_z]
    else:
        ax_old_av = average(old_data_copy[0])
        ay_old_av = average(old_data_copy[1])
        az_old_av = average(old_data_copy[2])
        new_x = old_data_copy[0][1:]
        new_y = old_data_copy[1][1:]
        new_z = old_data_copy[2][1:]
        # print(ax, ay, az)
        new_x.append(ax)
        new_y.append(ay)
        new_z.append(az)
        ax_new_av = average(new_x)
        ay_new_av = average(new_y)
        az_new_av = average(new_z)
        dt = 0.1
        move_mouse(ax_new_av - ax_old_av, ay_new_av - ay_old_av, az_new_av - az_old_av, dt)
        return [new_x, new_y, new_z]
