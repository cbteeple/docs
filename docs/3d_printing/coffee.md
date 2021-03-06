---
layout: default
title: Electric Coffee Grinder
permalink: /3d_printing/coffee
parent: 3D Printing
nav_order: 0
font_awesome: "fas fa-mug-hot"
---

# <i class="{{ page.font_awesome }}"></i> DIY Electric Burr Grinder
{: .no_toc }

{: .fs-5}
by [TeepSmart Inc.](http://teepsmart.cbteeple.com)



<img alt="JavaPresse Manual Burr Grinder"
     src="{{ "assets/img/coffee/grinder.jpg" | absolute_url }}"
     class="gallery gallery-50" />
<img alt="TeepSmart Electric Burr Grinder"
     src="{{ "assets/img/coffee/working.png" | absolute_url }}"
     class="gallery gallery-50" />

{: .fs-5}
Ditch that exhausting handle!

High-quality electric burr grinders are expensive, but manual ones are much more affordable. I wanted to see if I could turn my manual grinder into an electric one.

### Make It!
{: .no_toc }

1. TOC
{:toc}

---

## How it works

{: .fs-5}
I little backpack for your burr grinder.

All I really did was connect a motor to the grinder via a timing belt and pulleys.

<img alt="Electricals Assmbly"
     src="{{ "assets/img/coffee/assembly.jpg" | absolute_url }}"
     class="gallery gallery-50" />
<img alt="Super simple wiring (Make the motor turn the right direction)"
     src="{{ "assets/img/coffee/underside.jpg" | absolute_url }}"
     class="gallery gallery-50" />


## Bill of Materials

{: .fs-5}
For $86, you too can have a slow, loud, low-capacity burr grinder!

Everything in this project came from Amazon.com. When buying hobby-grade things on Amazon, you often have to buy things in packs of several (for example, you can't just buy one DC barrel jack, you have to buy a pack of 12). As such, the "_Amazon Price_" here is the price of purchasing the packs of several parts, and the "_Price for This Build_" is only for the correct number of compoenents, not counting the leftovers. You can always use the leftovers for another project (that's how you become a packrat like me)!


| Part                           | Qty | Amazon Price  | Price for This Build | Link    |
|:--------------------------------|:--:|:------:|:----------------:|:----------------------:|
| JavaPresse Manual Burr Grinder |   1| $39.95 | $39.95 | [Item](https://www.amazon.com/JavaPresse-Grinder-Conical-Brushed-Stainless/dp/B013R3Q7B2/ref=sr_1_5?crid=1WFYJVHRIQE8X&dchild=1&keywords=javapresse+manual+coffee+grinder&qid=1615042028&sprefix=javapresse%2Caps%2C182&sr=8-5) |
| Timing Pulley                  |   1 |  $6.89 |               $6.89 | [Item](https://www.amazon.com/gp/product/B0747LJJ2J/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)                                                                                                                           |
| Timing Belt                    |   1  |  $6.58 |                $6.58 |[Item]( https://www.amazon.com/gp/product/B00CMIGFY8/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                                                                                                                            |
| Bearings (1/4"x5/8"x0.196")    |   4 |  $8.95 |              $3.58 | [Item](https://www.amazon.com/gp/product/B07GT739PV/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)                                                                                                                           |
| DC Motor (12V, 50RPM)          |   1  | $15.49 |              $15.49 | [Item](https://www.amazon.com/gp/product/B07K9KPDNV/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&th=1)                                                                                                                            |
| Power Supply (24V)             |   1 |  $9.69 |              $9.69 | [Item](https://www.amazon.com/gp/product/B00L9PCJF4/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                                                                                                                            |
| DC Power Jack (Barrel Jack)    |   1 |  $7.99 |               $0.67 | [Pack of 12](https://www.amazon.com/ThreeBulls-Pieces-5-5mmx2-1mm-Female-Connector/dp/B01N8VV78D/ref=sr_1_3?dchild=1&keywords=dc+barrel+jack&qid=1615041413&sr=8-3)                                                                   |
| Power Switch                   |   1  |  $5.99 |             $1.20 | [Pack of 5](https://www.amazon.com/Magic-shell-5-Pack-Rocker-Position/dp/B07D285PLL/ref=sr_1_11?dchild=1&keywords=power+switch&qid=1615041469&sr=8-11) |
| Velcro Straps                  |   2  |  $9.55 |                $0.80 | [Pack of 24](https://www.amazon.com/gp/product/B0798L21FG/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1) |
| Neoprene Sheet                 |  1   | $15.99 |        $1.50 | [Assortment](https://www.amazon.com/gp/product/B01IC7THJ2/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) |
| M3 x 30mm Screws/Washers/Nuts               |   2  |  $0.00 |                $0.00 | [Assortment](https://www.amazon.com/VIGRUE-1110PCS-Stainless-Assortment-Tweezer/dp/B083SGJ7BD/ref=sr_1_6?dchild=1&keywords=m3+screw&qid=1615045917&sr=8-6) |
|  **Totals**                    |     | **$126.08**  |  **$86.34** |   |

## CAD for 3D Printed Parts

[<i class="fas fa-cube"></i> Check out the Fusion360 model](https://a360.co/2PFausd){: .btn .btn-primary}

I'd recommend printing this out of PETG or ABS. PLA gets soft at low enough temperatures that nothing will remain tight as the motor heats up (speaking from experience here).


## Comparison to Commercial Grinders

| Name | Description                           | Price | Link    |
|:-----|:--------------------------------------|:-----:|:--------:|
|Baratza Encore| The "highest regarded cheaper coffee grinder" | $140 |[Amazon](https://www.amazon.com/Baratza-Encore-Conical-Coffee-Grinder/dp/B007F183LK/ref=sr_1_2?dchild=1&keywords=burr+coffee+grinder+encore&qid=1615043040&s=kitchen&sr=1-2) |
|Capresso Infinity| Another "good brand" | $100 |[Amazon](https://www.amazon.com/Baratza-Encore-Conical-Coffee-Grinder/dp/B007F183LK/ref=sr_1_2?dchild=1&keywords=burr+coffee+grinder+encore&qid=1615043040&s=kitchen&sr=1-2) |
|TeepSmart Electric| The "I did it for cheaper" special | $86 | |