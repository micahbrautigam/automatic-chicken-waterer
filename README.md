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
&nbsp;&nbsp;&nbsp;&nbsp;Every 15 minutes, the load cell takes a weight reading, and the hx711 converts the load cell's tiny electrical signal into a readable weight value. The pico w then uses that value to either keep waiting or turn on the solenoid valve, depending on how heavy the waterer currently is. Once it gets light enough, the valve turns on, and the pico w checks every half of a second if the weight of the waterer is at its fill threshold. Once that threshold is reached, it then turns off the valve, and repeats the whole process.

Code
---
&nbsp;&nbsp;&nbsp;&nbsp;The micropython program remotely installed on the pico w controls the entire system. When the pico w gets power and starts the program, it turns off its wifi capabilities to lower power consumption, sets the physical pins on the hardware, and calibrates the load cell. It then enters a continuous loop, reading the weight every 15 minutes, and responding accordingly. If the weight is above a certain threshold, it will do nothing, and wait another 15 minutes. But if the weight is too low, it will turn on the water valve, and start a timer. It will turn off the water if one of two things happen: The weight of the waterer is heavy enough, or; the water valve has been running for more than 75 seconds. If it turns off the valve because it reached the proper weight, it will simply repeat the process. However, if it turns off because it has been running for over 75 seconds, something must be wrong because it should take no longer than 60 seconds for it to fill the waterer. If this happens, the entire program will enter a safety shutoff loop. Instead of taking weight readings, it will simply stay in a constant loop of it sleeping for 15 minutes, do nothing, and then sleep again. This is a very important piece to the program because it stops the waterer from not turning off and wasting water.  

&nbsp;&nbsp;&nbsp;&nbsp;The program's last feature is a way that the water valve can be manually controlled. A momentary push button that is wired to the pico w allows this to happen. When pressed, the valve turns on. When it is let go, the valve turns off. Pressing the button also resets the safety shutoff system. In theory, this button should work great. However, there was one issue. Whenever the pico w was in sleep mode, it wouldn't recognize when the button was pressed because it was mostly powered off and it would wake up for only a split second every 15 minutes to check the weight. To fix this problem, I had the pico w do something a little bit different when sleeping. It would sleep for one second, check if the button was pressed, and then repeat. This way, it could still be sleeping for 15 minutes, but would also respond when the button was pressed. 
