import busio
import board

from lib.adafruit_seesaw import seesaw, neopixel, rotaryio, digitalio
import lib.adafruit_ssd1306


SDA = board.GP8
SCL = board.GP9
i2c = busio.I2C(SCL, SDA)


oled = lib.adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
oled.fill(0)

oled.text("Midi Controller v0.1 initialising", 0,0, 1) # literal string
oled.show()

# Init rotary encoder
rt_enc1 = seesaw.Seesaw(i2c, addr=0x36)
rt_enc2 = seesaw.Seesaw(i2c, addr=0x37)
rt_enc3 = seesaw.Seesaw(i2c, addr=0x38)
rt_enc4 = seesaw.Seesaw(i2c, addr=0x3a)

# pixel = neopixel.NeoPixel(seesaw.Seesaw(i2c, addr=0x36), 6, 1)
# pixel.brightness = 0.5
# pixel.fill((255, 0, 0))

rt_enc1.pin_mode(24, rt_enc1.INPUT_PULLUP)
button = digitalio.DigitalIO(rt_enc1, 24)
button_held = False

encoder1 = rotaryio.IncrementalEncoder(rt_enc1)
last_position1 = None

encoder2 = rotaryio.IncrementalEncoder(rt_enc2)
last_position2 = None

encoder3 = rotaryio.IncrementalEncoder(rt_enc3)
last_position3 = None

encoder4 = rotaryio.IncrementalEncoder(rt_enc4)
last_position4 = None

while True:

    # negate the position to make clockwise rotation positive
    position1 = -encoder1.position
    position2 = -encoder2.position
    position3 = -encoder3.position
    position4 = -encoder4.position

    if position1 != last_position1:
        last_position1 = position1
        print("Position 1: {}".format(position1))

    if position2 != last_position2:
        last_position2 = position2
        print("Position 2: {}".format(position2))

    if position3 != last_position3:
        last_position3 = position3
        print("Position 3: {}".format(position3))

    if position4 != last_position4:
        last_position4 = position4
        print("Position 4: {}".format(position4))

    # display.print(position)
    oled.fill(0)
    oled.text("RT1: " + str(position1), 0,0, 1) # literal string
    oled.text("RT2: " + str(position2) , 70,0, 1) # literal string
    oled.text("RT3: " + str(position3) , 0,20, 1) # literal string
    oled.text("RT4: " + str(position4) , 70,20, 1) # literal string
    oled.show()

    if not button.value and not button_held:
        button_held = True
        print("Button pressed")
        oled.fill(0)
        oled.text("Button 1 pressed", 0,0, 1) # literal string
        oled.show()

    if button.value and button_held:
        button_held = False
        print("Button released")
