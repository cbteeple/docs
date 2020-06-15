---
layout: default
title: CR10s Upgrades (v2.0)
permalink: /3d_printing/upgrades
parent: 3D Printing
nav_order: 2
font_awesome: "fas fa-terminal"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}
{: .no_toc }


### My Customizations
{: .no_toc }

1. TOC
{:toc}

---

## Base Model - CR-10s

<img alt="My CR-10s 3D printer"
     src="{{ "assets/img/printer_wide.jpg" | absolute_url }}"
     class="gallery gallery-4to3-tall" />
<img alt="My CR-10s 3D printer"
     src="{{ "assets/img/printer_zoom.jpg" | absolute_url }}"
     class="gallery gallery-4to3-wide" />


## Motor Drivers + Main Board

<img alt="The SKR 1.4 board from BigTreeTech has a 32-bit MCU and fully configured internal routing for UART motor driver signals"
     src="{{ "assets/img/skr1_4_board.jpg" | absolute_url }}"
     class="gallery gallery-33"/>
<img alt="Testing the board with my printer before fully mounting it"
     src="{{ "assets/img/skr1_4_test.jpg" | absolute_url }}"
     class="gallery gallery-33"/>
<img alt="The board fits snuggly in the CR-10 case."
     src="{{ "assets/img/skr1_4_install.jpg" | absolute_url }}"
     class="gallery gallery-33"/>

I was tired of how loud the CR10s is out of the box, so I figured I could quiet it down with some nice Trinamic motor drivers. However, Creality designed thier own board for the CR10s with built-in motor drivers (pretty much the cheapest ones available). After playing around with an extra RAMPS 1.4 main board with an 8-bit Arduino Mega 2560 I had laying around, I decided to spring for a new 32-bit board (the SKR 1.4).

For super-quiet motors, I chose the TMC2208 stepper driver package from Trinamic becasue of its simple 1-wire UART connection and native 256 microstepping capabillities. I bought the driver boards from BigTreeTech, and The SKR 1.4 board already has internal routing for UART (and SPI) to each of the motor driver sockets, so this was a breeze to set up.

However, replacing the board caused a new issue: the stock Creality LCD didn't work with my new board. I had an extra Reprap Discount Full Graphic Screen that came with my extra RAMPS 1.4 board, but guess what: The holes in the stock CR10s case don't quite line up with the new screen.


## Face Plate for RepRapDiscount LCD
Since the new LCD didn't fit, I needed to make a new face plate. I decided to design one that snaps into place in the old cutout where the LCD use to sit. You can find the [part on Thingiverse](https://www.thingiverse.com/thing:4132276)

<img alt="Custom face plate for the RepRapDiscount LCD"
     src="{{ "assets/img/faceplate_zoom.jpg" | absolute_url }}"
     class="gallery gallery-4to3-tall" />
<img alt="My custom boot screen is lookin' nice!"
     src="{{ "assets/img/teeprint.jpg" | absolute_url }}"
     class="gallery gallery-4to3-wide" />

## Firmware
### Enable TMC2208 Drivers on the SKR 1.4

I followed the [instructions for the SKR 1.4 by BigTreeTech](https://github.com/bigtreetech/BIGTREETECH-SKR-V1.3/tree/master/BTT%20SKR%20V1.4) to set up Marlin on the SKR 1.4 with the TMC2208 drivers configured in UART mode. This turned out to be pretty straightforward, but rather lengthy:
1. Install VSCode
2. Installed the PlatformIO plugin for VSCode (this allows you to compile Marlin for 32-bit boards)
3. Clone [Marlin 2.0](https://github.com/MarlinFirmware/Marlin/tree/2.0.x)
4. Copy the boards and pins files for the SKR from [BigTreeTech's github repo](https://github.com/bigtreetech/BIGTREETECH-SKR-V1.3/tree/master/BTT%20SKR%20V1.4/Firmware/Marlin-bugfix-2.0.x-SKR-V1.4/Marlin/src)
5. Set up `platformio.ini` within Marlin with `env_default = "LPC1768"`
6. Copy the example config files for the CR-10s
7. Modify `configuration.h`:
    ```cpp
    #define SERIAL_PORT -1
    #define SERIAL_PORT_2 0
    #define MOTHERBOARD BOARD_BTT_SKR_V1_4 
    ```
8. Modify `configuration_adv.h` to set up the TMC2208 drivers
    - Set motor currents
    - Set the number of native microsteps to use (default=16 for CR-10s)
    - Don't forget to modify the steps_per_unit in `configuration.h`. These numbers assume 16 microsteps in the default CR-10s config.
9. Compile and drag the firmware to the sd card on the SKR 1.4 board
10. Manually restart.

### Boot Screen
After all of that nonsense getting Marlin to work, I figured I deserved a custom boot screen to commemorate all the hard work I've put into the printer so far. I followed these steps:

1. Design the boot screen based on the instructions found on [this blog post](http://community.robo3d.com/index.php?threads/custom-boot-screen-for-marlin-and-full-graphics-lcd.17221/)
2. Use Marlin's [Bitmap to C/C++ Converter](http://marlinfw.org/tools/u8glib/converter.html)
    - Select the "**Boot**" option
3. Replace the `_bootscreen.h` file with this new one.
4. Hack the Marlin Firmware to only show this new boot screen
    - By Default, Marlin will only has options to show Marlin's default boot screen, show a custom screen in addition to the marlin screen, or show no boot screen.
    - I obviously want to keep the boot sequence short, so I added another flag to the boot screen library that you can add in the _configuration.h_ that disables the marlin boot screen.



## Direct Drive Extruder
I designed my own remix of a model on [Thingiverse]()

My changes included:
- Simplifying the support braces into one chamfer (to clear up space for the BLTouch sensor mount)
- Correcting errors in the mounting hole positions and sizes 



## BL Touch
I used a model by [GuillaumeRvs on Thingiverse](https://www.thingiverse.com/thing:2994381/comments).

This also reqired some firmware changes as well

- Modify `configuration.h`:
    ```cpp
    // Use BLTouch for homing the z-axis
    #define USE_PROBE_FOR_Z_HOMING

    // Define the BLTouch sensor
    #define BLTOUCH

    #define NOZZLE_TO_PROBE_OFFSET { -40, -10, 0 }      // Probe offset from the nozzle
    #define PROBING_MARGIN 40                           // Keep the probe away from bed edges
    #define XY_PROBE_SPEED 12000                        // Travel fast (200mm/s)
    #define Z_PROBE_SPEED_FAST (30*60)                  // Probe fast
    #define Z_PROBE_SPEED_SLOW (Z_PROBE_SPEED_FAST / 2) // Slow speed is half of fast speed

    #define Z_CLEARANCE_DEPLOY_PROBE   15 // Z Clearance for Deploy/Stow
    #define Z_CLEARANCE_BETWEEN_PROBES  5 // Z Clearance between probe points
    #define Z_CLEARANCE_MULTI_PROBE     2 // Z Clearance between multiple probes

    #define AUTO_BED_LEVELING_BILINEAR    // Enable biliner bed leveing
    #define GRID_MAX_POINTS_X 5           // Use 5x5 grid of points
    #define GRID_MAX_POINTS_Y GRID_MAX_POINTS_X

    #define Z_SAFE_HOMING // Only home Z when X and X are homed
    ```

- Modify `configuration_adv.h`:
```cpp
    //Use "HIGH SPEED" mode for probing.
    #define BLTOUCH_HS_MODE
```