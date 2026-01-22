import pandas as pd
from src.data.loader import load_vuelta_climbs
from src.features.build_climb_features import build_climb_features


if __name__ == "__main__":
    df = load_vuelta_climbs("data/raw/vuelta_hardest_climbs.csv")

    df_features = build_climb_features(df)

    df_features.to_csv(
        "data/processed/vuelta_climbs_features.csv",
        index=False
    )

    print("Dataset de puertos procesado correctamente")
