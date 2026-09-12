import pandas as pd 
import matplotlib.pyplot as plt 
print("--- PORTFOLIO PROJECT 01: MARC SHOP ---") 
xls = pd.ExcelFile("marc.xlsx") 
print(f"Sheets: {xls.sheet_names}") 
df = pd.read_excel(xls, sheet_name=0) 
print(f"Rows: {len(df)} Columns: {list(df.columns)}") 
print(df.head()) 
print(df.describe(include='all')) 
