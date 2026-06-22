# https://github.com/TheSylex/ELK-BLEDOM-bluetooth-led-strip-controller

def turn_on():
    return bytearray([0x7e, 0x00, 0x04, 0xf0, 0x00, 0x01, 0xff, 0x00, 0xef])

def turn_off():
    return bytearray([0x7e, 0x00, 0x04, 0x00, 0x00, 0x00, 0xff, 0x00, 0xef])

def set_color(red: int, green: int, blue: int):
    return bytearray([0x7e, 0x00, 0x05, 0x03, red, green, blue, 0x00, 0xef])

def set_brightness(value: int):
    return bytearray([0x7e, 0x00, 0x01, min(value, 0x64), 0x00, 0x00, 0x00, 0x00, 0xef])

def set_effect(value: int):
    return bytearray([0x7e, 0x00, 0x03, value, 0x03, 0x00, 0x00, 0x00, 0xef])

def set_effect_speed(value: int):
    return bytearray([0x7e, 0x00, 0x02, min(value, 0x64), 0x00, 0x00, 0x00, 0x00, 0xef])

COMMANDS = {
    'turn_on': turn_on,
    'turn_off': turn_off,
    'set_color <r> <g> <b>': set_color,
    'set_brightness <brightness>': set_brightness,
    'set_effect <effect>': set_effect,
    'set_effect_speed <speed>': set_effect_speed,
}

EFFECTS =  {
    'jump_red_green_blue': 0x87,
    'jump_red_green_blue_yellow_cyan_magenta_white': 0x88,
    'crossfade_red': 0x8b,
    'crossfade_green': 0x8c,
    'crossfade_blue': 0x8d,
    'crossfade_yellow': 0x8e,
    'crossfade_cyan': 0x8f,
    'crossfade_magenta': 0x90,
    'crossfade_white': 0x91,
    'crossfade_red_green': 0x92,
    'crossfade_red_blue': 0x93,
    'crossfade_green_blue': 0x94,
    'crossfade_red_green_blue': 0x89,
    'crossfade_red_green_blue_yellow_cyan_magenta_white': 0x8a,
    'blink_red': 0x96,
    'blink_green': 0x97,
    'blink_blue': 0x98,
    'blink_yellow': 0x99,
    'blink_cyan': 0x9a,
    'blink_magenta': 0x9b,
    'blink_white': 0x9c,
    'blink_red_green_blue_yellow_cyan_magenta_white': 0x95,
}
