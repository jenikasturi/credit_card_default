import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'Credit Card Default - EDA',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

def run():
    # Membuat Title
    st.title('Credit Card Default memprediksi Default Payment Next Month')


    # Membuat sub Header
    st.subheader('EDA untuk analisis dataset credit_card_default')


    # Menambahkan Image
    st.image('https://fyh6jk7zypag.cdn.shift8web.com/wp-content/uploads/2023/04/pinjol-bunga-rendah-1-696x385.jpg', 
             caption='credit_card_default')
    

    # Menambahkan Deskripsi
    st.write('Page ini dibuat oeh Jeni :')
    st.write('# Selamat datang di halaman Credit Card Default')
    st.write('## Haiii')
    st.write('### Selamat datang')


    # Membuat garis lurus 
    st.write('---')


    # Magic syntax
    '''
    Pada page kali ini, penulis akan melakukan eksplorasi sederhana,
    Dataset yang digunakan adalah dataset credit_card_default.
    Dataset ini berasal dari [bigquery]('https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table&project=kisikisilc1&ws=!1m5!1m4!4m3!1sbigquery-public-data!2sml_datasets!3scredit_card_default')
    '''


    # Show Dataframe
    df_1 = pd.read_csv('P1G5_Set_1_jeni-kasturi.csv')
    st.dataframe(df_1)


    # Membuat barplot
    st.write('### default_payment_next_month')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='default_payment_next_month', data=df_1)
    st.pyplot(fig)

    # Mengatur palet warna seaborn
    sns.set_palette("Set2")


    # Membuat Histogram berdasarkan input user
    st.write('### Histogram berdasarkan Input User')
    pilihan = st.selectbox('Pilih Kolom : ', ('limit_balance', 'sex', 'education_level', 'age', 'marital_status', 'default_payment_next_month'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df_1[pilihan],bins=30,kde=True)
    st.pyplot(fig)


    # Membuat plotly plot
    st.write('### Plotly plot education_level dengan limit_balance')
    fig=px.scatter(df_1,x='education_level', y='limit_balance', hover_data=['sex', 'marital_status'])
    st.plotly_chart(fig)


if __name__== '__main__':
    run()