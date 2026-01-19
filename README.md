# Pro Cycling Trainer – Train Like a Pro with Data

## Descripción

**Pro Cycling Trainer** es una aplicación de *data analytics* que recomienda tramos reales de etapas profesionales de ciclismo (Tour de Francia, Giro d’Italia, Vuelta a España, clásicas, etc.) adaptados al nivel y objetivos de entrenamiento del usuario.

El objetivo es permitir que cualquier ciclista pueda entrenar en rutas míticas del ciclismo profesional, ajustadas a su condición física, tiempo disponible y tipo de entrenamiento, y así “sentirse como un profesional”.

El proyecto combina análisis de datos, APIs geográficas, sistemas de recomendación y visualización interactiva sobre mapas.

---

## Funcionalidades principales

- 🔍 **Recomendación de tramos de etapas profesionales** según:
  - Nivel del ciclista (principiante / intermedio / avanzado)
  - Tiempo disponible
  - Objetivo de entrenamiento (resistencia, escalada, ritmo)

- Generación de rutas reales usando APIs de enrutamiento.

- Cálculo automático de:
  - Distancia  
  - Desnivel acumulado  
  - Pendientes medias y máximas  
  - Índice de dificultad  

- Clasificación de rutas:
  - Suave  
  - Intermedia  
  - Dura  

- Visualización interactiva:
  - Mapas con recorridos  
  - Perfiles de altitud  
  - Información histórica de la etapa original  

- *(Opcional)* Comparación con tiempos reales de corredores profesionales.

---

## Arquitectura del proyecto

El proyecto sigue una estructura modular y escalable:

```text
pro_cycling_trainer/
├── data/            # Datos brutos, procesados y externos
├── notebooks/       # Exploración y prototipos
├── src/
│   ├── data/        # Descarga de datos y llamadas a APIs
│   ├── features/    # Ingeniería de características y dificultad
│   ├── recommender/# Lógica de recomendación
│   ├── visualization/ # Mapas y gráficos
│   └── app/         # Aplicación final (Streamlit)
├── tests/           # Tests unitarios
├── README.md
└── requirements.txt
```

## Fuentes de datos y APIs

- **OpenRouteService / GraphHopper** – generación de rutas y geometría  
- **OpenTopography / Elevation APIs** – perfiles de altitud y desnivel  
- **ProCyclingStats (scraping controlado)** – información histórica de etapas profesionales  
- **OpenStreetMap** – red viaria y datos geográficos  

---

## Tecnologías utilizadas

- **Python**  
- pandas, numpy  
- requests, BeautifulSoup  
- scikit-learn  
- Folium / Plotly (mapas y visualización)  
- Streamlit (aplicación interactiva)  
- Jupyter Notebooks  
- Visual Studio Code  

---

## Objetivo del proyecto

Este proyecto está diseñado como:

- Proyecto de **portfolio profesional en Data Analytics / Data Science**
- Demostración de:
  - Uso de APIs reales  
  - Procesamiento de datos geoespaciales  
  - Ingeniería de características  
  - Sistemas de recomendación  
  - Visualización avanzada  

---

## Autor

Proyecto desarrollado por **Jorge Palacios Colomina**

- Contacto: palaciusjorge@gmail.com  
- GitHub: [github.com/palaciusjorge](https://github.com/palaciusjorge)  
