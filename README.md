This project features a fully autonomous chicken waterer refill system.

Components:
- Raspberry Pi Pico W Microcontroller
- Solenoid Water Valve
- S-type Load Cell
- Hx711 Load Cell Amplifier
- Relay Module
- 12V, 2A Power Supply
- IN4007 Diode
- Momentary Push Button

Project Overview
---
&nbsp;&nbsp;&nbsp;&nbsp;Anyone who has owned them knows that taking care of chickens can be a hassle. But for me the most annoying and time-consuming part is having to fill up their water every morning and night. And so I decided to create a system that could refill it automatically. This system had to be able to perform 2 main functions:
1. Determine the current water level
2. Turn on/off water flow when necessary

&nbsp;&nbsp;&nbsp;&nbsp;My original thought was to use a float valve to determine the water level. However, this proved to be less than ideal due to the complications of installing one inside a chicken waterer, and the inherent potential for imprecise, inaccurate, and delayed readings. And so I decided that, instead of directly reading the water level, I could use the weight of the waterer to calculate its capacity. The best device to use that can both get a weight reading, and transmit it to a microcontroller, is a load cell.  

&nbsp;&nbsp;&nbsp;&nbsp;As for how to control water flow, it turned out to be easier than I thought it was going to be. I found a normally closed solenoid valve that was perfect for this project. You simply provide power to turn water flow on, and remove power for it to shut off. Combining these two devices, you can both determine the water level, and turn on or off water flow accordingly. 

How it Works
---

