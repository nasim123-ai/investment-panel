import pandas as pd
file_path = 'projects.xlsx'
df = pd.read_excel(file_path)
for index, row in df.iterrows():
    print(f"ردیف {index+1}: نام پروژه = {row['نام پروژه']}")
    