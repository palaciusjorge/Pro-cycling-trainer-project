from src.features.build_climb_features import build_climb_features

df = build_climb_features("data/raw/vuelta_hardest_climbs.csv")
print(df.head())

