import asyncio
from bleak import *


async def run():
    """
    Test that the computer can see the Arduino

    Checks for all visible BLE devices, then connects
    to 3dMouse if found. Verifies that it can read data
    off of the Arduino.
    """
    characteristic = "6b90ba69-3581-4c91-9614-ccc1d2178103"
    ble = None
    devices = await discover()
    for d in devices:
        if d.name == '3dMouse':
            ble = d
    if ble is not None:
        client = BleakClient(ble)
        print("connected to {}".format(ble.name))
        connection = await client.connect()
        data = await client.read_gatt_char(characteristic)
        print(int.from_bytes(data[0:3], byteorder='big'))
        print(int.from_bytes(data[4:7], byteorder='big'))
        print(int.from_bytes(data[8:11], byteorder='big'))
        await client.disconnect()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())