import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def generar_reglas_apriori(df, min_support, min_confidence, min_lift, max_rules):
    """
    Ejecuta el algoritmo Apriori sobre un DataFrame con columnas ['id_transaccion', 'producto'].
    Retorna un DataFrame de reglas de asociación filtradas según los parámetros.

    Parameters:
        df (DataFrame): debe tener columnas ['id_transaccion', 'producto']
        min_support (float)
        min_confidence (float)
        min_lift (float)
        max_rules (int)

    Returns:
        reglas_filtradas (DataFrame)
    """
    # Paso 1: Validar columnas necesarias
    if not {'id_transaccion', 'producto'}.issubset(df.columns):
        raise ValueError("El DataFrame debe contener las columnas 'id_transaccion' y 'producto'")

    # Paso 2: Pivotear para convertir a formato one-hot por transacción
    basket = df.groupby(['id_transaccion', 'producto'])['producto'] \
               .count().unstack().fillna(0)
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    # Paso 3: Obtener itemsets frecuentes
    frequent_itemsets = apriori(
        basket,
        min_support=min_support,
        use_colnames=True
    )

    if frequent_itemsets.empty:
        return pd.DataFrame()  # No hay itemsets frecuentes

    # Paso 4: Generar reglas de asociación
    reglas = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=min_confidence
    )

    if reglas.empty:
        return pd.DataFrame()  # No hay reglas

    # Paso 5: Filtrar por lift y limitar cantidad
    reglas_filtradas = reglas[
        reglas['lift'] >= min_lift
    ].sort_values(by='confidence', ascending=False)

    return reglas_filtradas.head(max_rules)
