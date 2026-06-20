
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ====================================
# KONFIGURASI
# ====================================

st.set_page_config(
    page_title="Dashboard TikTok Shop",
    layout="wide"
)

st.title("📊 Dashboard Analisis TikTok Shop")
st.subheader(
    "Pengaruh Gamifikasi Misi terhadap Retensi Pengguna TikTok Shop"
)

# ====================================
# DATA
# ====================================

df = pd.read_csv("data_tiktok_shop_bersih.csv")

# ====================================
# FILTER
# ====================================

st.sidebar.header("Filter")

gender = st.sidebar.selectbox(
    "Jenis Kelamin",
    ["Semua"] + list(df["Jenis Kelamin"].unique())
)

usia = st.sidebar.selectbox(
    "Usia",
    ["Semua"] + list(df["Usia"].unique())
)

df_filter = df.copy()

if gender != "Semua":
    df_filter = df_filter[
        df_filter["Jenis Kelamin"] == gender
    ]

if usia != "Semua":
    df_filter = df_filter[
        df_filter["Usia"] == usia
    ]

# ====================================
# METRIK
# ====================================

st.header("Ringkasan")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Jumlah Responden",
        len(df_filter)
    )

with col2:
    st.metric(
        "Kategori Gender",
        df_filter["Jenis Kelamin"].nunique()
    )

with col3:
    st.metric(
        "Kelompok Usia",
        df_filter["Usia"].nunique()
    )

# ====================================
# PIE CHART
# ====================================

st.header("Profil Responden")

col1, col2 = st.columns(2)

with col1:

    fig1, ax1 = plt.subplots()

    jk = df_filter["Jenis Kelamin"].value_counts()

    ax1.pie(
        jk,
        labels=jk.index,
        autopct="%1.1f%%"
    )

    ax1.set_title("Jenis Kelamin")

    st.pyplot(fig1)

with col2:

    fig2, ax2 = plt.subplots()

    usia_data = df_filter["Usia"].value_counts()

    ax2.pie(
        usia_data,
        labels=usia_data.index,
        autopct="%1.1f%%"
    )

    ax2.set_title("Usia")

    st.pyplot(fig2)

# ====================================
# RATA-RATA PERTANYAAN
# ====================================

st.header("Rata-rata Pertanyaan")

numeric_cols = df_filter.select_dtypes(
    include="number"
).columns

rata = (
    df_filter[numeric_cols]
    .mean()
    .sort_values()
)

fig3, ax3 = plt.subplots(
    figsize=(8,6)
)

ax3.barh(
    rata.index,
    rata.values
)

ax3.set_xlabel("Skor")

st.pyplot(fig3)

# ====================================
# PREVIEW DATA
# ====================================

st.header("Preview Data")

st.write(
    df_filter.head()
)
