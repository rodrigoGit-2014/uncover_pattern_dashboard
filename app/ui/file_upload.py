import streamlit as st
import pandas as pd

def upload_file():
    st.header("📁 Subir archivo de transacciones")

    uploaded_file = st.file_uploader(
        "Carga un archivo CSV con columnas como 'id_transaccion' y 'producto'",
        type=["csv"]
    )

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            # Validar columnas mínimas
            required_cols = {'id_transaccion', 'producto'}
            if not required_cols.issubset(df.columns):
                st.error(f"El archivo debe contener las columnas: {required_cols}")
                return None

            st.success("✅ Archivo cargado correctamente")
            st.markdown("### 🔍 Vista previa del archivo:")
            st.dataframe(df.head())

            return df

        except Exception as e:
            st.error(f"❌ Error al leer el archivo: {e}")
            return None
    else:
        return None
