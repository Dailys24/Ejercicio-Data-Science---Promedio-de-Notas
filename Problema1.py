import pandas as pd
from datos import datos

def calcular_analisis_notas():
    """
    Realiza un análisis completo de las notas y devuelve los resultados.
    """
    # Crear un DataFrame
    df_alumnos = pd.DataFrame(datos)

    # Calcular el promedio de cada alumno
    df_alumnos['promedio'] = df_alumnos['notas'].apply(lambda x: sum(x) / len(x))

    # Calcular el promedio general del curso
    promedio_general = df_alumnos['promedio'].mean()

    # Encontrar la nota más alta y la más baja
    todas_las_notas = df_alumnos['notas'].explode().astype(float)
    nota_mas_alta = todas_las_notas.max()
    nota_mas_baja = todas_las_notas.min()

    # Encontrar a los alumnos con el promedio más alto y más bajo
    alumno_nota_max = df_alumnos.loc[df_alumnos['promedio'].idxmax()]
    alumno_nota_min = df_alumnos.loc[df_alumnos['promedio'].idxmin()]

    # Devolver los resultados en un diccionario
    return {
        "promedio_general": promedio_general,
        "nota_mas_alta": nota_mas_alta,
        "nota_mas_baja": nota_mas_baja,
        "alumno_promedio_max": alumno_nota_max,
        "alumno_promedio_min": alumno_nota_min,
        "df_completo": df_alumnos
    }
