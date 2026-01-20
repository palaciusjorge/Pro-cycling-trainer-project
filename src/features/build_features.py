import pandas as pd
from src.data.loader import load_legendary_segments
from src.features.difficulty import compute_difficulty_score, classify_difficulty


def build_features(input_path, output_path):
    df = load_legendary_segments(input_path)

    df["difficulty_score"] = df.apply(compute_difficulty_score, axis=1)
    df["difficulty_level"] = df["difficulty_score"].apply(classify_difficulty)

    df.to_csv(output_path, index=False)
    print("Features built successfully:")
    print(df[["name", "difficulty_score", "difficulty_level"]])


if __name__ == "__main__":
    build_features(
        "data/raw/legendary_segments.csv",
        "data/processed/legendary_segments_features.csv"
    )
