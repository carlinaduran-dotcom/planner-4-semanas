import streamlit as st
import pandas as pd

st.set_page_config(page_title="Planner 4 Semanas PRO", layout="wide")

st.title("🔥 Planner 4 Semanas – Máximo Rendimiento")

if "data" not in st.session_state:
    days = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    weeks = ["Semana 1","Semana 2","Semana 3","Semana 4"]
    rows = []

    for week in weeks:
        for day in days:
            rows.append({
                "Semana": week,
                "Día": day,
                "Cumplido": 0,
                "Energía (1-5)": 3,
                "Hambre (1-5)": 3,
                "Retención (1-5)": 3,
                "Peso Semana": None
            })

    st.session_state.data = pd.DataFrame(rows)

df = st.session_state.data

st.subheader("📊 Seguimiento Diario")

edited_df = st.data_editor(
    df,
    use_container_width=True
)

st.session_state.data = edited_df

st.subheader("📈 Dashboard")

col1, col2, col3, col4 = st.columns(4)

adherencia = edited_df["Cumplido"].mean() * 100
energia = edited_df["Energía (1-5)"].mean()
hambre = edited_df["Hambre (1-5)"].mean()
retencion = edited_df["Retención (1-5)"].mean()

col1.metric("Adherencia %", f"{adherencia:.1f}%")
col2.metric("Energía Promedio", f"{energia:.1f}")
col3.metric("Hambre Promedio", f"{hambre:.1f}")
col4.metric("Retención Promedio", f"{retencion:.1f}")

st.subheader("⚖ Evolución del Peso")

peso_df = edited_df.groupby("Semana")["Peso Semana"].mean().reset_index()

st.line_chart(peso_df.set_index("Semana"))

st.markdown("---")
st.caption("Planner diseñado para pérdida de volumen y mejora metabólica.")
