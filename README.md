# 💤 Sleep Disorder Prediction App
Aplikasi berbasis Machine Learning untuk memprediksi risiko gangguan tidur (**Insomnia**, **Sleep Apnea**, atau **No Disorder**) berdasarkan kondisi kesehatan dan gaya hidup pengguna.

## 📌 Deskripsi
Gangguan tidur merupakan masalah kesehatan yang dapat berdampak pada kualitas hidup seseorang. Proyek ini bertujuan untuk membangun model klasifikasi menggunakan algoritma Machine Learning yang mampu memprediksi risiko gangguan tidur berdasarkan berbagai faktor seperti:

* Durasi tidur
* Tingkat stres
* Aktivitas fisik
* Kualitas tidur
* BMI (Body Mass Index)
* Tekanan darah
* dan faktor lainnya

Aplikasi ini dibuat menggunakan **Streamlit** sehingga dapat diakses melalui web secara interaktif.

## 🎯 Tujuan
* Membangun model klasifikasi gangguan tidur
* Membandingkan beberapa algoritma Machine Learning
* Mengimplementasikan model ke dalam aplikasi berbasis web
* Memberikan prediksi yang mudah digunakan oleh pengguna umum

## 🧠 Metode yang Digunakan
### 📊 Dataset
* **Nama**: Sleep Health and Lifestyle Dataset
* **Sumber**: Kaggle
* **Jumlah data**: 374 data
* **Target**: Sleep Disorder
  * No Disorder
  * Insomnia
  * Sleep Apnea

### ⚙️ Tahapan Machine Learning
1. **Data Understanding**
   * Analisis struktur dataset
   * Identifikasi missing values

2. **Data Preprocessing**
   * Menghapus fitur tidak relevan (Person ID)
   * Split Blood Pressure → Systolic & Diastolic
   * Encoding data kategorikal
   * Normalisasi (StandardScaler)

3. **Exploratory Data Analysis (EDA)**
   * Visualisasi distribusi data
   * Analisis hubungan antar fitur

4. **Modeling**
   Menggunakan 3 algoritma:
   * K-Nearest Neighbor (KNN)
   * Decision Tree (DT)
   * Random Forest (RF)

5. **Hyperparameter Tuning**
   * Menggunakan GridSearchCV
     
6. **Evaluation**
   * Accuracy
   * Precision
   * Recall
   * F1-Score
   * Confusion Matrix

## 🌐 Live Demo
Aplikasi dapat diakses secara online melalui link berikut:
👉 https://sleep-disorder-app-p.streamlit.app/

## ⚙️ Cara Menjalankan (Local)
1. Clone Repository
bash
git clone https://github.com/neysarazana/sleep-disorder-app.git
cd sleep-disorder-app

3. Install Dependency
bash
pip install -r requirements.txt

4. Jalankan Aplikasi
bash
streamlit run app.py

5. Buka di Browser
http://localhost:8501

## 📁 Struktur Project
sleep-disorder-app/
│
├── app.py                 # Aplikasi Streamlit
├── model_sleep.pkl        # Model Machine Learning
├── scaler.pkl             # Scaler
├── le_gender.pkl          # Encoder gender
├── le_occ.pkl             # Encoder pekerjaan
├── le_bmi.pkl             # Encoder BMI
├── le_target.pkl          # Encoder target
├── requirements.txt       # Dependency
└── README.md              # Dokumentasi

## 💡 Fitur Aplikasi
* Input data pengguna secara interaktif
* Prediksi gangguan tidur secara real-time
* Tampilan user-friendly
* Rekomendasi berdasarkan hasil prediksi

## ⚠️ Catatan
* Model hanya digunakan untuk tujuan edukasi
* Tidak menggantikan diagnosis medis profesional

## 👨‍💻 Author
Nama: Neysa Razana
