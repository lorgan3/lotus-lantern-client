import asyncio
import argparse
from bleak import BleakClient, BleakScanner

from protocol import COMMANDS, EFFECTS


# Print all found devices.
async def scan():
    print("Scanning for devices...")
    devices = await BleakScanner.discover()

    for device in devices:
        print(device)


# Send a command to a given device.
async def send_command(command: bytearray, client: BleakClient):
    for characteristic in client.services.characteristics.values():
        try:
            # For some reason it only works when sending the command twice.
            for i in range(0, 2):
                # Don't know why but without reading we can't write
                await client.read_gatt_char(characteristic.uuid)

                await client.write_gatt_char(characteristic.uuid, command)
        except:
            # Seems like ELK-BLEDOM needs to write to the first characteristic and ELK-BLEDOB to the last one. Just ignore errors
            pass


# Connect to a device using name or uuid, send 1 command and then disconnect.
async def send_command_once(command: bytearray, name: str = None, uuid: str = None):
    if name is not None:
        device = await BleakScanner.find_device_by_filter(
            lambda device, data: device.name == name
        )
    elif uuid is not None:
        device = await BleakScanner.find_device_by_filter(
            lambda device, data: device.address == uuid
        )
    else:
        raise ValueError("You must provide either a name or a uuid")

    async with BleakClient(device.address) as client:
        await send_command(command, client)


async def main(command: bytearray = None, name: str = None, uuid: str = None):
    if command is None:
        await scan()
    else:
        await send_command_once(command, name, uuid)


if __name__ == "__main__":
    epilog = """
Available commands are:
\n\t- {commands}

Available effects are:
\n\t- {effects}
""".format(
        commands="\n\t- ".join(COMMANDS.keys()), effects="\n\t- ".join(EFFECTS.keys())
    )

    parser = argparse.ArgumentParser(
        description="Simple lotus lantern client.",
        epilog=epilog,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--name", help="Name of the ledstrip, usually 'ELK-BLEDOM' or 'ELK-BLEDOB'."
    )
    parser.add_argument(
        "--uuid", help="Uuid of the specific ledstrip you want to connect to."
    )
    parser.add_argument(
        "--command",
        help="Command to send to the ledstrip. Use quotes for parameters: '--command set_color 255 0 0'",
    )
    args = parser.parse_args()

    command = None
    if args.command:
        argCommand, *rest = args.command.split(" ")
        key = next(
            (
                command
                for command, fn in COMMANDS.items()
                if command.startswith(argCommand)
            ),
            None,
        )

        if key is not None:
            if key == "set_effect <effect>":
                intParams = [EFFECTS[rest[0]]]
            else:
                intParams = [int(param) for param in rest]

            command = COMMANDS[key](*intParams)

    asyncio.run(main(name=args.name, uuid=args.uuid, command=command))
