import pandas as pd
def load_legendary_segments(path: str):
    """
    Load initial legendary cycling segments dataset.
    """
    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    df = load_legendary_segments("data/raw/legendary_segments.csv")
    print(df.head())
