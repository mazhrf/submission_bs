import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    day_df = pd.read_csv("data/day.csv")
    hour_df = pd.read_csv("data/hour.csv")
    
    # Konversi kolom tanggal
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    return day_df, hour_df

day_df, hour_df = load_data()

img_path = "assets/dicoding.png"
st.sidebar.image(img_path, width=150)
st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.title("Profile:")
st.sidebar.markdown("**• Nama: Muhammad Azhar Fikri**")
st.sidebar.markdown("**• Email: muhammadazharfikri990@gmail.com**")

st.sidebar.header("Filter Data")
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

start_date, end_date = st.sidebar.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

weather_map = {1: 'Clear', 2: 'Mist', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca", options=list(weather_map.values()))

filtered_day_df = day_df[
    (day_df['dteday'] >= pd.Timestamp(start_date)) & 
    (day_df['dteday'] <= pd.Timestamp(end_date)) &
    (day_df['weathersit'].map(weather_map) == selected_weather)
]

filtered_hour_df = hour_df[
    (hour_df['dteday'] >= pd.Timestamp(start_date)) & 
    (hour_df['dteday'] <= pd.Timestamp(end_date))
]


st.title("Dashboard Analisis Penyewaan Sepeda")
st.sidebar.header("Pilih Visualisasi")
visualization_option = st.sidebar.radio(
    "Pilih jenis visualisasi:", 
    ['Penyewaan per Jam', 'Rata-Rata Penyewaan Sepeda per Hari', 'Distribusi Penyewaan Berdasarkan Cuaca']
)

if visualization_option == 'Penyewaan per Jam':
    rentals_per_hour = hour_df.groupby('hr', as_index=False)['cnt'].sum()
    rentals_per_hour["color_scale"] = rentals_per_hour["hr"].apply(lambda x: 1 if x == 17 else 0.5)

    fig_hourly = px.bar(rentals_per_hour, x='hr', y='cnt', 
                        title='Jumlah Penyewaan Sepeda per Jam', 
                        labels={'hr': 'Jam', 'cnt': 'Jumlah Penyewaan'},
                        color='color_scale',
                        color_continuous_scale=["lightblue", "blue"],
                        range_y=[0, rentals_per_hour['cnt'].max() * 1.1]) 

    fig_hourly.update_layout(yaxis=dict(tickformat=".0f"))
    fig_hourly.update_coloraxes(showscale=False)

    st.plotly_chart(fig_hourly)

elif visualization_option == 'Rata-Rata Penyewaan Sepeda per Hari':
    avg_rentals_per_day = filtered_hour_df.groupby(filtered_hour_df['dteday'].dt.date)['cnt'].mean()
    avg_rentals_df = avg_rentals_per_day.reset_index()
    avg_rentals_df.columns = ['Tanggal', 'Rata-Rata Penyewaan']

    avg_rentals_df = avg_rentals_df.sort_values(by='Tanggal')

    fig = px.line(
        avg_rentals_df, x='Tanggal', y='Rata-Rata Penyewaan', 
        title=f'Rata-Rata Penyewaan Sepeda per Hari ({start_date} - {end_date})', 
        labels={'Tanggal': 'Tanggal', 'Rata-Rata Penyewaan': 'Jumlah Rata-Rata Penyewaan'}
    )

    st.plotly_chart(fig)


elif visualization_option == 'Distribusi Penyewaan Berdasarkan Cuaca':
    fig_box = px.box(day_df, x='weathersit', y='cnt', title='Distribusi Penyewaan Berdasarkan Cuaca', 
                    labels={'weathersit': 'Kondisi Cuaca', 'cnt': 'Jumlah Penyewaan'})

    st.plotly_chart(fig_box)

if st.sidebar.checkbox("Tampilkan Data Mentah"):
    st.subheader("Data Harian")
    st.write(day_df.head())
    st.subheader("Data Jam")
    st.write(hour_df.head())

st.caption('Copyright © submission_dataset 2025')