from source.decode_bytes import decode_bytes
from source.filter_data import filter_data
from source.move_mouse import move_mouse


def data_handler(data, lz, la, lb):
    x, y, z = data
    new_x, zix = filter_data(x, la[0], lb[0], lz[0])
    new_y, ziy = filter_data(y, la[1], lb[1], lz[1])
    new_z, ziz = filter_data(z, la[2], lb[2], lz[2])
    move_mouse(new_x, new_y, new_z, 0.1)
    return [zix, ziy, ziz]
