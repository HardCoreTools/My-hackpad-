# My-hackpad
A custom macropad I designed from scratch for Hack Club's Hackpad program. It's a small programmable keypad for shortcuts and macros, built to learn PCB design, embedded firmware, and CAD along the way.


<img src="images/Screenshot 2026-09-30 163131.png" width="360">


## Features
 
- programmable keys with remappable macros
- Custom PCB designed in KiCad
- Custom firmware ([QMK / KMK])
- Custom 3D-printable case designed in Fusion 360 
- [OLED display / rotary encoder.]



## Images
 
| Schematic | PCB | Case |
|-----------|-----|------|
| <img src="images/Screenshot 2026-09-30 172713.png" width="360"> | <img src="images/Screenshot 2026-09-30 172844.png" width="360"> | <img src="images/Screenshot 2026-09-30 163131.png" width="360"> |

[![View PCB on KiCanvas](https://hack.club/pcb-badge)]([https://kicanvas.org/?repo=https://github.com/<OWNER>/<REPOSITORY>/tree/main/pcb](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2FHardCoreTools%2FMy-hackpad-%2Ftree%2Fmain%2Fpcb))


 ## Bill of Materials
- 9x Cherry MX Switches
- 1x XIAO RP2040
- 9x Blank DSA Keycaps
- 9x 1N4148 Diodes.
- 4x M3x16 Bolt
- 4x M3 Heatset
- 1x OLED display
- 1x rotary encoder
- 1x case base
- 1x case top


## Repo Structure
 
```
.
├── pcb/         # EasyEDA schematic and board files
├── firmware/    # Microcontroller code
├── case/        # CAD files and STL/STEP exports
├── images/      # Screenshots and renders
└── README.md
```
