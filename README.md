# Lotus lantern client

This is a simple python script to control `ELK-BLEDOM` / `ELK-BLEDOB` led strips without the need of the lotus lantern app.
It can be used both from the command line or in a different python script.

Big shout out to [ELK-BLEDOM-bluetooth-led-strip-controller](https://github.com/TheSylex/ELK-BLEDOM-bluetooth-led-strip-controller) for documenting the protocol. I'm not familiar with rust, so I decided to take the pieces I want and create a python script instead.

Commands are sent as a Write Without Response to the writable characteristic. Because that write is fire-and-forget, the script waits briefly afterwards so the packet flushes before disconnecting — otherwise the command never reaches the strip (this was the cause of it working on macOS but not on a Raspberry Pi).

## Installation

1. Clone this repository
2. Install the package (this pulls in [bleak](https://pypi.org/project/bleak/) automatically):

```shell
pip install .
```

Use `pip install -e .` instead if you want an editable/development install.

## Usage from command line

Installing the package adds a `lotus-lantern` command.

**Scanning**

If you don't know the address or name of your ledstrip, just run the command with no arguments. It will print all nearby devices:

```shell
lotus-lantern
```

**Controlling**

Once you know the name or uuid of the led strip you can send commands. Run the following to see all options

```shell
lotus-lantern -h
```

Some example commands you can try:

```shell
lotus-lantern --name ELK-BLEDOM --command turn_on
lotus-lantern --uuid B2C210C6-C0AB-1BA1-44C8-FAE26F57EB7A --command 'set_color 255 255 0'
lotus-lantern --name ELK-BLEDOM --command 'set_effect crossfade_cyan'
```

## Usage in another python script

Import the helpers from the `lotus_lantern` package and use `asyncio` to run them.

```python
import asyncio
from lotus_lantern import send_command_once
from lotus_lantern.protocol import turn_on

asyncio.run(send_command_once(turn_on(), "ELK-BLEDOM"))
```
