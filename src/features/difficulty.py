import pandas as pd


def compute_difficulty_score(row):
    """
    Compute a difficulty score between 0 and 1 for a cycling segment.
    """

    # Normalizaciones simples (valores máximos razonables)
    distance_norm = row["distance_km"] / 25        # 25 km subida larga
    elevation_norm = row["elevation_gain_m"] / 1800  # 1800 m muy duro
    avg_gradient_norm = row["avg_gradient"] / 12     # 12% muy duro
    max_gradient_norm = row["max_gradient"] / 25     # 25% extremo

    score = (
        0.35 * elevation_norm +
        0.30 * avg_gradient_norm +
        0.20 * distance_norm +
        0.15 * max_gradient_norm
    )

    return min(score, 1.0)


def classify_difficulty(score):
    if score < 0.3:
        return "suave"
    elif score < 0.6:
        return "intermedia"
    else:
        return "dura"