# My-hackpad
A custom macropad I designed from scratch for Hack Club's Hackpad program. It's a small programmable keypad for shortcuts and macros, built to learn PCB design, embedded firmware, and CAD along the way.


## Features
 
- programmable keys with remappable macros
- Custom PCB designed in KiCad
- Custom firmware ([QMK / KMK])
- Custom 3D-printable case designed in Fusion 360 
- [OLED display / rotary encoder.]



## Images
 
| Schematic | PCB | Case |
|-----------|-----|------|
| ![Schematic](images/schematic.png) | ![PCB](images/pcb.png) | ![Case](images/case.png) |


 ## Bill of Materials
9x Cherry MX Switches
1x XIAO RP2040
9x Blank DSA Keycaps
9x 1N4148 Diodes.
4x M3x16 Bolt
4x M3 Heatset
1x OLED display
1x rotary encoder
1x case base
1x case top


## Repo Structure
 
```
.
├── pcb/         # EasyEDA schematic and board files
├── firmware/    # Microcontroller code
├── case/        # CAD files and STL/STEP exports
├── images/      # Screenshots and renders
└── README.md
```
