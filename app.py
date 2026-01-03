import streamlit as st
import time
from main import run

# 1. Sayfa Yapılandırması
st.set_page_config(
    page_title="AI Startup Scout | Autonomous Analyst",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sade ve Etkili Stil (Okunurluk Odaklı)
st.markdown("""
    <style>
    /* Ana başlık (H1) rengi - Açık Beyaz/Gri */
    .stApp h1 {
        color: #F8FAFC !important;
        font-weight: 800;
    }
    
    /* Rapor başlıkları (H2 ve H3) - Açık Mavi tonu */
    h2, h3 {
        color: #60A5FA !important; /* Daha görünür bir mavi */
        padding-top: 1.5rem;
        background-color: transparent !important; /* Arka plan vurgusunu temizler */
    }

    /* Normal metinlerin okunurluğu için (Markdown içindeki yazılar) */
    .stMarkdown p {
        color: #E2E8F0;
    }

    /* Sidebar düzenlemesi */
    .stSidebar {
        background-color: #111827; /* Sidebar'ı biraz daha belirgin bir koyu ton yapar */
    }
    
    /* Sidebar başlıkları */
    .stSidebar h1, .stSidebar h2, .stSidebar h3 {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- YARDIMCI FONKSİYONLAR ---
def stream_text(text):
    """Metni ekrana daktilo efektiyle yazar."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80) # Opsiyonel logo
    st.title("Settings")
    
    sector = st.selectbox(
        "Target Industry Sector",
        options=["Healthcare", "Finance", "Enterprise Software", "Retail", "Cybersecurity", "LegalTech"],
        help="Ajanlar bu sektöre odaklanarak derinlemesine araştırma yapacak."
    )
    
    st.divider()
    run_button = st.button("🚀 Start Scouting Agents", use_container_width=True, type="primary")
    
    st.info("💡 **Tip:** Agents will perform real-time web crawling and competitive analysis.")
    
    st.caption("Developed by **Yusuf Ataş** | Software Engineer")

# --- ANA ALAN ---
st.title("🚀 AI Startup Scout")
st.markdown("##### *Autonomous Multi-Agent System for Deep Market Intelligence*")

if not run_button:
    # Başlangıç Ekranı (Daha şık bir karşılama)
    st.empty()
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("")
        st.markdown("""
        ### Welcome to the Future of Market Research.
        Bu sistem, **CrewAI** altyapısını kullanarak sizin yerinize interneti tarar, 
        startup'ları sınıflandırır ve yatırım yapılabilirliği analiz eder.
        
        **Neler bekleyebilirsiniz?**
        - 🔍 Gerçek zamanlı web taraması (Tavily AI)
        - 📊 Disruption Score hesaplamaları
        - 📄 Profesyonel yönetici raporu
        """)
    with col2:
        with st.expander("🛠️ System Architecture", expanded=True):
            st.info("""
            1. **Discovery Agent**
            2. **Classification Agent**
            3. **Insight Agent**
            4. **Reporting Agent**
            """)

else:
    # ÇALIŞMA ANI
    with st.status("🤖 Agents are collaborating...", expanded=True) as status:
        st.write("🔍 **Discovery Agent:** Searching for emerging AI startups...")
        # Simüle edilmiş veya gerçek loglar buraya gelebilir
        
        # Gerçek fonksiyonu çağırıyoruz
        result = run(sector=sector)
        
        status.update(label="✅ Analysis Complete!", state="complete", expanded=False)

    # RAPOR ALANI
    st.toast(f"{sector} analizi başarıyla tamamlandı!", icon='✅')
    
    # Header & Download
    header_col, download_col = st.columns([3, 1])
    with header_col:
        st.subheader(f"📄 Executive Analysis Report: {sector}")
    with download_col:
        st.download_button(
            label="📥 Download Report",
            data=result,
            file_name=f"AI_Scout_{sector}.md",
            mime="text/markdown",
            use_container_width=True
        )

    # CANLI YAZDIRMA EFEKTİ (Daktilo Efekti)
    st.markdown("---")
    with st.container():
        # result verisini stream_text üzerinden akıtıyoruz
        st.write_stream(stream_text(result))

    st.balloons()