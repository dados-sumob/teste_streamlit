import streamlit as st
import folium
from streamlit_folium import st_folium

# Título do App
st.title("Mapa de Belo Horizonte")
st.write("Este é um mapa interativo de Belo Horizonte.")

# Criar o mapa centralizado em Belo Horizonte
latitude_bh, longitude_bh = -19.9167, -43.9345
map_bh = folium.Map(location=[latitude_bh, longitude_bh], zoom_start=12, tiles="OpenStreetMap")

# Adicionar marcadores (exemplo)
folium.Marker(
    location=[-19.9208, -43.9378],
    popup="Praça da Liberdade",
    tooltip="Praça da Liberdade",
    icon=folium.Icon(color="blue", icon="info-sign"),
).add_to(map_bh)

folium.Marker(
    location=[-19.9173, -43.9346],
    popup="Mercado Central",
    tooltip="Mercado Central",
    icon=folium.Icon(color="green", icon="shopping-cart"),
).add_to(map_bh)

# Exibir o mapa no Streamlit
st_folium(map_bh, width=700, height=500)