import streamlit as st

def render_advanced_parameters():
    st.subheader("⚙️ Ajustes avanzados de Apriori")

    st.markdown("Ajusta los valores para controlar el comportamiento del algoritmo Apriori:")

    min_support = st.slider(
        "Soporte mínimo",
        min_value=0.001,
        max_value=0.1,
        value=0.01,
        step=0.001,
        help="Proporción mínima de transacciones que deben contener los productos (frecuencia relativa)."
    )

    min_confidence = st.slider(
        "Confianza mínima",
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="Probabilidad mínima de que ocurra el consecuente dado el antecedente."
    )

    min_lift = st.slider(
        "Lift mínimo",
        min_value=1.0,
        max_value=3.0,
        value=1.0,
        step=0.1,
        help="Qué tan fuerte es la asociación comparado con el azar (1 = sin relación, >1 = relación positiva)."
    )

    max_rules = st.slider(
        "Número máximo de reglas a mostrar",
        min_value=10,
        max_value=500,
        value=100,
        step=10,
        help="Limita la cantidad de reglas que se generarán."
    )

    # Guardar en session_state (para que otras partes puedan acceder)
    st.session_state["min_support"] = min_support
    st.session_state["min_confidence"] = min_confidence
    st.session_state["min_lift"] = min_lift
    st.session_state["max_rules"] = max_rules
