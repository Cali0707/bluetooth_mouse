import asyncio
from bleak import *


async def connect(device_name):
    ble = None
    devices = await discover()
    connection = False
    client = None
    for d in devices:
        if d.name == device_name:
            ble = d
    if ble is not None:
        client = BleakClient(ble)
        connection = await client.connect()
        # print(client)
    if connection:
        print('Connected to {}'.format(device_name))
        await asyncio.sleep(4)
        return client
    else:
        raise ConnectionError("Failed to connect to {}".format(device_name))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = loop.run_until_complete(connect('3dMouse'))
    print(client)

