# Lotus lantern client

This is a simple python script to control `ELK-BLEDOM` / `ELK-BLEDOB` led strips without the need of the lotus lantern app.
It can be used both from the command line or in a different python script.

Big shout out to [ELK-BLEDOM-bluetooth-led-strip-controller](https://github.com/TheSylex/ELK-BLEDOM-bluetooth-led-strip-controller) for documenting the protocol. I'm not familiar with rust, so I decided to take the pieces I want and create a python script instead.

I need to do something wonky to send the commands (read a characteristic and send the command twice) but it works fine so maybe that's just how it works for these led strips.

## Installation

1. Clone this repository
2. Install the requirements

```shell
pip install -r requirements.txt
```

## Usage from command line

After installing you can run it from the command line:

**Scanning**

If you don't know the address or name of your ledstrip, just run the script with no arguments. It will print all nearby devices:

```shell
python3 src/core.py
```

**Controlling**

Once you know the name or uuid of the led strip you can send commands. Run the following to see all options

```shell
python3 src/core.py -h
```

Some example commands you can try:

```shell
python3 src/core.py --name ELK-BLEDOM --command turn_on
python3 src/core.py --uuid B2C210C6-C0AB-1BA1-44C8-FAE26F57EB7A --command 'set_color 255 255 0'
python3 src/core.py --name ELK-BLEDOM --command 'set_effect crossfade_cyan'
```

## Usage in another python script

Use `asyncio` to run the functions from the `core` file.

```python
import asyncio
from core import send_command_once
from protocol import turn_on

asyncio.run(send_command_once(turn_on(), "ELK-BLEDOM"))
```
