
Components:(delete)
- Raspberry Pi Pico W Microcontroller
- Solenoid Water Valve
- S-type Load Cell
- Hx711 Load Cell Amplifier
- Relay Module
- 12V, 2A Power Supply
- 1N4007 Diode
- Momentary Push Button

Project Overview
---
&nbsp;&nbsp;&nbsp;&nbsp;I developed a system that can automatically detect the water level of a chicken waterer and refill as needed. This system requires 2 main functions:
1. Determine the current water level
2. Turn on/off water flow when necessary

&nbsp;&nbsp;&nbsp;&nbsp;My original thought was to use a float valve to determine the water level. However, this proved to be less than ideal due to the complications of installing one inside a chicken waterer, and the inherent potential for imprecise, inaccurate, and delayed readings. And so instead of directly reading the water level, I designed it to use the weight of the waterer to determine its capacity. The device I used to do this is a load cell, which can both get a weight reading, and transmit that reading to a microcontroller.  

&nbsp;&nbsp;&nbsp;&nbsp;As for how to control water flow, I used a normally closed solenoid valve. This component proved to be perfect for this project. You simply provide power to turn water flow on, and once power is removed, it shuts off. Combining this with the load cell, the microcontroller can both determine the water level, and turn on or off water flow accordingly. 

How it Works
---
&nbsp;&nbsp;&nbsp;&nbsp;Every 15 minutes, the load cell takes a weight reading, and the hx711 converts the load cell's tiny electrical signal into a readable weight value. The pico w then uses that value to either keep waiting or turn on the solenoid valve, depending on how heavy the waterer currently is. Once it gets light enough, the valve turns on, and the pico w checks every half of a second if the weight of the waterer is at its fill threshold. Once that threshold is reached, it then turns off the valve, and repeats the whole process.

Code
---
&nbsp;&nbsp;&nbsp;&nbsp;The micropython program remotely installed on the pico w controls the entire system. Immediately after the pico w receives power and starts the program, it turns off its wifi capabilities to lower power consumption, sets the physical pins on the hardware, and calibrates the load cell. It then enters a continuous loop, reading the weight of the waterer every 15 minutes, and responding accordingly. If the weight is above a certain threshold, it will do nothing, and wait another 15 minutes. But if the weight is too low, it will turn on the water valve, and start a timer. It will shut the water off if either of the following occurs:  
- The waterer reaches its' weight threshold,
- Or the water valve is on for more than 75 seconds.

If it turns off the valve because it reached the proper weight, it will simply repeat the process. However, if it turns off because it has been running for over 75 seconds, a malfunction must have occurred because it takes no longer than 60 seconds for the valve to fill the waterer. If this happens, the entire program will enter a safety shutoff loop. Instead of taking weight readings, it will simply stay in a constant loop of it sleeping for 15 minutes, doing nothing, and then sleeping again. This is a very important piece to the program because it prevents the valve from not turning off and wasting water.  

&nbsp;&nbsp;&nbsp;&nbsp;The program's last feature allows the water valve to be manually controlled. A momentary push button that is wired to the pico w allows this to happen. When pressed, the valve turns on. When it is let go, the valve turns off. Pressing the button also resets the safety shutoff system. One problem with this button was that whenever the pico w was in sleep mode, it wouldn't recognize when the button was pressed because it was mostly powered off and wouldn't wake up to check if the button was being pressed. To fix this problem, I reprogrammed the pico w during its 15 minuted sleep to sleep for one second, wake up, check if the button was pressed, and then sleep again. This way, it could still be lowering power consumption during the 15 minute sleep, but would also respond when the button was pressed.  


Hardware
---

| Component | Link |
| --- | --- |
| Raspberry Pi Pico W Microcontroller | https://www.newark.com/raspberry-pi/raspberry-pi-pico-wh/sbc-raspberry-pi-pico-wh-rp2040/dp/38AK5987?CMP=KNC-GUSA-GEN-PMAX-Shopping-New |
| Solenoid Valve | https://ussolid.com/products/u-s-solid-solenoid-valve-1-2-zinc-alloy-12v-dc-solenoid-valve-nbr-seal-html?variant=46918472728831 |
| S-type Load Cell | https://www.amazon.com/Portable-High-Precision-Pressure-Tension-Weighing/dp/B077YHNNCP/ref=sr_1_17_sspa?s=industrial |
| Hx711 Load Cell Amplifier | https://www.newark.com/raspberry-pi/raspberry-pi-pico-wh/sbc-raspberry-pi-pico-wh-rp2040/dp/38AK5987?CMP=KNC-GUSA-GEN-PMAX-Shopping-New |
| Relay Module | https://www.amazon.com/JESSINIE-Channel-Optocoupler-Isolated-Development/dp/B0BG2F7349/ref=sr_1_3 |
| 12V, 2A Power Supply | Row 6, Col 2 |
| 1N4007 Diode | https://www.amazon.com/EEEEE-1N4007-Rectifier-Electronic-Silicon/dp/B0FC2CQF24/ref=sr_1_1_sspa |
| Momentary Push Button | https://www.amazon.com/QTEATAK-Momentary-Tactile-Button-Switch/dp/B07VSNN9S2/ref=sr_1_1_sspa |

