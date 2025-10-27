"Digester size and dimensions based on community waste input and energy demand"

import math
import pandas as pd

# Factors for digester sizing
digester_hydraulic_retention_time = 30 # from literature (days)
design_buffer = 1.2 #safety factor 

#Total Solids (TS%) in the Digester
total_solids = 135.32 #kg/day

#Reactor Slurry Target 
reactor_slurry_target = 0.08 # %target total solids fraction inside the digester slurry; energypedia (2025)
slurry_volume_needed = total_solids / (reactor_slurry_target * 1000 ) #(in m^3/day)
print(f"Slurry Volume: {slurry_volume_needed:.2f} m^3/day")

# Required digester volume based on Hydraulic Retention Time (HRT)
required_digester_volume = slurry_volume_needed * digester_hydraulic_retention_time * design_buffer
print(f"\nBiogas digester volume: {required_digester_volume:.2f} m^3")

#Calculate the digester diameter and height
import math
def digester_dimensions(volume, diameter_to_height_ratio):
    H = (4 * volume / (math.pi * (diameter_to_height_ratio ** 2))) ** (1/3)
    D = diameter_to_height_ratio * H
    return D, H

D, H = digester_dimensions(required_digester_volume, 2)
print(f"Digester Diameter (D): {D:.2f} m")
print(f"Digester Height (H): {H:.2f} m")
