import streamlit as st

st.set_page_config(
    page_title="UGC AI Commercial Director - Pemula & Emak-Emak",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF4B4B, #FF8E53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 1rem;
        color: #94A3B8;
        margin-bottom: 20px;
    }
    .status-badge {
        background-color: #10B981;
        color: white;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎬 UGC AI Commercial Director</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Mode Pemula & Emak-Emak • Tinggal Isi Nama Barang ➔ Klik 1 Tombol ➔ Iklan Otomatis Jadi!</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("📋 Form Iklan Praktis")
    
    st.subheader("1. Barang Jualan")
    product_name = st.text_input("Nama Produk / Barang", value="Flame Gun + Gas Cane", help="Contoh: Gamis Busui, Sambal Bawang, Senter 1000 Lumen")
    product_desc = st.text_area("Deskripsi / SS Toko (Opsional)", 
                                value="Flame gun pemantik api bodi alumunium kokoh, bisa dicolok ke kaleng gas portable. Cocok buat masak, bakar keju, dan outdoor.",
                                help="Bisa copy-paste teks promo toko di sini.")
    product_img = st.file_uploader("Upload Foto Barang / SS Toko (Opsional)", type=["jpg", "png", "webp"])
    
    st.subheader("2. Gaya Video (Style)")
    style_option = st.selectbox(
        "Pilih Style Video:",
        [
            "🤖 Otomatis Pilihkan (AI Decides)",
            "🔥 Tham Story / Barbaric Gen Z (Absurd, Kocak, Relate)",
            "⭐ Review Jujur Emak-Emak (Polos, Realistis, Persuasif)",
            "✨ Street Commercial (Modern, Energetik, Urban)",
            "💎 Luxury Film (Mewah, Elegan, Premium)",
            "🌿 Aesthetic Lifestyle (Calm, Soft, Minimalis)",
            "✏️ Custom Style (Ketik Sendiri...)"
        ]
    )
    
    aspect_ratio = st.selectbox(
        "Ukuran Layar (Rasio):",
        ["9:16 (Tegak - TikTok / Reels / Shorts)", "3:4 (Katalog Shopee / Feed IG)", "16:9 (Mendatar - YouTube)"]
    )

    st.subheader("3. Gaya Suara (Voice-Over)")
    col_gender, col_vibe = st.columns(2)
    with col_gender:
        narrator_gender = st.selectbox(
            "Gender Suara:",
            ["🤖 Auto AI", "👨 Pria Barbar", "👨 Pria Berat/Serius", "👩 Wanita Gen-Z", "👩 Wanita Ibu-Ibu Ramah", "👥 Duet"]
        )
    with col_vibe:
        narrative_vibe = st.selectbox(
            "Vibe Suara:",
            ["🔥 Barbaric Tham Story", "⚡ Energetik", "😌 Ngobrol Santai", "🤫 ASMR / Soft", "💰 Hard-Sell Promo"]
        )

    st.subheader("4. Tambahan (Opsional)")
    talent_option = st.selectbox(
        "Pilihan Model/Talent:",
        ["Emak-Emak Santai", "Anak Muda Ceria", "Tanpa Talent (Fokus Produk)", "Custom Talent"]
    )
    custom_hook = st.text_input("Ide Kata Pembuka / Hook Sendiri (Opsional)", placeholder="Kosongkan jika ingin AI yang buatkan otomatis")
    
    st.markdown("---")
    btn_generate = st.button("🚀 BIKIN DRAFT IKLAN SEKARANG", type="primary", use_container_width=True)

st.info("💡 **Petunjuk:** Cukup isi nama barang di sebelah kiri, lalu klik **BIKIN DRAFT IKLAN SEKARANG**!")

tab1, tab2, tab3 = st.tabs(["🖼️ Step 1: Preview 4 Gambar Adegan", "🎙️ Step 2: Naskah Suara (Script VO)", "⚡ Step 3: Prompt Video Sekali Copy"])

with tab1:
    st.subheader("🖼️ Preview 4 Gambar Acuan Adegan (Keyframe)")
    st.caption("Cek dulu bentuk produk dan adegannya di sini sebelum diubah jadi video.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**Scene 1: Drama Hook**")
        st.image("https://images.unsplash.com/photo-1508873696983-2df515122519?w=400", caption="Scene 1: Mati Lampu / Susah Nyala")
        st.markdown("<span class='status-badge'>✅ Product Lock OK</span>", unsafe_allow_html=True)
    with col2:
        st.markdown("**Scene 2: Cara Pakai**")
        st.image("https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=400", caption="Scene 2: Rakit & Nyalakan")
        st.markdown("<span class='status-badge'>✅ Action Lock OK</span>", unsafe_allow_html=True)
    with col3:
        st.markdown("**Scene 3: WOW Payoff**")
        st.image("https://images.unsplash.com/photo-1517420704952-d9f39e95b43e?w=400", caption="Scene 3: Api Biru Bakar Keju")
        st.markdown("<span class='status-badge'>✅ Style Lock OK</span>", unsafe_allow_html=True)
    with col4:
        st.markdown("**Scene 4: Penutup / CTA**")
        st.image("https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400", caption="Scene 4: Senyum Puas & Ajakan Beli")
        st.markdown("<span class='status-badge'>✅ Outro Lock OK</span>", unsafe_allow_html=True)

with tab2:
    st.subheader("🎙️ Naskah Narasi Suara (Voice-Over)")
    st.markdown(f"**Barang:** `{product_name}` | **Style:** `{style_option}` | **Suara:** `{narrator_gender}` ({narrative_vibe})")
    st.markdown("""
    * **Detik 0–2 (Hook):** *Woylah! Ini mau bakar sate apa mau tiup balon?! Ditiupin sampe paru-paru kempes juga gak bakal nyala!*
    * **Detik 2–4 (Fitur):** *Tinggal tancap Flame Gun ke kaleng gas, putar knob, terus... CETEK! Semburan apinya langsung ngebakar emosi!*
    * **Detik 4–7 (Aksi):** *Keju meleleh instan, daging mateng sempurna, berasa dapet pencerahan gaib dari Chef bintang lima!*
    * **Detik 7–10 (CTA):** *Masak makin sat-set, perut kenyang, arwah lo tetep tenang! Buruan bungkus!*
    """)

with tab3:
    st.subheader("⚡ Master Prompts (Siap Copy ke Generator Video)")
    st.text_area("Prompt Siap Pakai (Runway / Kling / Luma / Google Flow):", 
                 value=f"Product: {product_name}\nAspect Ratio: {aspect_ratio}\nStyle: {style_option}\n\n[SCENE 1 - HOOK]\nImage: Asian male looking frustrated in modern kitchen blowing charcoal smoke.\nMotion: Fast handheld push-in camera movement.\n\n[SCENE 2 - ASSEMBLY]\nImage: Close-up male hands snapping metal Flame Gun head onto butane gas canister.\nMotion: Tracking shot following hand motion with ignition spark.", 
                 height=200)
