from src.recommender.recommend_by_city import recommend_by_city


def ask_city():
    city = input("Introduce tu ciudad: ").strip()
    return city


def ask_level():
    print("\nSelecciona tu nivel:")
    print("1 - Principiante")
    print("2 - Intermedio")
    print("3 - Avanzado")

    while True:
        choice = input("Opción (1/2/3): ").strip()

        if choice == "1":
            return "principiante"
        elif choice == "2":
            return "intermedio"
        elif choice == "3":
            return "avanzado"
        else:
            print("Opción no válida. Introduce 1, 2 o 3.")


def ask_radius():
    value = input("\nRadio máximo de búsqueda en km (por defecto 120): ").strip()

    if value == "":
        return 120

    try:
        return float(value)
    except ValueError:
        print("Valor no válido. Usando 120 km por defecto.")
        return 120


def print_results(city, lat, lon, recs):
    print("\n" + "=" * 50)
    print(f"Ubicación detectada: {city} (lat={lat:.3f}, lon={lon:.3f})")
    print("=" * 50)

    if recs.empty:
        print("\nNo se encontraron segmentos cercanos con estos criterios 😕")
        return

    print("\nRecomendaciones:\n")

    for i, row in enumerate(recs.itertuples(), start=1):
        print(
            f"{i}. {row.name} ({row.region}) | "
            f"{row.distance_to_user_km:.1f} km | "
            f"dificultad: {row.difficulty_level}"
        )


def main():
    print("\n=== Pro Cycling Trainer – Spain Edition ===\n")

    city = ask_city()
    user_level = ask_level()
    radius = ask_radius()

    print("\nBuscando tramos cerca de", city, "...\n")

    try:
        lat, lon, recs = recommend_by_city(
            city_name=city,
            user_level=user_level,
            max_distance_km=radius
        )
    except Exception as e:
        print("\nError:", e)
        return

    print_results(city, lat, lon, recs)


if __name__ == "__main__":
    main()
