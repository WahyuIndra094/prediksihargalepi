import streamlit as st
import pickle
from PIL import Image
import pandas as pd
import plotly.express as px

filename = 'modelPrediksi.sav'
loaded_model = pickle.load(open(filename, 'rb'))

image = Image.open('Picture.png')

df = pd.read_csv('laptop_data.csv')

with st.container():
    
    st.title('Prediksi Harga Laptop\n')
    coll1, coll2 = st.columns([3,100])

    with coll1:
            st.write("")

    with coll2:
            st.image(image , width= 550)
            
st.dataframe(df)

produk_count = df['Company'].value_counts().reset_index()
produk_count.columns = ['Company', 'Jumlah']
fig = px.bar(produk_count, x='Company', y='Jumlah', title='Jumlah Produk yang Banyak di Pasaran')
fig.update_xaxes(title='Company')
fig.update_yaxes(title='Jumlah')
st.plotly_chart(fig)

avg_price = df.groupby('Company')['Price'].mean().reset_index()
fig_avg_price = px.bar(avg_price, x='Company', y='Price', title='Rata-rata Harga Produk per Company')
fig_avg_price.update_xaxes(title='Company')
fig_avg_price.update_yaxes(title='Rata-rata Harga')
st.plotly_chart(fig_avg_price)
st.sidebar.subheader('Variasi Fitur')
st.sidebar.markdown('Pilih nilai untuk setiap fitur dan tekan tombol "Prediksi" untuk melihat hasil.')

ram = st.sidebar.slider('RAM (GB)', 2, 32)
inches = st.sidebar.slider('Ukuran Layar (Inchi)', 10, 20)
weight = st.sidebar.slider('Berat (kg)', 1.0, 5.0)
ghz = st.sidebar.slider('GHz', 1.0, 5.0)

if st.sidebar.button('Prediksi'):
    prediction = round(loaded_model.predict([[ram, inches, weight, ghz]])[0], 2)
    
    st.sidebar.success(f'Prediksi harga laptop adalah: Rp.{prediction}')

st.subheader('Aplikasi ini membantu Anda memprediksi harga laptop berdasarkan beberapa fitur tertentu.')
st.subheader('Gunakan slider di sidebar untuk mengatur nilai fitur dan tekan tombol "Prediksi".')
st.subheader('Pastikan untuk memilih nilai yang sesuai sebelum melakukan prediksi.')

st.markdown('Dibuat dengan ❤ menggunakan Streamlit oleh kelompok 7')
