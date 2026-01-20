from src.data.loader_spain import load_spain_segments
from src.features.difficulty import compute_difficulty_score, classify_difficulty


def build_features(input_path, output_path):
    df = load_spain_segments(input_path)

    df["difficulty_score"] = df.apply(compute_difficulty_score, axis=1)
    df["difficulty_level"] = df["difficulty_score"].apply(classify_difficulty)

    df.to_csv(output_path, index=False)

    print("Spanish segments processed:")
    print(df[["name", "region", "difficulty_score", "difficulty_level"]])


if __name__ == "__main__":
    build_features(
        "data/raw/spain_legendary_segments.csv",
        "data/processed/spain_segments_features.csv"
    )
