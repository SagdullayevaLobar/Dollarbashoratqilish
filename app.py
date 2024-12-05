import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Modelni yuklash
model = joblib.load("Dollarmodel.pkl")

# Ilova sarlavhasi
st.title("Dollar Kursi Bashorati")

# Foydalanuvchi kiritish interfeysi
st.sidebar.header("Kiritish ma'lumotlari")
def user_input():
    Inflation_Rate = st.sidebar.slider("Inflyatsiya darajasi (%)", 0.0, 20.0, 5.0)
    Interest_Rate = st.sidebar.slider("Foiz stavkasi (%)", 0.0, 20.0, 5.0)
    Trade_Balance = st.sidebar.slider("Savdo balansi (mlrd $)", -10.0, 10.0, 0.0)
    Foreign_Reserves = st.sidebar.slider("Xorijiy zaxiralar (mlrd $)", 0.0, 100.0, 50.0)
    Crude_Oil_Price = st.sidebar.slider("Neft narxi ($/barrel)", 20.0, 150.0, 75.0)
    Gold_Price = st.sidebar.slider("Oltin narxi ($/unsiya)", 1000.0, 2000.0, 1500.0)
    Stock_Index = st.sidebar.slider("Fond birjasi indeksi", 1000.0, 5000.0, 2500.0)
    Export_Volume = st.sidebar.slider("Eksport hajmi (mlrd $)", 0.0, 100.0, 50.0)
    Import_Volume = st.sidebar.slider("Import hajmi (mlrd $)", 0.0, 100.0, 50.0)
    Unemployment_Rate = st.sidebar.slider("Ishsizlik darajasi (%)", 0.0, 25.0, 10.0)
    GDP_Growth_Rate = st.sidebar.slider("YaIM o'sish sur'ati (%)", -10.0, 10.0, 2.0)
    Political_Stability_Index = st.sidebar.slider("Siyosiy barqarorlik indeksi (1-10)", 1, 10, 5)
    Currency_Circulation = st.sidebar.slider("Naqd valyuta (mlrd)", 0.0, 50000.0, 25000.0)
    Remittance_Inflow = st.sidebar.slider("Pul o'tkazmalari (mlrd $)", 0.0, 50.0, 25.0)
    Global_USD_Index = st.sidebar.slider("Jahon dollar indeksi", 80.0, 120.0, 100.0)
    Fed_Interest_Rate = st.sidebar.slider("AQSh Federal Rezerv foiz stavkasi (%)", 0.0, 5.0, 2.5)
    Geopolitical_Event = st.sidebar.selectbox("Geosiyosiy hodisa", [0, 1])

    data = {
        "Inflation_Rate": Inflation_Rate,
        "Interest_Rate": Interest_Rate,
        "Trade_Balance": Trade_Balance,
        "Foreign_Reserves": Foreign_Reserves,
        "Crude_Oil_Price": Crude_Oil_Price,
        "Gold_Price": Gold_Price,
        "Stock_Index": Stock_Index,
        "Export_Volume": Export_Volume,
        "Import_Volume": Import_Volume,
        "Unemployment_Rate": Unemployment_Rate,
        "GDP_Growth_Rate": GDP_Growth_Rate,
        "Political_Stability_Index": Political_Stability_Index,
        "Currency_Circulation": Currency_Circulation,
        "Remittance_Inflow": Remittance_Inflow,
        "Global_USD_Index": Global_USD_Index,
        "Fed_Interest_Rate": Fed_Interest_Rate,
        "Geopolitical_Event": Geopolitical_Event,
    }
    return pd.DataFrame(data, index=[0])

# Kiritilgan ma'lumotlar
input_data = user_input()

# Bashorat
st.subheader("Kiritilgan ma'lumotlar")
st.write(input_data)

prediction = model.predict(input_data)
st.subheader("Bashorat qilingan Dollar Kursi")
st.write(f"{prediction[0]:,.2f} UZS")


