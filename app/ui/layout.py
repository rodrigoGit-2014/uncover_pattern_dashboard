import streamlit as st
from app.business.apriori_runner import generar_reglas_apriori

def render_header():
    st.title("🧠 Explorador de Reglas de Asociación")
    st.markdown(
        "Descubre patrones ocultos en tus transacciones sin necesidad de conocimientos técnicos.\n"
        "Sube un archivo, ajusta los parámetros si lo deseas y deja que la app te entregue reglas valiosas e interpretables."
    )
    st.divider()

"""
def render_analysis_tab(df):
    st.subheader("Modo de análisis")
    
    if df is None:
        st.info("Por favor, sube un archivo de transacciones en la sección principal.")
        return

    modo = st.radio("Selecciona el modo de análisis:", ["Automático (recomendado)", "Avanzado (manual)"])

    if modo == "Automático (recomendado)":
        sensibilidad = st.slider(
            "🔍 Nivel de exploración",
            min_value=1,
            max_value=3,
            value=2,
            format="%d",
            help="Controla qué tan estricta será la búsqueda de reglas: 1 = reglas muy frecuentes y fuertes, 3 = más flexibles y exploratorias."
        )
        st.success(f"Nivel seleccionado: {'Bajo' if sensibilidad == 1 else 'Medio' if sensibilidad == 2 else 'Alto'}")

    if modo == "Avanzado (manual)":
        st.warning("Puedes ajustar los parámetros en la pestaña ⚙️ Configuración Avanzada antes de generar las reglas.")

    st.button("🚀 Generar Reglas de Asociación")
"""
def render_analysis_tab(df):
    st.subheader("Modo de análisis")

    if df is None:
        st.info("Por favor, sube un archivo de transacciones en la sección principal.")
        return

    modo = st.radio("Selecciona el modo de análisis:", ["Automático (recomendado)", "Avanzado (manual)"])

    if modo == "Automático (recomendado)":
        sensibilidad = st.slider(
            "🔍 Nivel de exploración",
            min_value=1,
            max_value=3,
            value=2,
            format="%d",
            help="Controla qué tan estricta será la búsqueda de reglas: 1 = muy frecuentes, 3 = exploratorias"
        )
        st.session_state["modo"] = "auto"
        st.session_state["sensibilidad"] = sensibilidad
        st.success(f"Nivel seleccionado: {'Bajo' if sensibilidad == 1 else 'Medio' if sensibilidad == 2 else 'Alto'}")

    else:
        st.warning("Puedes ajustar los parámetros en la pestaña ⚙️ Configuración Avanzada.")
        st.session_state["modo"] = "manual"

    if st.button("🚀 Generar Reglas de Asociación"):
        with st.spinner("Generando reglas..."):

            if st.session_state["modo"] == "manual":
                # Parámetros desde configuración avanzada
                min_support = st.session_state.get("min_support", 0.01)
                min_confidence = st.session_state.get("min_confidence", 0.5)
                min_lift = st.session_state.get("min_lift", 1.0)
                max_rules = st.session_state.get("max_rules", 100)

            else:
                # Parámetros automáticos según sensibilidad
                sensibilidad = st.session_state["sensibilidad"]
                min_support = {1: 0.05, 2: 0.02, 3: 0.005}[sensibilidad]
                min_confidence = {1: 0.8, 2: 0.6, 3: 0.4}[sensibilidad]
                min_lift = 1.1
                max_rules = 100

            reglas = generar_reglas_apriori(df, min_support, min_confidence, min_lift, max_rules)

            if reglas.empty:
                st.error("No se encontraron reglas con los parámetros actuales.")
            else:
                st.success(f"✅ Se generaron {len(reglas)} reglas.")
                st.session_state["reglas"] = reglas
                st.dataframe(reglas[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

def render_visualization_tab(df):
    st.subheader("📊 Visualización de reglas")
    
    if df is None:
        st.info("Cargue un archivo de transacciones para habilitar esta sección.")
        return

    st.info("Aquí se mostrarán gráficos cuando se hayan generado reglas.")


def render_export_tab():
    st.subheader("📥 Exportar resultados")

    st.info("Cuando se generen reglas, podrás exportarlas desde aquí.")
    st.button("📄 Exportar a CSV")
    st.button("📝 Exportar a PDF con interpretaciones automáticas")
