import pandas as pd
import numpy as np
file = 'data/Houehold_Survey_Results.xlsx'
pd.read_excel(file)
df = pd.read_excel(file, sheet_name='Survey Results')
df.head()