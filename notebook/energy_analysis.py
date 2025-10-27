"Useful daily household energy demand based on survey data of fuel consumption."
import pandas as pd
import numpy as np
file = "./analysis/Household_Survey_Analysis.csv"
result = pd.read_csv(file)
print((result.head()))
result = result.dropna(axis=1, how='all')
print(result.head())
# Calculate daily fuel usage
result['Daily Fuel Usage (KG/day)'] = result['Fuel mass (KG)'] / result['Time taken (days)']
print(result)
# Lower Heating Values and efficiencies of fuels (source: engineeringtoolbox.com)
lhv_lpg = 45.5  # MJ/kg
lhv_charcoal = 29.6 # MJ/kg
efficiency_lpg = 0.55
efficiency_charcoal = 0.20
# Calculate Gross Energy per day
result['Gross Energy per day (MJ/day)'] = result.apply(
    lambda row: row['Daily Fuel Usage (KG/day)'] * (lhv_lpg if row['Primary Fuel'] == 'LPG' else lhv_charcoal),
    axis=1
)
# Calculate Useful Energy per day
result['Useful Energy per day (MJ/day)'] = result.apply(
    lambda row: row['Gross Energy per day (MJ/day)'] * (efficiency_lpg if row['Primary Fuel'] == 'LPG' else efficiency_charcoal),
    axis=1
)
# Calculate LPG-equivalent demand
result['LPG-equivalent demand (kg/day)'] = result['Useful Energy per day (MJ/day)'] / (lhv_lpg * efficiency_lpg)
print(result.head())
#Total LPG Fuel Required Per Day
total_fuel_required_per_day = result['LPG-equivalent demand (kg/day)'].sum()
print(f"Total LPG-equivalent fuel required per day for all surveyed households: {total_fuel_required_per_day:.2f} kg LPG/day")
#Total Useful Energy Required Per Day
total_useful_energy_per_day = result['Useful Energy per day (MJ/day)'].sum()
print(f"Total useful energy required per day for all surveyed households: {total_useful_energy_per_day:.2f} MJ/day")
result.to_csv("./analysis/Household_Survey_Analysis_with_LPG_equiv.csv", index=False)
#Biogas Equivalent Required Per Day (source: energypedia)
biogas_energy_content = 20 # MJ/m³ biogas
biogas_stove_efficiency = 0.55
def required_biogas_yield(total_useful_energy_per_day, biogas_energy_content, biogas_stove_efficiency):
    return total_useful_energy_per_day / (biogas_energy_content * biogas_stove_efficiency)
Wumba_biogas_need = required_biogas_yield(total_useful_energy_per_day, biogas_energy_content, biogas_stove_efficiency)
print(f"\nTotal daily biogas need : {Wumba_biogas_need:.2f} m^3/day")
