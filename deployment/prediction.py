import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load dump files
with open('svm_random_best.pkl', 'rb') as file_1: #rb = write binary
    svm_random_best = pickle.load(file_1)

with open('scaler.pkl', 'rb') as file_2: #rb = write binary
    scaler = pickle.load(file_2)

with open('num_col.txt', 'r') as file_3:
    num_col = json.load(file_3)
    
with open('cat_col.txt', 'r') as file_4:
    cat_col = json.load(file_4)


def run():
    # Membuat form
    with st.form(key='form parameters'):
        limit_balance = st.number_input('Limit Balance', 0, 1000000, 100, help='Amount of given credit in NT dollars (includes individual and family/supplementary credit)')
        sex = st.selectbox('Jenis Kelamin', ('1', '2'), help='1=laki-laki, 2=perempuan')
        education_level = st.selectbox('Tingkat Pendidikan', ('1', '2', '3', '4', '5', '6'), 
                                       help='1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown')
        marital_status = st.selectbox('Status Pernikahan', ('1', '2', '3'), help='1=menikah, 2=lajang, 3=lainnya')
        age = st.number_input('Usia', min_value=20, max_value=50, value=25, step=1, help='Usia')
        st.markdown('---')
        pay_0 = st.selectbox('Status Pelunasan bulan September 2005', ('-1', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 
                             help='-1=bayar lunas, 1=keterlambatan pembayaran selama 1 bulan, 2=keterlambatan pembayaran selama 2 bulan, 3=keterlambatan pembayaran selama 3 bulan, 4=keterlambatan pembayaran selama 4 bulan, 5=keterlambatan pembayaran selama 5 bulan, 6=keterlambatan pembayaran selama 6 bulan, 7=keterlambatan pembayaran selama 7 bulan, 8=keterlambatan pembayaran selama 8 bulan, 9=keterlambatan pembayaran selama 9 bulan')
        pay_2 = st.selectbox('Status Pelunasan bulan Agustus 2005', ('-1', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 
                             help='-1=bayar lunas, 1=keterlambatan pembayaran selama 1 bulan, 2=keterlambatan pembayaran selama 2 bulan, 3=keterlambatan pembayaran selama 3 bulan, 4=keterlambatan pembayaran selama 4 bulan, 5=keterlambatan pembayaran selama 5 bulan, 6=keterlambatan pembayaran selama 6 bulan, 7=keterlambatan pembayaran selama 7 bulan, 8=keterlambatan pembayaran selama 8 bulan, 9=keterlambatan pembayaran selama 9 bulan')
        pay_3 = st.selectbox('Status Pelunasan bulan Juli 2005', ('-1', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 
                             help='-1=bayar lunas, 1=keterlambatan pembayaran selama 1 bulan, 2=keterlambatan pembayaran selama 2 bulan, 3=keterlambatan pembayaran selama 3 bulan, 4=keterlambatan pembayaran selama 4 bulan, 5=keterlambatan pembayaran selama 5 bulan, 6=keterlambatan pembayaran selama 6 bulan, 7=keterlambatan pembayaran selama 7 bulan, 8=keterlambatan pembayaran selama 8 bulan, 9=keterlambatan pembayaran selama 9 bulan')
        pay_4 = st.selectbox('Status Pelunasan bulan Juni 2005', ('-1', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 
                             help='-1=bayar lunas, 1=keterlambatan pembayaran selama 1 bulan, 2=keterlambatan pembayaran selama 2 bulan, 3=keterlambatan pembayaran selama 3 bulan, 4=keterlambatan pembayaran selama 4 bulan, 5=keterlambatan pembayaran selama 5 bulan, 6=keterlambatan pembayaran selama 6 bulan, 7=keterlambatan pembayaran selama 7 bulan, 8=keterlambatan pembayaran selama 8 bulan, 9=keterlambatan pembayaran selama 9 bulan')
        pay_5 = st.selectbox('Status Pelunasan bulan Mei 2005', ('-1', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 
                             help='-1=bayar lunas, 1=keterlambatan pembayaran selama 1 bulan, 2=keterlambatan pembayaran selama 2 bulan, 3=keterlambatan pembayaran selama 3 bulan, 4=keterlambatan pembayaran selama 4 bulan, 5=keterlambatan pembayaran selama 5 bulan, 6=keterlambatan pembayaran selama 6 bulan, 7=keterlambatan pembayaran selama 7 bulan, 8=keterlambatan pembayaran selama 8 bulan, 9=keterlambatan pembayaran selama 9 bulan')
        pay_6 = st.selectbox('Status Pelunasan bulan April 2005', ('-1', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 
                             help='-1=bayar lunas, 1=keterlambatan pembayaran selama 1 bulan, 2=keterlambatan pembayaran selama 2 bulan, 3=keterlambatan pembayaran selama 3 bulan, 4=keterlambatan pembayaran selama 4 bulan, 5=keterlambatan pembayaran selama 5 bulan, 6=keterlambatan pembayaran selama 6 bulan, 7=keterlambatan pembayaran selama 7 bulan, 8=keterlambatan pembayaran selama 8 bulan, 9=keterlambatan pembayaran selama 9 bulan')
        st.markdown('---')
        bill_amt_1 = st.number_input('Jumlah Tagihan bulan September 2005 (dolar NT)', 0, 1000000, 10)
        bill_amt_2 = st.number_input('Jumlah Tagihan bulan Agustus 2005 (dolar NT)', 0, 1000000, 10)
        bill_amt_3 = st.number_input('Jumlah Tagihan bulan Juli 2005 (dolar NT)', 0, 1000000, 10)
        bill_amt_4 = st.number_input('Jumlah Tagihan bulan Juni 2005 (dolar NT)', 0, 1000000, 10)
        bill_amt_5 = st.number_input('Jumlah Tagihan bulan Mei 2005 (dolar NT)', 0, 1000000, 10)
        bill_amt_6 = st.number_input('Jumlah Tagihan bulan April 2005 (dolar NT)', 0, 1000000, 10)
        st.markdown('---')
        pay_amt_1 = st.number_input('Jumlah pembayaran sebelumnya pada bulan September 2005 (dolar NT)', 0, 1000000, 10)
        pay_amt_2 = st.number_input('Jumlah pembayaran sebelumnya pada bulan Agustus 2005 (dolar NT)', 0, 1000000, 10)
        pay_amt_3 = st.number_input('Jumlah pembayaran sebelumnya pada bulan Juli 2005 (dolar NT)', 0, 1000000, 10)
        pay_amt_4 = st.number_input('Jumlah pembayaran sebelumnya pada bulan Juni 2005 (dolar NT)', 0, 1000000, 10)
        pay_amt_5 = st.number_input('Jumlah pembayaran sebelumnya pada bulan Mei 2005 (dolar NT)', 0, 1000000, 10)
        pay_amt_6 = st.number_input('Jumlah pembayaran sebelumnya pada bulan April 2005 (dolar NT)', 0, 1000000, 10)

        submitted = st.form_submit_button('Predict')
    
    data_inf = {
        'limit_balance' : limit_balance,
        'sex' : sex, 
        'education_level' : education_level,
        'marital_status' : marital_status,
        'age' : age, 
        'pay_0' : pay_0, 
        'pay_2' : pay_2, 
        'pay_3' : pay_3, 
        'pay_4' : pay_4,
        'pay_5' : pay_5, 
        'pay_6' : pay_6, 
        'bill_amt_1': bill_amt_1, 
        'bill_amt_2' : bill_amt_2,
        'bill_amt_3' : bill_amt_3, 
        'bill_amt_4' : bill_amt_4, 
        'bill_amt_5' : bill_amt_5,
        'bill_amt_6' : bill_amt_6,
        'pay_amt_1' : pay_amt_1,
        'pay_amt_2' : pay_amt_2,
        'pay_amt_3' : pay_amt_3,
        'pay_amt_4' : pay_amt_4,
        'pay_amt_5' : pay_amt_5,
        'pay_amt_6' : pay_amt_6}
    
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Split between num col and cat col
        data_inf_num = data_inf[num_col]
        data_inf_cat = data_inf[cat_col]

        # feature scaling and encoding
        data_inf_num_scaled = scaler.transform(data_inf_num)

        # Concat data inference scaled dan encoded
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat], axis=1)

        # Predict new data inference using knn model
        y_pred_inf = svm_random_best.predict(data_inf_final)

        # Display Result
        if y_pred_inf == 0:
            st.write(f'### Hasil prediksi default_payment_next_month adalah {round(y_pred_inf[0])} yang artinya akan bayar')
        else:
            st.write(f'### Hasil prediksi default_payment_next_month adalah {round(y_pred_inf[0])} yang artinya tidak bayar')

if __name__== '__main__':
    run()