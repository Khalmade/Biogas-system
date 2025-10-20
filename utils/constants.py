# Lower Heating Values and efficiencies of fuels
lhv_lpg = 45.5  # MJ/kg
lhv_charcoal = 29.6 # MJ/kg
efficiency_lpg = 0.55
efficiency_charcoal = 0.20

biogas_energy_content = 20 # MJ/m³ biogas
biogas_stove_efficiency = 0.55

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

# Constants for sizing
digester_hydraulic_retention_time = 30  # days
design_buffer = 1.2
reactor_slurry_target = 0.08           # 8% TS (Energypedia)