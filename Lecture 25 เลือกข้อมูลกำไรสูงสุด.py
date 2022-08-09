import pandas as pd

movies_df = pd.read_csv("IMDb movies1.csv", dtype={'year':int})
new_movies_df = movies_df[movies_df['year'] >= 2015]
filtered_movies_df = new_movies_df[new_movies_df['budget'].notna() & new_movies_df['worlwide_gross_income'].notna()][["imdb_title_id",'budget','worlwide_gross_income']]
# สกุลเงิน
filtered_movies_df = filtered_movies_df['budget'].apply(lambda m: m.split( )[0]).unique()
filtered_movies_df1 = filtered_movies_df['worlwide_gross_income'].apply(lambda m: m.split([0])).unique()
print(filtered_movies_df1)