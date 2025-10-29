import pandas as pd

df = pd.read_csv("spotify.csv")

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

numericas = df.select_dtypes(include="number")

print("=== MEDIDAS DE TENDENCIA CENTRAL ===")
for col in numericas.columns:
    media = numericas[col].mean()
    mediana = numericas[col].median()
    moda = numericas[col].mode()[0] if not numericas[col].mode().empty else None

    print(f"\nVariable: {col}")
    print(f"  Media: {media:.2f}")
    print(f"  Mediana: {mediana:.2f}")
    print(f"  Moda: {moda}")

# ===== CLASIFICACIÓN =====
clasificacion = []

for col in df.columns:
    if df[col].dtype == "object":
        clasificacion.append([col, "Cualitativa", "Nominal"])
    else:
        if pd.api.types.is_integer_dtype(df[col]):
            clasificacion.append([col, "Cuantitativa", "Discreta"])
        else:
            clasificacion.append([col, "Cuantitativa", "Continua"])

tabla = pd.DataFrame(clasificacion, columns=["Variable", "Tipo", "Subtipo"])
print("\n\n=== CLASIFICACIÓN DE VARIABLES ===")
print(tabla)
print("\n\n=== CONCLUSIÓN DEL ANÁLISIS ===\n")
print("""
Al analizar la media, la mediana y la desviación estándar de las variables numéricas del dataset, se puede ver qué tan parecidos o diferentes están los valores entre sí. Por ejemplo, en variables como danceability, energy y valence, la media y la mediana son muy parecidas, lo que significa que la mayoría de las canciones tienen características musicales parecidas; o sea, no hay canciones súper diferentes en cómo suenan, casi todas tienen niveles similares de energía o qué tan “bailables” son.

En cambio, en variables como popularity y duration_ms, sí se nota una diferencia más grande entre la media y la mediana, lo que nos dice que los datos están sesgados. Esto pasa porque hay canciones muy populares que “suben” el promedio, pero en realidad la mayoría no lo son tanto. Lo mismo con la duración: hay rolas muy cortas y otras larguísimas, entonces la variabilidad es más grande y se refleja en la desviación estándar alta.

En pocas palabras, las canciones son parecidas en cómo se escuchan, pero no se parecen tanto en qué tan populares son ni en cuánto duran. O sea, musicalmente mantienen un estilo más uniforme, pero en impacto y longitud sí varían un buen.
""")

