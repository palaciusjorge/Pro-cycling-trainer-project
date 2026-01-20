from src.recommender.recommend_spain import recommend_segments

if __name__ == "__main__":
    user_lat = 43.361   # Oviedo
    user_lon = -5.849
    user_level = "intermedio"

    recs = recommend_segments(
        user_lat,
        user_lon,
        user_level,
        max_distance_km=100,
    )

    print("\nRecomendaciones cercanas:\n")
    print(recs[["name", "region", "distance_to_user_km", "difficulty_level"]])


