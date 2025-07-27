import pandas as pd
from ast import literal_eval
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Leer el archivo CSV
df = pd.read_csv("./data/dummy_items.csv")

# Asegurar que la columna 'items' sea una lista real (no string)
df["items"] = df["items"].apply(literal_eval)

# Convertir la lista de transacciones en formato one-hot encoding
te = TransactionEncoder()
te_ary = te.fit(df["items"]).transform(df["items"])
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Ejecutar Apriori
frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)

# Generar reglas de asociación
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Mostrar reglas relevantes
rules = rules[["antecedents", "consequents", "support", "confidence", "lift"]]

# Formatear reglas como texto legible
rules["rule"] = rules.apply(lambda row: f"IF {set(row['antecedents'])} THEN {set(row['consequents'])}", axis=1)

# Mostrar resultados
print(rules[["rule", "support", "confidence", "lift"]])
