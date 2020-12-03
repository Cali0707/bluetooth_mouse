import asyncio
from bleak import *
from source.connect import connect
from source.handle_data import handle_data


async def main():
    device_name = '3dMouse'
    characteristic = '6b90ba69-3581-4c91-9614-ccc1d2178103'
    client = await connect(device_name)
    time = 0
    old_data = [[], [], []]
    # print(type(old_data))
    while time < 40:
        print("Calibrating...    {} seconds remaining".format(str(time)))
        await asyncio.sleep(10)
        time += 10
    while time < 60:
        data = await client.read_gatt_char(characteristic)
        old_data = handle_data(data, old_data)
        time += 0.1
        print(time)
        print(old_data)
    await client.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
