
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
        autopct="%1.1f%%",
        colors=["#C084FC", "#F9A8D4"]
    )

    ax1.set_title("Jenis Kelamin")

    st.pyplot(fig1)

with col2:

    fig2, ax2 = plt.subplots()

    usia_data = df_filter["Usia"].value_counts()

    ax2.pie(
        usia_data,
        labels=usia_data.index,
        autopct="%1.1f%%",
        colors=["#06B6D4", "#FBBF24", "#84CC16"]
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
# ====================================
# PIE CHART FREKUENSI PENGGUNAAN
# ====================================

st.header("Frekuensi Penggunaan TikTok Shop")

fig4, ax4 = plt.subplots()

freq = df_filter[
    "Seberapa sering anda menggunakan fitur Tiktok Shop?"
].value_counts()

ax3.pie(
    freq,
    labels=freq.index,
    autopct="%1.1f%%",
    colors=["#3B82F6", "#F59E0B", "#22C55E"]
)

ax3.set_title("Frekuensi Penggunaan")

st.pyplot(fig4)

# ====================================
# VARIABEL PENELITIAN
# ====================================

variabel_mapping = {
    'X1 (Gamifikasi)': [
        'Sistem pengumpulan poin atau level pada TikTok Shop sudah adil. ',
        'Informasi mengenai syarat kenaikan poin atau level pada TikTok Shop sudah jelas dan transparan. ',
        'Saya memahami mekanisme pengumpulan poin atau peningkatan level di TikTok Shop. ',
        'Sistem pemberian poin atau level pada TikTok Shop dapat dipercaya. ',
        'Perolehan poin atau level pada TikTok Shop sesuai dengan aktivitas yang saya lakukan. '
    ],

    'M1 (Tantangan)': [
        'Saya merasa tertantang saat menyelesaikan target atau misi harian di TikTok Shop.',
        'Durasi terbatas pada Flash Sale di TikTok Shop meningkatkan rasa tantangan dalam\nberbelanja.',
        'Saya merasa tertantang untuk bersaing dengan penonton lain dalam memperoleh produk saat sesi Live Shopping di TikTok Shop.',
        'Saya merasa tertantang untuk terus menonton Live Shopping di TikTok Shop.',
        'Saya merasa tertantang saat mengikuti event campaign (misalnya event tanggal kembar) di TikTok Shop.'
    ],

    'M2 (Hiburan)': [
        'Aktivitas seperti Flash Sale di TikTok Shop membuat pengalaman saya menjadi lebih menyenangkan.',
        'Saya merasa terhibur saat berinteraksi dengan fitur Live Shopping di TikTok Shop.',
        'Aktivitas berburu promo di TikTok Shop membuat saya merasa lebih antusias.',
        'Aktivitas di TikTok Shop terasa sebagai hiburan, bukan sekadar kegiatan berbelanja. ',
        'Proses mengumpulkan voucher atau reward di TikTok Shop memberikan kesenangan bagi saya.'
    ],

    'Y (Retensi)': [
        'Saya sering menggunakan TikTok Shop.',
        'Kemudahan dalam mencari barang di TikTok Shop membuat saya lebih sering menggunakannya.',
        'Tampilan TikTok Shop mendorong saya untuk kembali menggunakan aplikasi.',
        'Promo atau diskon di TikTok Shop meningkatkan frekuensi penggunaan saya.',
        'Fitur reward di TikTok Shop mendorong saya untuk terus menggunakan aplikasi.'
    ]
}

# ====================================
# RATA-RATA VARIABEL
# ====================================

st.header("Rata-rata Variabel Penelitian")

rata2_variabel = {
    var: df_filter[cols].mean().mean()
    for var, cols in variabel_mapping.items()
}

fig5, ax5 = plt.subplots(figsize=(8, 5))

bars = ax5.bar(
    rata2_variabel.keys(),
    rata2_variabel.values(),
    color=[
        "#8B5CF6",
        "#EF4444",
        "#84CC16",
        "#3B82F6"
    ]
)

ax5.set_ylim(0, 5)
ax5.set_ylabel("Rata-rata Skor")
ax5.set_title("Rata-rata Skor Variabel")

for bar in bars:
    height = bar.get_height()

    ax5.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.05,
        f"{height:.2f}",
        ha="center"
    )

st.pyplot(fig5)

# ====================================
# SCATTER PLOT
# ====================================

st.header("Hubungan Gamifikasi terhadap Retensi")

df_scatter = df_filter.copy()

df_scatter['Skor_X1'] = (
    df_scatter[
        variabel_mapping['X1 (Gamifikasi)']
    ].mean(axis=1)
)

df_scatter['Skor_Y'] = (
    df_scatter[
        variabel_mapping['Y (Retensi)']
    ].mean(axis=1)
)

fig6, ax6 = plt.subplots(figsize=(8, 6))

ax6.scatter(
    df_scatter['Skor_X1'],
    df_scatter['Skor_Y'],
    color="#60A5FA",
    alpha=0.7,
    s=50
)

ax6.set_xlabel('Skor Gamifikasi (X1)')
ax6.set_ylabel('Skor Retensi (Y)')
ax6.set_title(
    'Hubungan Gamifikasi terhadap Retensi Pengguna'
)

st.pyplot(fig6)
