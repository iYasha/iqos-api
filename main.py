import asyncio
from bleak import BleakClient

IQOS_MAC = ''
BATTERY_NOTIFY = 'f8a54120-b041-11e4-9be7-0002a5d5c51b'


def battery_info_cb(_, bytearray_data):
    if len(bytearray_data) == 7:
        charger_charge = bytearray_data[2]
        holder_charge = bytearray_data[6]
    else:
        charger_charge = bytearray_data[2]
        holder_charge = False
    print(f'IQOS Battery Charge: {charger_charge}')
    print(f'IQOS Stick was charging: {holder_charge}')


async def connection(address):
    async with BleakClient(address) as client:
        while True:
            await asyncio.sleep(5.0)
            await client.start_notify(BATTERY_NOTIFY, battery_info_cb)


loop = asyncio.get_event_loop()
loop.run_until_complete(connection(IQOS_MAC))
