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
Anyone who has owned them knows that taking care of chickens can be a hassle. But for me the most annoying and time-consuming part is having to fill up their water every morning and night. And so I decided to create a system that could automatically refill it for me. There where 2 main functions that the system had to be able to perform:
1. Determine the current water level
2. Turn on/off water flow when necessary

My original thought was to use a float valve to determine the water level. However, this proved to be less than ideal due to the complications of installing one inside a chicken waterer, and the inherent potential for imprecise, inaccurate, and delayed readings. And so, I decided that instead of directly reading the water level, I could get the water's weight, and calculate how full it is that way. But what can give a weight reading that can input into a microcontroller? The answer is a load cell. A load cell can determine the amount of force applied to it and 
