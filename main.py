import time
import machine
from machine import Pin
from hx711 import HX711
import network

for interface in (network.STA_IF, network.AP_IF):
    wlan = network.WLAN(interface)
    wlan.active(False)
    wlan.deinit()

pin_out = Pin(27, Pin.IN)
pin_sck = Pin(28, Pin.OUT)

hx = HX711(clock=pin_sck, data=pin_out)

hx.tare()

ratio = 20787.8
hx.set_scale(ratio)

relay_in = Pin(17, Pin.OUT)
relay_in.value(0)

button = Pin(2, Pin.IN, Pin.PULL_UP)

safety_turnoff = False

def battery_sleep_15_min():
    for _ in range(900):
        if button.value() == 0:
            break
        machine.lightsleep(1000)
        time.sleep(0.05)

def button_pressed():
    global safety_turnoff
    time.sleep(0.05)
        
    if safety_turnoff:
        safety_turnoff = False
            
    relay_in.value(1)
        
    while button.value() == 0:
        time.sleep(0.05)
        
    relay_in.value(0)
    time.sleep(1)


def fill_waterer():
    global safety_turnoff
    time.sleep(1)
    weight = hx.get_units()
        
    if weight > 5:
        battery_sleep_15_min()
        return
        
    elif weight <= 5:
        relay_in.value(1)
        start_time = time.ticks_ms() 
            
        while weight <= 23:
            weight = hx.get_units()
                
            elapsed_seconds = time.ticks_diff(time.ticks_ms(), start_time) / 1000	
            time.sleep(.5)

            if elapsed_seconds >= 75:
                safety_turnoff = True
                break
            
        relay_in.value(0)
        time.sleep(5)
            
            

while True:
    
    #  IF BUTTON PRESSED
    
    if button.value() == 0:
        button_pressed()
        continue
    
    if safety_turnoff:
        relay_in.value(0)
        battery_sleep_15_min()
        continue

    time.sleep(.5)
    weight = hx.get_units()
    
    if weight > 5:
        battery_sleep_15_min()
        continue
    
    elif weight <= 5:
        fill_waterer()

