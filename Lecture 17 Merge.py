import pandas as pd

movies_df = pd.read_csv("IMDb movies.csv")
movies_df = movies_df.describe()
print(movies_df)