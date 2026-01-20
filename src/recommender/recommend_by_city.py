from src.data.geocoding import geocode_city
from src.recommender.recommend_spain import recommend_segments


def recommend_by_city(city_name, user_level, max_distance_km=120, max_results=5):
    # Obtener coordenadas de la ciudad
    lat, lon = geocode_city(city_name)

    if lat is None:
        raise ValueError(f"No se pudo encontrar la ciudad: {city_name}")

    # Llamar al recomendador geográfico
    recs = recommend_segments(
        user_lat=lat,
        user_lon=lon,
        user_level=user_level,
        max_distance_km=max_distance_km,
        max_results=max_results
    )

    return lat, lon, recs
