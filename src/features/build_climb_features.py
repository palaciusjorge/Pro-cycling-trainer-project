import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def build_climb_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build difficulty features for climbs.
    """

    df = df.copy()

    # Handle missing values
    df["length_km"] = df["length_km"].fillna(df["length_km"].median())
    df["avg_gradient"] = df["avg_gradient"].fillna(df["avg_gradient"].median())

    # Normalize features
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(
        df[["profile_score", "length_km", "avg_gradient"]]
    )

    df["profile_score_norm"] = scaled[:, 0]
    df["length_km_norm"] = scaled[:, 1]
    df["avg_gradient_norm"] = scaled[:, 2]

    # Difficulty score
    df["difficulty_score"] = (
        0.5 * df["profile_score_norm"]
        + 0.3 * df["length_km_norm"]
        + 0.2 * df["avg_gradient_norm"]
    )

    # Round values
    cols_to_round = [
        "profile_score_norm",
        "length_km_norm",
        "avg_gradient_norm",
        "difficulty_score"
    ]
    df[cols_to_round] = df[cols_to_round].round(2)

    # Difficulty level
    df["difficulty_level"] = pd.qcut(
        df["difficulty_score"],
        q=3,
        labels=["suave", "intermedia", "dura"]
    )

    return df
