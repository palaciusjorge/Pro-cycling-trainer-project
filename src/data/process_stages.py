import pandas as pd
from src.features.build_stage_features import build_stage_features


if __name__ == "__main__":
    df = pd.read_csv("data/raw/spain_stages.csv")

    df_features = build_stage_features(df)

    df_features.to_csv(
        "data/processed/spain_stages_features.csv",
        index=False
    )

    print("Dataset de etapas procesado correctamente")
