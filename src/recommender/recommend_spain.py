import pandas as pd
from src.features.geo import compute_distance_to_user


def get_difficulty_priority(user_level):
    """
    Define difficulty priority order depending on user level.
    """
    if user_level == "principiante":
        return ["suave", "intermedia", "dura"]
    elif user_level == "intermedio":
        return ["intermedia", "suave", "dura"]
    else:  # avanzado
        return ["dura", "intermedia", "suave"]


def recommend_segments(
    user_lat,
    user_lon,
    user_level,
    max_distance_km=120,
    max_results=5
):
    df = pd.read_csv("data/processed/spain_segments_features.csv")

    # Calcular distancia al usuario
    df = compute_distance_to_user(df, user_lat, user_lon)

    # Filtrar solo por cercanía
    df = df[df["distance_to_user_km"] <= max_distance_km]

    # Asignar prioridad según nivel
    priority_order = get_difficulty_priority(user_level)
    priority_map = {level: i for i, level in enumerate(priority_order)}

    df["difficulty_priority"] = df["difficulty_level"].map(priority_map)

    # Ordenar:
    # 1. Por prioridad de dificultad (menor = mejor)
    # 2. Por cercanía
    df = df.sort_values(
        by=["difficulty_priority", "distance_to_user_km"],
        ascending=[True, True]
    )

    return df.head(max_results)
