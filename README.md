# Analisis Data Penyewaan Sepeda

## Ikhtisar

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan data historis. Analisis meliputi tren harian dan per jam, pengaruh cuaca, proyek ini juga mencakup dashboard interaktif menggunakan Streamlit untuk memvisualisasikan hasil analisis secara lebih intuitif.

## Penulis

- **Nama:** Muhammad Azhar Fikri
- **Email:** [muhammadazharfikri990@gmail.com](mailto\:muhammadazharfikri990@gmail.com)

## Struktur Folder

- `notebooks/`: Berisi Notebook Jupyter untuk eksplorasi dan analisis data.
- `dashboard/`: Folder yang berisi kode untuk aplikasi Streamlit.
- `data/`: Menyimpan dataset yang digunakan dalam analisis.
- `assets/`: Berisi gambar atau aset lain yang digunakan dalam proyek.

## Temuan Kunci

- **Pola Harian**: Penyewaan sepeda meningkat pada jam sibuk pagi dan sore hari.
- **Pengaruh Cuaca**: Kondisi cuaca seperti hujan dan suhu ekstrem memengaruhi jumlah penyewaan.

## Cara Menjalankan

1. Pastikan Anda memiliki Python dan pustaka yang diperlukan telah terinstal.
2. Untuk menjalankan notebook analisis, gunakan Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Untuk menjalankan dashboard Streamlit:
   ```bash
   cd dashboard
   streamlit run dashboard.py
   ```

## Kebutuhan dan Instalasi

Pastikan pustaka berikut telah terinstal sebelum menjalankan proyek ini:

- Matplotlib 3.8.3
- NumPy 1.26.4
- Pandas 2.2.0
- Plotly 5.19.0
- Seaborn 0.13.2
- Streamlit 1.31.1

Instal semua pustaka dengan perintah berikut:

```bash
pip install matplotlib numpy pandas plotly seaborn streamlit
```

Proyek ini dikembangkan untuk membantu memahami faktor yang memengaruhi permintaan penyewaan sepeda dan memberikan wawasan berbasis data bagi pengelola layanan penyewaan.