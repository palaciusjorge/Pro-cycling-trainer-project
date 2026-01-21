import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def build_climb_features(csv_path: str) -> pd.DataFrame:
    """
    Load climb dataset and build difficulty features.
    """

    df = pd.read_csv(csv_path)

    # ---- Handle missing values ----
    df["length_km"] = df["length_km"].fillna(df["length_km"].median())
    df["avg_gradient"] = df["avg_gradient"].fillna(df["avg_gradient"].median())

    # ---- Normalize features ----
    scaler = MinMaxScaler()

    scaled_features = scaler.fit_transform(
        df[["profile_score", "length_km", "avg_gradient"]]
    )

    df["profile_score_norm"] = scaled_features[:, 0]
    df["length_km_norm"] = scaled_features[:, 1]
    df["avg_gradient_norm"] = scaled_features[:, 2]

    # ---- Difficulty score ----
    df["difficulty_score"] = (
        0.5 * df["profile_score_norm"] #  Mayor peso puesto que es la puntuación otorgada por la página pro cycling stats.
        + 0.3 * df["length_km_norm"]
        + 0.2 * df["avg_gradient_norm"]
    )

    # ---- Difficulty level ----
    df["difficulty_level"] = pd.qcut(
        df["difficulty_score"],
        q=3,
        labels=["suave", "intermedia", "dura"]
    )

    return df