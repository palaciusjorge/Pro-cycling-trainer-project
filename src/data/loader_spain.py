import pandas as pd


def load_spain_segments(path: str):
    """
    Load legendary Spanish cycling segments dataset.
    """
    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    df = load_spain_segments("data/raw/spain_legendary_segments.csv")
    print(df[["name", "region", "distance_km", "elevation_gain_m"]])
