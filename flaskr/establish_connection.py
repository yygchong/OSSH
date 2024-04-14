# import python-kasa
import asyncio
from kasa import Discover
from collections import defaultdict
import sqlite3

def establish_connection():
    """This is a view function for establishing a connection with
    our IOT device(s). This is used for debugging and manual set up of devices."""

    device_dict = defaultdict(list)
    devices = asyncio.run(Discover.discover())
    for addr, dev in devices.items():
        asyncio.run(dev.update())
        print(f"{addr} is on: {dev.is_on}")

        device_dict[addr] = dev.is_on

    return device_dict