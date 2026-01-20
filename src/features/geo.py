import numpy as np


def haversine(lat1, lon1, lat2, lon2):
    """
    Distance between two points on Earth (km).
    """
    R = 6371  # Earth radius km

    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c


def compute_distance_to_user(df, user_lat, user_lon):
    """
    Compute distance from user to start of each segment.
    """
    df = df.copy()

    df["distance_to_user_km"] = df.apply(
        lambda row: haversine(
            user_lat,
            user_lon,
            row["start_lat"],
            row["start_lon"]
        ),
        axis=1
    )

    return df
