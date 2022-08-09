import pandas as pf

df = pf.read_csv("IMDb movies.csv")
df = df["Genre"].apply(lambda m : m.split(", ")).explode().unique()
