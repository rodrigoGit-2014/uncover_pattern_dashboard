import sys
import os
# Agrega la carpeta raíz del proyecto al sys.path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

import streamlit as st
from app.ui import layout, file_upload, parameter_controls


# Configuración de la página
st.set_page_config(
    page_title="Explorador de Reglas de Asociación",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
layout.render_header()

# Carga del archivo
df = file_upload.upload_file()

# Tabs principales
tabs = st.tabs(["🔍 Análisis", "📊 Visualización", "⚙️ Configuración Avanzada", "📥 Exportar"])

# ----- TAB 1: Análisis -----
with tabs[0]:
    layout.render_analysis_tab(df)

# ----- TAB 2: Visualización -----
with tabs[1]:
    layout.render_visualization_tab(df)

# ----- TAB 3: Configuración Avanzada -----
with tabs[2]:
    parameter_controls.render_advanced_parameters()

# ----- TAB 4: Exportar -----
with tabs[3]:
    layout.render_export_tab()
