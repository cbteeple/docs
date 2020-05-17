---
layout: default
title: Gaming
has_children: false
permalink: gaming
nav_order: 8
font_awesome: "fas fa-gamepad"
---


# <i class="{{ page.font_awesome }}"></i> {{ page.title }}
{: .no_toc }

1. TOC
{:toc}

---

## PC Gaming with Nintendo JoyCons

### Set up the JoyCons
Following a [guide from Windows Central](https://www.windowscentral.com/how-use-nintendo-switch-joy-cons-and-game-windows-pc) to set things up.

1. Download and install [**vJoy**](http://vjoystick.sourceforge.net/site/). This provides the device driver needed by the joycons.
2. Run the **Configure vJoy** program, and set up two devices:
<img alt="Configure Device 1"
     src="{{ "assets/img/vjoy_setup.png" | absolute_url }}"
     class="gallery gallery-50" />
<img alt="Configure Device 2"
     src="{{ "assets/img/vjoy_setup_single.png" | absolute_url }}"
     class="gallery gallery-50" />

3. Once configured, you'll need to restart your computer.
4. Clone [**JoyCon-Driver**](https://github.com/fossephate/JoyCon-Driver) from _fossephate_ on github
5. [Pair your JoyCons](https://www.digitaltrends.com/gaming/how-to-connect-a-nintendo-switch-controller-to-a-pc/) to your computer using Bluetooth by pressing and holding the "pair" button until the LEDs start blinking.
<img alt="Configure Device 2"
     src="{{ "assets/img/joycon-edge.jpg" | absolute_url }}"
     class="gallery gallery-100" />

6. Navigate to **joycon-driver >> build >> Win32 >> Release** and run **joycon-driver.exe**. You might need to [override the high-dpi settings](https://www.windowscentral.com/how-change-high-dpi-settings-classic-apps-windows-10-april-2018-update) in order to make the program look right.
7. Click **Start**, and let the program run. Your joycons should vibrate when they are detected.
8. Congrats! Now you can use your joycons as controllers for games!

### Emulate an XBOX controller
Some games won't work natively with joycons, so you have to map the buttons and joysticks to the corresponding XBOX controller buttons.

1. Download [**x360ce**](https://www.x360ce.com/), an emulation program that will create the correct button mapping files.
2. Connect your JoyCons per the instructions above. Be sure to check "Combine JoyCons" when running **JoyCon-Driver**.
3. Set up all the buttons (you can use the "record" option to speed things up). This will generate two new files in the same folder as where you put x360ce.
5. For each game, copy all three files into the same folder as the game's excecutable (Per the installation instructions from x360ce).
6. That's it. The buttons will be mapped, and your combined JoyCons will behave like an XBOX controller!