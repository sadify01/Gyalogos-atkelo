def set_lights(p0, p1, p2, p14, p16, delay):
  pins.digital_write_pin(DigitalPin.P0, p0)
  pins.digital_write_pin(DigitalPin.P1, p1)
  pins.digital_write_pin(DigitalPin.P2, p2)
  pins.digital_write_pin(DigitalPin.P14, p14)
  pins.digital_write_pin(DigitalPin.P16, p16)
  pause(delay)

while True:
  set_lights(0, 0, 1, 1, 0, 15000)
  set_lights(0, 1, 0, 1, 0, 3000)
  set_lights(1, 0, 0, 1, 0, 3000) 
  set_lights(1, 0, 0, 0, 1, 10000)
  
  for i in range(5):
    set_lights(1, 0, 0, 0, 0, 500)
    set_lights(1, 0, 0, 0, 1, 500)

  set_lights(1, 0, 0, 1, 0, 3000)
  set_lights(1, 1, 0, 1, 0, 3000)