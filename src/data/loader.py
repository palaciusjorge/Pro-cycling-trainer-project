import pandas as pd
def load_vuelta_climbs(path: str) -> pd.DataFrame:
    """
    Load initial vuelta hardest climbs dataset.
    """
    df = pd.read_csv(path)

    required_columns = {"climb_id", "name", "profile_score"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df



if __name__ == "__main__":
    df = load_vuelta_climbs("data/raw/vuelta_hardest_climbs.csv")
    print(df.head())
