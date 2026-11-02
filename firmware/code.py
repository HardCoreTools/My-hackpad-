import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Matrix (3x3)
keyboard.col_pins = (board.D1, board.D0, board.D2)
keyboard.row_pins = (board.D3, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

# Rotary encoder (A, B, button)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D10, board.D6, board.D7, False),)

# Key shortcuts
BACK = KC.LALT(KC.LEFT)                    # Browser back
REFRESH = KC.F5                            # Refresh page
FORWARD = KC.LALT(KC.RIGHT)                # Browser forward
LOCK = KC.LGUI(KC.L)                       # Lock computer
DESKTOP = KC.LGUI(KC.D)                    # Show desktop
TASKMGR = KC.LCTL(KC.LSFT(KC.ESC))         # Task manager

keyboard.keymap = [
    [
        BACK,       REFRESH,    FORWARD,
        KC.MPRV,    KC.MPLY,    KC.MNXT,
        LOCK,       DESKTOP,    TASKMGR,
    ],
]

# Encoder: turn left = volume down, turn right = volume up, press = mute
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

# OLED (128x32): show "Hello"
try:
    displayio.release_displays()
    i2c = busio.I2C(board.SCL, board.SDA)
    bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    oled = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=32)

    group = displayio.Group()
    group.append(
        label.Label(
            terminalio.FONT,
            text='Hello!',
            scale=2,
            anchor_point=(0.5, 0.5),
            anchored_position=(64, 16),
        )
    )
    oled.root_group = group
except Exception as e:
    # Keyboard still works even if the screen fails
    print('OLED error:', e)

if __name__ == '__main__':
    keyboard.go()
