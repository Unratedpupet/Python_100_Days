import pandas as pd

df = pd.read_csv("weather_data.csv")


# day | temp | condition
print(df["temp"])