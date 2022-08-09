import pandas as pd

movies_df = pd.read_csv("IMDb movies1.csv", dtype={'year':int})
print(movies_df.head(5))