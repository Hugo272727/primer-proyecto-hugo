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
