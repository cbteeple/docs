---
layout: default
title: CR10s Upgrades (2022)
permalink: /3d_printing/upgrades2022
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

## E3D Hemera Hotend Upgrade

[<i class="fas fa-link"></i> View on PrusaPrinters (Coming Soon...)](){: .btn .btn-outline}
[<i class="fas fa-link"></i> View on Thingiverse (Coming Soon...)](){: .btn .btn-outline}

[<i class="fas fa-file-pdf"></i> View Writeup]( {{ "assets/files/hemera_writeup.pdf" | absolute_url }} ){: .btn .btn-primary}

The [Hemera Direct-Drive hotend/extruder](https://e3d-online.com/products/e3d-hemera-direct-kit-1-75mm) from E3D is a top-of-the line hotend! That is... if you can find a way to mount it rigidly to your printer. After much searching, I could not find a mounting plate for the CR-10 that was rigid enough and sufficiently modular for my tastes. Thus, the Teebert Industries Hemera Mount was born!


<img alt="The Teebert Industries Hemera Mount"
     src="{{ "assets/img/hemera/4_add_bltouch.jpg" | absolute_url }}"
     class="gallery gallery-50"/>
<img alt="The complete hemera upgrade!"
     src="{{ "assets/img/hemera/10-final.jpg" | absolute_url }}"
     class="gallery gallery-50"/>



### Pre-Build Notes

This project came about because I tried to use the mounting plate from E3D's [CR-10 Upgrade guide (Version 1)](https://e3d-online.zendesk.com/hc/en-us/articles/360017637478-Hemera-Creality-CR10-Upgrade-Guide-Edition-1-), but their design has a critical flaw: The mounting plate is extremely compliant due to how far the Hemera ends up hanging over the side of the CR-10's original X-carriage. This ends up producing horrible prints because the height of the nozzle is extremely inconsistent (squishing layers randomly all the time), and any acceleration causes vibrations in the nozzle.

I then searched for more mounting options. First I looked at Version 2 of [E3D's upgrade guide for the CR-10 and Ender 3](https://e3d-online.zendesk.com/hc/en-us/articles/360018062117-Hemera-Ender-3-V2-Ender-3-CR10-CR10-V2-Upgrade-Guide-Edition-2-), but this very sparse mount still looks too compliant. I also found several designs online while scouring Thingiverse and PrisaPrinters, but nothing really seemed refined enough. The closest thing to what I was looking for was [this plate by Aaen on PrusaPrinters](https://www.prusaprinters.org/prints/21817-ender-3-compact-hemera-mount-plate-with-bltouch), where the Hemera is mounted firmly to the plate with most of the weight supported by the steel X-carriage. However, the attachment points to the X-carriage are very thin in this design (1 mm), and I am a fan of modality, so I'd prefer to make the BLTouch mount as a separate part. 


### Off-The-Shelf Hardware

This mount is designed to re-use most of the hardware from a standard CR-10 or Ender 3 X-carriage. However, there are a few fasteners you'll need to scrounge up:

- 5x **M3 x 8mm screws** (4 of these come with the Hemera)
- 4x **M3 square nuts** (2 of these come with the Hemera)
- 2x **M3 x 6mm screws** (for the BLTouch mount)
- A Few **M3 washers**
- 1x **M5 washer**
- 40mm length of cable wrap.
- 2x Zip ties

Additionally, if you choose to use the fan duct provided by E3D for the part cooling fan, you will also need a 5015 Blower fan that runs at the correct voltage for you system (12 V or 24 V), two M3 x 10mm Screws, and one M3x 20mm screw.


### Printed Parts

There are a few printed parts you'll need:

- Main mounting plate
- BLTouch mount OR simple x-axis extension
- Your choice of part cooling fan duct. Many options exist for cooling ducts, but I prefer the "_Ender_3_V2_Duct_" provided by E3D in an [only partially relevant tutorial](https://e3d-online.zendesk.com/hc/en-us/articles/360018062117-Hemera-Ender-3-V2-Ender-3-CR10-CR10-V2-Upgrade-Guide-Edition-2-)

<img alt="Parts to print (Cooling duct not shown, but you'll need that too.)"
     src="{{ "assets/img/hemera/parts_to_print.jpg" | absolute_url }}"
     class="gallery"/>


### Assembly

The assembly process is relatively complex. Here are a smattering of images from the process. For in-depth instructions, [see my writeup]({{ "assets/files/hemera_writeup.pdf" | absolute_url }} ).


<img alt="Start with the mounting plate"
     src="{{ "assets/img/hemera/1_start_with bracket.jpg" | absolute_url }}"
     class="gallery gallery-50"/>
<img alt="Start with the mounting plate"
     src="{{ "assets/img/hemera/3-screw.jpg" | absolute_url }}"
     class="gallery gallery-50"/>


<img alt="Add the Hemera"
     src="{{ "assets/img/hemera/2_add_hemera_nofan.jpg" | absolute_url }}"
     class="gallery gallery-50"/>
<img alt="Add the Hemera"
     src="{{ "assets/img/hemera/5-attach-hemera.jpg" | absolute_url }}"
     class="gallery gallery-50"/>


<img alt="Press in the original X-Carriage from the CR-10"
     src="{{ "assets/img/hemera/3_add_x_carraige.jpg" | absolute_url }}"
     class="gallery gallery-50"/>
<img alt="Press in the original X-Carriage from the CR-10"
     src="{{ "assets/img/hemera/7-carriage.jpg" | absolute_url }}"
     class="gallery gallery-50"/>


<img alt="Add the BLTouch"
     src="{{ "assets/img/hemera/4_add_bltouch.jpg" | absolute_url }}"
     class="gallery gallery-50"/>
<img alt="Add the BLTouch"
     src="{{ "assets/img/hemera/8-fan_bltouch.jpg" | absolute_url }}"
     class="gallery gallery-50"/>
