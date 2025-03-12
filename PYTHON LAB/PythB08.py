import pandas as pd
d=pd.read_excel("C:/Users/admin/Desktop/Excel/PandasMarks.xlsx")
df=pd.DataFrame(d)
print(df)
df['Total_Marks']=df[['Hindi','English','Maths','Science','Social']].sum(axis=1)
print("\nTotal for each student\n",df['Total_Marks'])


