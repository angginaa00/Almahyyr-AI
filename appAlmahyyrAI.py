import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import io

# ==========================================
# 1. KONFIGURASI HALAMAN & TAMPILAN (UI/UX)
# ==========================================
st.set_page_config(page_title="Almahyyr AI", page_icon="🎓", layout="wide")

# CSS Kustom untuk tampilan yang penuh warna, modern, dan cocok untuk MTs
st.markdown("""
<style>
    .main { background-color: #f4f9f9; }
    h1 { color: #2E86AB; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; font-weight: 800;}
    h2, h3 { color: #A23B72; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton>button { background-color: #F18F01; color: white; border-radius: 15px; font-weight: bold; border: none; padding: 10px 20px; transition: 0.3s; }
    .stButton>button:hover { background-color: #C73E1D; color: white; transform: scale(1.05); }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .arabic-text { font-size: 28px; font-family: 'Amiri', 'Lateef', 'Arial', sans-serif; text-align: right; direction: rtl; color: #2b2b2b; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INISIALISASI SESSION STATE (Manajemen Sesi)
# ==========================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ustadz_choice" not in st.session_state:
    st.session_state.ustadz_choice = "Ustadz Rafli"

# ==========================================
# 3. HALAMAN LOGIN (Otentikasi API)
# ==========================================
if not st.session_state.logged_in:
    st.markdown("<h1>🌟 Selamat Datang di Almahyyr AI 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Platform Pembelajaran Bahasa Arab Interaktif Kelas 8 MTs</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        username_input = st.text_input("👤 Nama Pengguna (Username):")
        api_key_input = st.text_input("🔑 Google AI Studio API Key:", type="password")
        
        if st.button("🚀 Masuk / الدُّخُولُ (Login)"):
            if username_input and api_key_input:
                try:
                    # Validasi API Key dengan mencoba konfigurasi
                    genai.configure(api_key=api_key_input)
                    # Uji coba ringan
                    model = genai.GenerativeModel("gemini-2.5-flash")
                    st.session_state.logged_in = True
                    st.session_state.username = username_input
                    st.session_state.api_key = api_key_input
                    st.rerun()
                except Exception as e:
                    st.error(f"API Key tidak valid atau terjadi kesalahan: {e}")
            else:
                st.warning("Silakan masukkan Username dan API Key terlebih dahulu!")
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 4. HALAMAN UTAMA (Aplikasi Berjalan)
# ==========================================
else:
    genai.configure(api_key=st.session_state.api_key)
    model = genai.GenerativeModel("gemini-2.5-flash") # Model yang mendukung teks dan audio

    # --- SIDEBAR PENGATURAN ---
    with st.sidebar:
        st.markdown("### ⚙️ Pengaturan Pembelajaran")
        st.session_state.ustadz_choice = st.selectbox(
            "Pilih Pengajar Anda:", 
            ["Ustadz Rafli 👨‍🏫", "Ustadzah Fatimah 👩‍🏫"]
        )
        
        mode_pembelajaran = st.radio(
            "Pilih Mode Pembelajaran:",
            ["1️⃣ Mufradat (Kosakata)", "2️⃣ Maharah Istima' (Mendengar)", "3️⃣ Maharah Kalam (Berbicara)", "💬 Chat Interaktif"]
        )
        
        st.markdown("---")
        if st.button("🚪 Keluar / الخُرُوجُ (Exit)"):
            st.session_state.clear()
            st.rerun()

    # Tentukan Avatar dan Nama Pengajar
    avatar_img = "👨‍🏫" if "Rafli" in st.session_state.ustadz_choice else "👩‍🏫"
    nama_pengajar = "الأُسْتَاذُ رَفْلِي" if "Rafli" in st.session_state.ustadz_choice else "الأُسْتَاذَةُ فَاطِمَةُ"

    st.markdown(f"<h1>Almahyyr AI - {st.session_state.ustadz_choice}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='arabic-text' style='text-align: center;'>أَهْلًا وَسَهْلًا بِكَ يَا {st.session_state.username} فِي مَنْصَةِ الْمَاهِير، أَنَا {nama_pengajar}</p>", unsafe_allow_html=True)

    # ==========================================
    # MODE 1: MUFRADAT (KOSAKATA TENTANG AL-MADROSAH)
    # ==========================================
    if mode_pembelajaran == "1️⃣ Mufradat (Kosakata)":
        st.markdown("### 📚 المُفْرَدَاتُ عَنِ الْمَدْرَسَةِ (Kosakata tentang Sekolah)")
        st.info("Pelajari kosakata dan kata kerja berikut beserta gambarnya.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 50px;'>🏫</h1>", unsafe_allow_html=True)
            st.markdown("<p class='arabic-text'>مَدْرَسَةٌ</p>", unsafe_allow_html=True)
            st.caption("Sekolah")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 50px;'>📖</h1>", unsafe_allow_html=True)
            st.markdown("<p class='arabic-text'>يَقْرَأُ</p>", unsafe_allow_html=True)
            st.caption("Membaca (Kata Kerja)")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 50px;'>👨‍🎓</h1>", unsafe_allow_html=True)
            st.markdown("<p class='arabic-text'>طَالِبٌ</p>", unsafe_allow_html=True)
            st.caption("Siswa")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 50px;'>✍️</h1>", unsafe_allow_html=True)
            st.markdown("<p class='arabic-text'>يَكْتُبُ</p>", unsafe_allow_html=True)
            st.caption("Menulis (Kata Kerja)")
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 50px;'>🪑</h1>", unsafe_allow_html=True)
            st.markdown("<p class='arabic-text'>فَصْلٌ</p>", unsafe_allow_html=True)
            st.caption("Kelas")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
            st.markdown("<h1 style='font-size: 50px;'>🗣️</h1>", unsafe_allow_html=True)
            st.markdown("<p class='arabic-text'>يَتَكَلَّمُ</p>", unsafe_allow_html=True)
            st.caption("Berbicara (Kata Kerja)")
            st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # MODE 2: MAHARAH ISTIMA' (MENDENGAR)
    # ==========================================
    elif mode_pembelajaran == "2️⃣ Maharah Istima' (Mendengar)":
        st.markdown("### 🎧 مَهَارَةُ الِاسْتِمَاعِ (Keterampilan Mendengar)")
        st.write("Tekan tombol putar di bawah ini, dengarkan baik-baik (اسْتَمِعْ جَيِّدًا), dan pahami cerita tentang sekolah!")
        
        teks_istima = "هَذِهِ مَدْرَسَتِي. هِيَ كَبِيرَةٌ وَجَمِيلَةٌ. فِي الْمَدْرَسَةِ فُصُولٌ كَثِيرَةٌ، وَمَكْتَبَةٌ، وَمَلْعَبٌ وَاسِعٌ. أَنَا أَدْرُسُ اللُّغَةَ الْعَرَبِيَّةَ فِي الْفَصْلِ مَعَ أَصْدِقَائِي."
        
        # Menggunakan gTTS untuk men-generate audio native
        try:
            tts = gTTS(text=teks_istima, lang='ar', slow=False)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            
            st.audio(fp, format='audio/mp3')
            
            with st.expander("Tampilkan Teks (Show Text)"):
                st.markdown(f"<p class='arabic-text'>{teks_istima}</p>", unsafe_allow_html=True)
                st.write("Ini sekolahku. Ia besar dan indah. Di sekolah ada banyak kelas, perpustakaan, dan lapangan yang luas. Saya belajar bahasa Arab di kelas bersama teman-temanku.")
        except Exception as e:
            st.error(f"Gagal memuat audio. Pastikan koneksi internet stabil. Error: {e}")

    # ==========================================
    # MODE 3: MAHARAH KALAM (BERBICARA - ROLE PLAY)
    # ==========================================
    elif mode_pembelajaran == "3️⃣ Maharah Kalam (Berbicara)":
        st.markdown("### 🎙️ مَهَارَةُ الْكَلَامِ (Keterampilan Berbicara & Role Play)")
        st.info("Mari bermain peran (Role Play)! Jawab pertanyaan pengajar menggunakan rekaman suara Anda di bawah ini.")
        
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        pertanyaan_kalam = "أَيْنَ تَتَعَلَّمُ اللُّغَةَ الْعَرَبِيَّةَ وَمَاذَا تَعْمَلُ فِي الْفَصْلِ؟"
        st.markdown(f"**{st.session_state.ustadz_choice} bertanya:**")
        st.markdown(f"<p class='arabic-text'>{pertanyaan_kalam}</p>", unsafe_allow_html=True)
        st.caption("*(Di mana kamu belajar bahasa Arab dan apa yang kamu lakukan di kelas?)*")
        st.markdown("</div>", unsafe_allow_html=True)

        st.write("سَجِّلْ صَوْتَكَ هُنَا (Rekam suara Anda di sini):")
        # Fitur st.audio_input (Membutuhkan Streamlit >= 1.36.0)
        audio_value = st.audio_input("Rekam Suara")

        if audio_value is not None:
            st.success("Rekaman berhasil disimpan! Anda dapat memutarnya kembali sebelum mengirim.")
            
            if st.button("أَرْسِلْ لِلتَّقْيِيمِ (Kirim untuk Dinilai)"):
                with st.spinner('Sedang dinilai oleh AI...'):
                    try:
                        # Mempersiapkan data audio untuk Gemini
                        audio_data = {
                            "mime_type": "audio/wav",
                            "data": audio_value.getvalue()
                        }
                        
                        prompt_evaluasi = f"""
                        Bertindaklah sebagai {st.session_state.ustadz_choice}, guru bahasa Arab MTs yang ramah. 
                        Siswa kelas 8 baru saja menjawab pertanyaan ini secara lisan: "{pertanyaan_kalam}".
                        Dengarkan rekaman audio yang dikirim. Evaluasi pengucapan bahasa Arabnya, 
                        berikan nilai dari skala 1-100, dan berikan umpan balik yang membangun menggunakan bahasa Indonesia.
                        Gunakan sedikit ungkapan apresiasi dalam bahasa Arab di awal.
                        """
                        
                        response = model.generate_content([prompt_evaluasi, audio_data])
                        
                        st.markdown("<div class='card'>", unsafe_allow_html=True)
                        st.markdown("#### 📝 Hasil Penilaian:")
                        st.write(response.text)
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"Terjadi kesalahan saat memproses audio. Error: {e}")

    # ==========================================
    # MODE 4: CHAT INTERAKTIF (CONVERSATION HISTORY)
    # ==========================================
    elif mode_pembelajaran == "💬 Chat Interaktif":
        st.markdown(f"### 💬 حِوَارٌ مَعَ {nama_pengajar} (Percakapan)")
        
        # Menampilkan riwayat percakapan
        for message in st.session_state.messages:
            with st.chat_message(message["role"], avatar=avatar_img if message["role"] == "assistant" else "🧑‍🎓"):
                st.markdown(message["content"])

        # Input dari pengguna (Chat)
        if prompt := st.chat_input("اُكْتُبْ رِسَالَتَكَ هُنَا (Tulis pesanmu di sini)..."):
            # Tambahkan pesan user ke state
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user", avatar="🧑‍🎓"):
                st.markdown(prompt)

            # AI merespons
            with st.chat_message("assistant", avatar=avatar_img):
                try:
                    # Membangun konteks percakapan untuk Gemini
                    konteks = f"""
                    Anda adalah {st.session_state.ustadz_choice}, guru Bahasa Arab untuk siswa MTs kelas 8.
                    Nama siswa adalah {st.session_state.username}. Materi saat ini adalah "Al-Madrosah" (Sekolah).
                    Gunakan sapaan islami, berikan harakat (syakal) pada setiap kalimat Bahasa Arab, 
                    dan terjemahkan ke bahasa Indonesia untuk instruksi/penjelasan.
                    Jawablah pesan berikut dari siswa: {prompt}
                    """
                    
                    response = model.generate_content(konteks)
                    st.markdown(response.text)
                    # Simpan balasan AI ke riwayat
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Sistem sedang sibuk atau ada masalah API. Error: {e}")