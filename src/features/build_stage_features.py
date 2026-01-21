import pandas as pd


def build_stage_features(df):
    """
    Add training-related features to stages.
    """
    df = df.copy()

    # Clasificación simple de entrenamiento
    df["training_focus"] = df["stage_type"].map({
        "flat": "llano_potencia",
        "tt": "contrarreloj",
        "rolling": "ritmo_sostenido",
        "mountain": "escalada"
    })

    # Duración estimada (asumiendo 38 km/h media)
    df["estimated_duration_h"] = df["distance_km"] / 38

    return df
