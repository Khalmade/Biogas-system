# 🌱🏡 Biogas System for Wumba District

## 📖 Project Overview  
This project models a **small-scale biogas system** designed to meet the cooking needs of **20 households in the Wumba village district in Abuja, FCT Nigeria**.  
It uses **community-level data collection**, **data analysis**, and **system design** to demonstrate how local waste resources can be transformed into sustainable energy.  

---

## 🎯 Objectives
1. Survey households to estimate **daily cooking energy demand** and available kitchen waste.
2. Survey community abattoir, cattle rearers, fruit and vegetable sellers to also estimate the animal, fruit and vegetables wastes and dung that can be obtained.
3. Calculate the biogas potential from available waste sources.
4. Model a **biogas system** using anaerobic digestion of household waste.  
5. Size the biogas digester and the type required to meet energy needs of the households.

---

## 🔬 Methodology  

### 1. Community Data Collection  
- Survey 20 households, farm, markets in Wumba
- Get values for → daily cooking fuel use, market waste, food waste, kitchen waste.  
- Convert waste → useful energy potential (kg waste → m³ CH₄).  

### 2. Biogas Yield Calculation  
- Tools: **Python**.  
- Inputs: waste feedstock (composition), constants from literature, digester conditions.  
- Outputs: methane yield, digestate.  

### 3. Energy System Design  
- Convert methane yield → cooking gas (LPG/Charcoal equivalent).  

### 4. Analysis  
- Compare household needs vs the system output.  

---

## 📊 Outputs  
- Biogas production potential (m³/day) for 20 households.  
- Dimensions for the biogas digester.  
- Biogas system model.    

---

## 🛠 Tools Used  
- **Excel** → Household survey data
- **Python** → Pandas, NumPy  

---

## 📌 Impact  
- Demonstrates how these rural communities can use their **local waste → clean energy**.  
- Provides an **affordable alternative** to cooking gas and other fuels.  
- Offers a **scalable model** for sustainable energy access in Africa.

---

## 📝 Assumptions:  
- Literature biogas yields (m³/kg fresh waste).
- Slurry target TS: 8%.  
- HRT = 30 days, safety buffer ×1.2.  

---

## 📊 Summary of Results:

| Parameter                | Value         | Note                                                |
|--------------------------|-------------- |------------------------------------------------------|
| Households surveyed      | 20            | Wumba village district                               |
| Fruit/vegetable sellers  | 12            | Wumba market survey                                  |
| Total kitchen waste      | 36.5 kg/day   | Fresh kitchen waste                                  |
| Orange peels             | 32.35 kg/day  |
| Pineapple peels          | 48 kg/day     |
| Watermelon_peel          | 36 kg/day     |
| Vegetable wastes         | 22 kg/day     |
| Cow dung                 | 405 kg/day    | Based on estimate of cow herd and literature on dung |
| Meat (beef) wastes       | 18.5          | Abattoir                                             |
| Total useful energy      | ~232 MJ/day   | Based on the efficiency of the cooking fuels         |
| Daily biogas need        | ~21.09 m³/day | Based on useful energy need and stove efficiency     |
| Biogas production        | ~21.71 m³/day | Using biogas yield values from literature            |
| Total Solids in Digester | ~135.32 kg/day| TS(%) of all waste streams                           |
| Feedstock available      | ~116.5 kg/day | Total of Kitchen + cow dung + meat waste             |
| Digester design volume   | ~60.89 m³     | 30-day retention time, TS 8%, 1.2× safety factor     |
| Digester diameter        | ~5.37 m³      | $V = \frac{\pi}{4} D^2 H$.                           |
| Digester height          | ~2.69 m³      |                                                      |

---

**✅ Conclusion**:
- The biogas potential from the available waste sources in the Wumba village distrcit is sufficient to meet the cooking needs of at least 20 households surveyed.


