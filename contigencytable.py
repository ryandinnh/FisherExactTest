import pandas as pd
cardiac = pd.read_csv("/cardiac.csv")

#2x2 contingency table
table = pd.crosstab(cardiac['gender'], cardiac['hxofHT']==0, rownames=['Gender'], colnames=['Hypertension'])
table.index = ['Male', 'Female']
table.columns = ['No Hypertension', 'Hypertension']
print(table)
