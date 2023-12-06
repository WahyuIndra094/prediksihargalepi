import streamlit as st
import pickle
from PIL import Image

# Load the pre-trained model
filename = 'modelPrediksi.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Image
image = Image.open('Picture.png')

# Credits
with st.container():
   
    st.title('Prediksi Harga Laptop\n')
    coll1, coll2 = st.columns([3,100])

    with coll1:
            st.write("")

    with coll2:
            st.image(image , width= 550)

# Sidebar with Information
st.sidebar.subheader('Variasi Fitur')
st.sidebar.markdown('Pilih nilai untuk setiap fitur dan tekan tombol "Prediksi" untuk melihat hasil.')

# Add sliders for features
ram = st.sidebar.slider('RAM (GB)', 2, 32, 8)
inches = st.sidebar.slider('Ukuran Layar (Inchi)', 10, 20, 15)
weight = st.sidebar.slider('Berat (kg)', 1.0, 5.0, 2.0)
ghz = st.sidebar.slider('GHz', 1.0, 5.0, 2.0)

# Button to trigger prediction
if st.sidebar.button('Prediksi'):
    # Make prediction using the loaded model
    prediction = round(loaded_model.predict([[ram, inches, weight, ghz]])[0], 2)
    
    # Display the prediction result
    st.sidebar.success(f'Prediksi harga laptop adalah: Rp.{prediction}')

# Information and Tips Section
st.subheader('Aplikasi ini membantu Anda memprediksi harga laptop berdasarkan beberapa fitur tertentu.')
st.subheader('Gunakan slider di sidebar untuk mengatur nilai fitur dan tekan tombol "Prediksi".')
st.subheader('Pastikan untuk memilih nilai yang sesuai sebelum melakukan prediksi.')

# Footer
st.markdown('Dibuat dengan ❤️ menggunakan Streamlit oleh kelompok 7')

