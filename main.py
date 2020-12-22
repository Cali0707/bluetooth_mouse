import asyncio
from bleak import *
from source.connect import connect
from source.data_handler import data_handler
from source.filter_data import initialize_filter
from source.handle_data import handle_data


async def main():
    """
    Main loop for running using the 3dMouse

    Connects to the appropriate device and reads data from the characteristic.
    This is passed to handle_data.py which filters the data and moves the mouse.
    """
    device_name = '3dMouse'
    characteristic = '6b90ba69-3581-4c91-9614-ccc1d2178103'
    client = await connect(device_name)
    time = 0
    old_data = [[], [], []]
    b, a, zi = initialize_filter()
    la = [a] * 3
    lb = [b] * 3
    lz = [zi] * 3
    while time < 20:
        data = await client.read_gatt_char(characteristic)
        old_data, lz = handle_data(data, old_data, la, lb, lz)
        time += 0.1
    await client.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
