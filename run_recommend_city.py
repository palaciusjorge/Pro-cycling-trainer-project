from src.recommender.recommend_by_city import recommend_by_city

if __name__ == "__main__":
    city = "Oviedo"
    user_level = "intermedio"

    lat, lon, recs = recommend_by_city(
        city_name=city,
        user_level=user_level,
        max_distance_km=120
    )

    print(f"\nUbicación detectada: {city} -> lat={lat:.3f}, lon={lon:.3f}\n")

    print("Recomendaciones cercanas:\n")
    print(recs[["name", "region", "distance_to_user_km", "difficulty_level"]])