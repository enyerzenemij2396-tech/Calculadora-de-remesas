import streamlit as st

st.title("Calculadora de Remesas 🇨🇴 ➡️ 🇻🇪")
tasa = 7.21
pesos = st.number_input("Pesos Colombianos (COP):", min_value=0.0, value=1000.0)
bolivares = pesos / tasa
st.header(f"Recibes: {bolivares:,.2f} VES")
st.write(f"Tasa aplicada: {tasa}")
