# RUBIX 2.0 - VEX IQ Rubik's Cube Solver


## [YouTube video](https://www.youtube.com/watch?v=L6gSuM-JHgo)

![](https://img.youtube.com/vi/L6gSuM-JHgo/0.jpg)

> Following RUBIX, this is a Rubik's cube solver robot based on VEX IQ and Android. A custom Android app scans the cube and finds the solution (max 24 moves). Since the IQ Brain does not have Bluetooth capabilities, the app communicates with it using light pulses. The robot acks the app by waving a piece in front of the smartphone's proximity sensor.
>
> The communication is the bottleneck of the system, as you can guess. Maximum solving time is less than one minute.
>
> The mechanics are self-inspired by my LEGO Rubik's UTOPIA robot, which was the first LEGO MINDSTORMS NXT robot that could solve a Rubik's cube in 2007.
> 
> More at [https://robotics.benedettelli.com/vex-iq-rubik-solver](#Webpage).


## [Webpage](https://robotics.benedettelli.com/vex-iq-rubik-solver)


### Rubik + VEX = RUBIX

In February 2014 I was invited as a VEX IQ Super User at the VEX World Championship in Anaheim California that took place at the end of April. At that time, the VEX IQ system was completely new to me, so it took few days to get very confident with the building system. The system allows you to build big and strong robots very fast. Once I tamed the toolkit, I decided that the best robot that could prove the capabilities of the new toolkit was a VEX IQ Rubik’s cube solver robot. While the temptative [RUBIX 1.0](https://www.youtube.com/watch?v=bGxpXlIaIaA) robot was based on great David Gilday’s [Mindcuber](http://www.mindcuber.com), the mechanism of the version 2.0 shown here is much faster, being able to solve any cube in under a minute. It is inspired to the very first and famous LEGO MINDSTORMS NXT Rubik’s cube solver. And yes, it can handle the dreadful [superflip](http://www.speedsolving.com/wiki/index.php/Superflip).


### The VEX IQ system

[VEX IQ](http://www.vexrobotics.com/vexiq) is an educational robotics system which is quite new. It was launched in October 2013, about at the same time as the EV3. The system includes plastic elements, metal axles, gears, wheels, treads, servo motors, sensors, and the [VEX IQ brain](http://www.vexrobotics.com/vexiq/products/brain-g.html), a microcomputer with 12 I/O ports and backlit display. The [VEX IQ smart motors](http://www.vexrobotics.com/vexiq/products/228-2560.html) have a very precise PID loop controller on board. For a very good review of the VEX IQ system, check out [this post at Bot Bench](http://botbench.com/blog/2014/05/18/vex-iq-modular-robotics-system-for-stem).


### How it works

The VEX IQ brain is programmed using [ROBOTC](http://www.robotc.net) and controls the movements of the robot and reads the sensors, while the cube is scanned and solved by a custom Android app running on a Samsung Galaxy SL. I am using the same app for my latest LEGO MINDSTORMS Rubik’s cube solver robots as well.

The biggest challenge in realizing this project was making the VEX IQ system communicate with an Android app. The VEX IQ brain is not Bluetooth enabled, so I came up with the following work-around. The robot can just send acknowledgements to the app by waving a piece in front of the phone proximity sensor. The phone, in return, must send the sequence of the solving moves back to the robot. So I implemented a synchronous 2-bit base-6 parallel communication channel flashing colors on the screen of the smartphone and reading them using the VEX IQ color sensors. This way of communication is quite slow, estimated around 12 bauds: It takes 10 seconds (sped up in the video) to send a solution of 21 moves to the robot. I thought of many other ways to implement the communication (creating a custom Bluetooth adapter for example), but the current solution works out of the box, without modifying or creating any component. The communication channel is the bottleneck and the pitfall of the robot, though it is the novel feature that makes me pretty proud of it. Someone at the VEX World Championship, referring to the communication channel, told me “you made the impossible“. A bit over-the-top, but gives you the idea.


### Future developments

The VEX IQ brain has a slot for the [radio module](http://www.vexrobotics.com/vexiq/products/228-2621.html) that allow you to make [remote controlled robots](http://www.vexrobotics.com/vexiq/products/vex-iq-controller.html). I hope VEX will enrich the IQ system with a Bluetooth module, or release the full SDK and HDK documentation to develop custom sensors using the I2C bus.
