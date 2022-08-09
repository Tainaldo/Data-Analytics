import pandas as pd

movies_df = pd.read_csv("IMDb movies1.csv", dtype={'year':int})
new_movies_df = movies_df[movies_df['year'] >= 2015]

print(new_movies_df)