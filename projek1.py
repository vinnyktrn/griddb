import streamlit as st
import pandas as pd


# Data gula per 100 gram buah (untuk contoh, Anda bisa menambahkan lebih banyak buah)
buah_data = {
    'Nama Buah': ['Apel', 'Arbei', 'Apricot', 'Anggur', 'Alpukat', 'Bit' , 'Belimbing','Bengkuang','Blueberi','Blewah','Ceri','Ciplukan','Carica','Cermai','Cranberry','Cempedak','Delima','Durian','Duku','Jeruk','Jambu Biji','Jambu Air','Kurma', 'Kedondong','Kelapa','Kecapi','Kelengkeng','Kiwi','Kesemek','Leci','Labu','Lemon','Mangga','Murbei','Matoa','Mengkudu', 'Manggis','Melon','Markisa','Naga','Nangka','Nanas','Pepaya','Pir','Persik','Plum','Pisang','Rambutan','Sirsak','Sukun','Salak','Stroberi','Semangka','Sawo','Tin','Tomat','Tebu','Timun','Zaitun'],
    'Gula (gram)': [10,8,9,16,0.7,8,5,1.8,14,8,8,3,3,3,4,13.5,16,19,20,9,9,4.5,66,6,3,14,65,9,20,21.5,3.5,2.5,13.7,8,21,8,15.6,8,11,13,19.3,10,7.8,10,10,10,12,15,13.5,24.5,21,7.4,6,18,16,2.6,16,5,0],  # Gula per 100 gram
}
#untuk input gambar background
def add_gradient_overlay_background(image_url, overlay_opacity=1):
    """
    Menambahkan background gambar dengan overlay warna hitam dan opacity yang dapat diatur.
    
    Parameters:
    - image_url: URL gambar untuk background.
    - overlay_opacity: Opacity overlay hitam (0.0 - 1.0).
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: 
                linear-gradient(
                    rgba(0, 0, 0, {overlay_opacity}), /* Overlay warna hitam dengan opacity */
                    rgba(0, 0, 0, {overlay_opacity})
                ),
                url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL gambar Anda (ganti dengan URL gambar yang Anda gunakan)
image_url = "https://akcdn.detik.net.id/community/media/visual/2022/05/16/buah-buahan-1_169.jpeg?w=700&q=90"

# Tambahkan background dengan overlay hitam (opacity 0.5)
add_gradient_overlay_background(image_url, overlay_opacity=0.7)



# Membuat DataFrame untuk buah
df_buah = pd.DataFrame(buah_data)

# Fungsi untuk menghitung kebutuhan gula berdasarkan berat badan dan usia
def hitung_kebutuhan_gula(usia, berat_badan):
    # Asumsi kebutuhan gula (contoh: 10% dari kalori harian, dengan 1 gram gula = 4 kalori)
    kebutuhan_kalori = berat_badan * 24  # Asumsi 24 kalori per kg berat badan
    kebutuhan_gula = (kebutuhan_kalori * 0.1) / 4  # 10% kalori berasal dari gula
    return kebutuhan_gula

# Fungsi untuk menghitung gula dalam jumlah buah yang dikonsumsi
def hitung_gula_buah(fruit, jumlah_gram):
    gula_per_100gram = df_buah[df_buah['Nama Buah'] == fruit]['Gula (gram)'].values[0]
    gula_total = (gula_per_100gram / 100) * jumlah_gram
    return gula_total

# Tampilan Streamlit
st.title("Kalkulator Kebutuhan gula manusia dalam buah ")

# Input Usia dan Berat Badan
usia = st.number_input("Masukkan Usia (tahun)", min_value=1, max_value=100, value=30)
berat_badan = st.number_input("Masukkan Berat Badan (kg)", min_value=30, max_value=200, value=70)

# Hitung kebutuhan gula berdasarkan berat badan dan usia
kebutuhan_gula = hitung_kebutuhan_gula(usia, berat_badan)
st.write(f"Kebutuhan gula harian Anda adalah sekitar {kebutuhan_gula:.2f} gram.")

# Input Buah dan jumlahnya
buah_terpilih = st.multiselect("Pilih Buah", df_buah['Nama Buah'].tolist())
jumlah_buah = st.number_input("Masukkan Jumlah Buah yang Akan Dikirim (gram)", min_value=50, max_value=1000, value=100)

# Menampilkan informasi gula dari buah yang dipilih
if buah_terpilih:
    for buah in buah_terpilih:
        gula_buah = hitung_gula_buah(buah, jumlah_buah)
        st.write(f"Untuk {jumlah_buah} gram {buah}, Anda akan mengkonsumsi {gula_buah:.2f} gram gula.")

    total_gula = sum([hitung_gula_buah(buah, jumlah_buah) for buah in buah_terpilih])
    st.write(f"Total gula yang dikonsumsi dari buah-buah terpilih: {total_gula:.2f} gram.")
    
# Fungsi untuk memberikan kesimpulan korelasi
def kesimpulan(usia, berat_badan, total_gula, kebutuhan_gula):
    if usia < 18:
        usia_kategori = "usia muda"
    elif 18 <= usia <= 60:
        usia_kategori = "usia dewasa"
    else:
        usia_kategori = "usia tua"

    if total_gula > kebutuhan_gula:
        rekomendasi = "Anda telah mengonsumsi gula melebihi kebutuhan harian. Kurangi konsumsi buah dengan kadar gula tinggi."
    elif total_gula < kebutuhan_gula * 0.5:
        rekomendasi = "Anda mengonsumsi gula jauh di bawah kebutuhan harian. Anda bisa menambah konsumsi buah."
    else:
        rekomendasi = "Anda mengonsumsi gula dalam kisaran yang sehat. Pertahankan pola konsumsi ini."

    kesimpulan_teks = (
        f"Dengan kategori {usia_kategori} dan berat badan {berat_badan} kg, kebutuhan gula harian Anda adalah sekitar {kebutuhan_gula:.2f} gram.\n"
        f" total gula sebesar {total_gula:.2f} gram dari buah-buahan yang dipilih.\n"
        f"{rekomendasi}"
    )
    return kesimpulan_teks

# Hitung dan tampilkan kesimpulan
if buah_terpilih:
    kesimpulan_teks = kesimpulan(usia, berat_badan, total_gula, kebutuhan_gula)
    st.subheader("Kesimpulan")
    st.write(kesimpulan_teks)
