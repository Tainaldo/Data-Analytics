import pandas as pf

df = pf.read_csv("IMDb movies.csv")
df = df['Genre'].apply(lambda member: "Action" in member)
print(df)