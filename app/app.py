import streamlit as st
import pandas as pd
import joblib
import os

# ================= CONFIG =================
st.set_page_config(
    page_title="Sleep Disorder Prediction",
    page_icon="💤",
    layout="centered"
)

# ================= STYLE =================
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
.stButton button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
.stNumberInput input {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ================= LOAD MODEL (FIX PATH) =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, 'model_sleep.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))
le_gender = joblib.load(os.path.join(BASE_DIR, 'le_gender.pkl'))
le_occ = joblib.load(os.path.join(BASE_DIR, 'le_occ.pkl'))
le_bmi = joblib.load(os.path.join(BASE_DIR, 'le_bmi.pkl'))
le_target = joblib.load(os.path.join(BASE_DIR, 'le_target.pkl'))

# ================= HEADER =================
st.title("💤 Prediksi Gangguan Tidur")
st.markdown("Aplikasi ini membantu memprediksi risiko **gangguan tidur** berdasarkan kondisi kesehatan Anda.")

st.info("Silakan isi data di bawah ini dengan benar.")

# ================= INPUT =================
st.subheader("👤 Data Diri")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Jenis Kelamin", le_gender.classes_)
    age = st.number_input("Umur", 10, 100, 30)
    occupation = st.selectbox("Pekerjaan", le_occ.classes_)

with col2:
    bmi = st.selectbox("Kategori BMI", le_bmi.classes_)
    heart_rate = st.number_input("Detak Jantung (bpm)", 40, 150, 80)
    steps = st.number_input("Langkah per Hari", 0, 20000, 5000)

# ================= KESEHATAN =================
st.subheader("🩺 Kondisi Kesehatan")

sleep_duration = st.slider("Durasi Tidur (jam)", 0.0, 12.0, 6.0)
quality = st.slider("Kualitas Tidur (1 = buruk, 9 = sangat baik)", 1, 9, 5)
activity = st.slider("Aktivitas Fisik (menit/hari)", 0, 120, 30)
stress = st.slider("Tingkat Stres (1 = rendah, 10 = tinggi)", 1, 10, 5)

st.markdown("### 🩸 Tekanan Darah")
st.caption("Contoh normal: 120 / 80 mmHg")

col3, col4 = st.columns(2)

with col3:
    sys = st.number_input("Tekanan Atas (Systolic)", 80, 200, 120)

with col4:
    dia = st.number_input("Tekanan Bawah (Diastolic)", 60, 150, 80)

# ================= PREDIKSI =================
if st.button("🔍 Prediksi Sekarang"):

    data = pd.DataFrame([{
        'Gender': le_gender.transform([gender])[0],
        'Age': age,
        'Occupation': le_occ.transform([occupation])[0],
        'Sleep Duration': sleep_duration,
        'Quality of Sleep': quality,
        'Physical Activity Level': activity,
        'Stress Level': stress,
        'BMI Category': le_bmi.transform([bmi])[0],
        'Heart Rate': heart_rate,
        'Daily Steps': steps,
        'Systolic_BP': sys,
        'Diastolic_BP': dia
    }])

    # scaling
    data_scaled = scaler.transform(data)

    # prediksi (pakai data_scaled karena training kamu pakai scaler)
    pred = model.predict(data_scaled)[0]
hasil = le_target.inverse_transform([pred])[0]

# ================= FIX LOGIKA BIAR MASUK AKAL =================
if sleep_duration < 4 and stress >= 7:
    hasil = "Insomnia"

if bmi == "Obese" and sys > 140:
    hasil = "Sleep Apnea"

if quality <= 3 and stress >= 8:
    hasil = "Insomnia"

    # ================= OUTPUT =================
    st.subheader("📊 Hasil Prediksi")

    if hasil == "No Disorder":
        st.success("✅ Anda tidak terindikasi gangguan tidur.")
    elif hasil == "Insomnia":
        st.warning("⚠️ Anda berisiko mengalami Insomnia.")
    else:
        st.error("🚨 Anda berisiko mengalami Sleep Apnea.")

    # ================= SARAN =================
    st.markdown("### 💡 Rekomendasi")

    if hasil == "Insomnia":
        st.write("- Kurangi stres")
        st.write("- Perbaiki pola tidur")
        st.write("- Hindari gadget sebelum tidur")
    elif hasil == "Sleep Apnea":
        st.write("- Konsultasi ke dokter")
        st.write("- Perhatikan berat badan")
        st.write("- Hindari tidur telentang")
    else:
        st.write("- Pertahankan gaya hidup sehat")
        st.write("- Tidur cukup dan teratur")