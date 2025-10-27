"Biogas yield potential from community waste streams in Wumba District."

import pandas as pd
# Load survey energy results
result = pd.read_csv("./analysis/Household_Survey_Analysis_with_LPG_equiv.csv")

# --- Constants (from literature) ---

#Y = biogas yield per kg of VS (m^3/kg VS)
#TS = total solids content (fraction of wet mass)
#VS = volatile solids content (fraction of total solids)
# Source: Ogur & Mbatia (2013), IntechOpen (2018), Energypedia (2023)

# Waste type constants (values from literature)
Y_kw, TS_kw, VS_kw = 0.30, 0.20, 0.80   # kitchen waste
Y_op, TS_op, VS_op = 0.23, 0.12, 0.90   # orange peel
Y_pp, TS_pp, VS_pp = 0.30, 0.18, 0.85   # pineapple peel
Y_wp, TS_wp, VS_wp = 0.30, 0.15, 0.85   # watermelon peel
Y_vw, TS_vw, VS_vw = 0.35, 0.15, 0.80   # vegetable waste
Y_mw, TS_mw, VS_mw = 0.50, 0.30, 0.90   # meat waste
Y_cd, TS_cd, VS_cd = 0.15, 0.25, 0.80   # cow dung

# --- Daily Waste Quantities (kg/day) in Wumba based on survey data---
kitchen_waste = result['Solid waste/day (Kg)'].sum()
orange_peel = 32.35
pineapple_peel = 48
watermelon_peel = 36
vegetable_waste = 22
cow_dung = 405  
meat_waste = 18.5

# --- Biogas potential function ---
def biogas_potential(mass, TS, VS, Y):
    return mass * TS * VS * Y

# --- Biogas potential for each waste ---
biogas_kw = biogas_potential(kitchen_waste, TS_kw, VS_kw, Y_kw)
biogas_op = biogas_potential(orange_peel, TS_op, VS_op, Y_op)
biogas_pp = biogas_potential(pineapple_peel, TS_pp, VS_pp, Y_pp)
biogas_wp = biogas_potential(watermelon_peel, TS_wp, VS_wp, Y_wp)
biogas_vw = biogas_potential(vegetable_waste, TS_vw, VS_vw, Y_vw)
biogas_cd = biogas_potential(cow_dung, TS_cd, VS_cd, Y_cd)
biogas_mw = biogas_potential(meat_waste, TS_mw, VS_mw, Y_mw)

# --- Totals ---
total_biogas_potential = (
    biogas_kw + biogas_op + biogas_pp + biogas_wp +
    biogas_vw + biogas_cd + biogas_mw
)

print(f"\nTotal daily biogas potential: {total_biogas_potential:.2f} m³/day")
print(f" - Kitchen Waste: {biogas_kw:.2f}")
print(f" - Fruit Peels: {biogas_op + biogas_pp + biogas_wp:.2f}")
print(f" - Vegetables: {biogas_vw:.2f}")
print(f" - Meat Waste: {biogas_mw:.2f}")
print(f" - Cow Dung: {biogas_cd:.2f}")
