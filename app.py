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
        options=["HealthTech", "Fintech", "Sports", "B2B SaaS", "Logistics / Supply Chain", "Cybersecurity", "Sustainability",],
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
        Leveraging the **CrewAI** framework, this autonomous system scouts the web on your behalf, 
        categorizes emerging startups, and evaluates their investment viability.
        
        **Key Capabilities:**
        - 🔍 **Real-time Web Intelligence:** Powered by Tavily AI for precise data extraction.
        - 📊 **Strategic Scoring:** Quantitative analysis including 'Disruption' and 'Confidence' scores.
        - 📄 **Executive Reporting:** High-quality Markdown reports tailored for stakeholders.
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
    # === AGENT ÇALIŞMA SÜRECİ (SEVİYE 1 UX) ===
    with st.status("🤖 Agents are collaborating...", expanded=True) as status:
        st.write("🔍 **Discovery Agent:** Scanning the web for AI-first startups...")
        time.sleep(1)

        st.write("🧠 **Classification Agent:** Filtering and categorizing startups...")
        time.sleep(1)

        st.write("📊 **Insight Agent:** Evaluating disruption potential and moats...")
        time.sleep(1)

        st.write("📝 **Reporting Agent:** Synthesizing executive report...")
        
        # 🔥 Asıl ağır iş burada (blocking)
        result = run(sector=sector)

        status.update(
            label="✅ Analysis Complete!",
            state="complete",
            expanded=False
        )

    # === RAPOR GÖSTERİMİ ===
    st.toast(f"{sector} analysis completed successfully!", icon="✅")

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

    st.markdown("---")

    # Daktilo efekti (sadece final rapor)
    st.write_stream(stream_text(result))
