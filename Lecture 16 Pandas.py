import pandas as pf

df = pf.read_csv("IMDb movies.csv")
df = df[['Title','Genre']]
df = df['Genre'].apply(lambda member : "Action" in member)
df = df[df]
print(df)