# 🌱🏡 Biogas System for Wumba District

## 📖 Project Overview  
This project models a **small-scale biogas system** designed to meet the cooking needs of **20 households in the Wumba district, Abuja, FCT Nigeria**.  
It integrates **community-level data collection**, **data analysis**, and **system design** to demonstrate how local waste resources can be transformed into sustainable energy.  

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
- Get values for → daily cooking fuel use, farm waste, food waste, kitchen waste.  
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
- Volatile Solids: 80%
- Feedstock TS fractions: kitchen 20%, cow dung 12%, meat waste 25%.  
- Slurry target TS: 8%.  
- HRT = 30 days, safety buffer ×1.2.  

---

## 📊 Summary of Results:

| Parameter                | Value        | Notes                                                |
|--------------------------|--------------|------------------------------------------------------|
| Households surveyed      | 20           | Wumba District                                       |
| Total useful energy      | ~233.6 MJ/day| Based on the efficiency of the cooking fuels         |
| Daily cooking fuel need  | ~9.21 kg LPG | Based on survey data and LPG/charcoal equivalence    |
| Daily biogas need        | ~21.2 m³/day | Based on the useful energy need and stove efficiency |
| Feedstock available      | ~116.5 kg/day| Total of Kitchen + cow dung + meat waste             |
| Biogas production        | ~25.3 m³/day | Using kitchen, cow dung, meat biogas yields from lit.|
| Digester design volume   | ~13.4 m³     | HRT, 30-day retention time, TS 8%, 1.5× safety factor|

---

**✅ Conclusion**:
- The biogas potential from the available waste meets the community's energy needs.


