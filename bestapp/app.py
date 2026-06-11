import streamlit as st
import time

# 1. PAGE CONFIGURATION & INITIAL STATE
st.set_page_config(
    page_title="Bharat Heritage Portal",
    page_icon="🇮🇳",
    layout="wide"
)

# Global Session States Initialize karna
if "verified" not in st.session_state:
    st.session_state.verified = False
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "Light Modern"
if "font_profile" not in st.session_state:
    st.session_state.font_profile = "Standard"

# 2. DYNAMIC THEMING & READING MODE ENGINE (CSS)
font_size = "17px" if st.session_state.font_profile == "Standard" else "24px"
bg_color, text_color, card_bg, border_color = ("#FFFFFF", "#212121", "#F8F9FA", "#EAEAEA") if st.session_state.theme_mode == "Light Modern" else ("#111622", "#E2E8F0", "#1A2333", "#2D3748")

st.markdown(f"""
<style>
    .stApp {{ background-color: {bg_color} !important; color: {text_color} !important; }}
    .article-card {{
        background-color: {card_bg};
        border: 1px solid {border_color};
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 22px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }}
    .article-card:hover {{ transform: translateY(-2px); }}
    .article-title {{ color: {text_color}; font-weight: 700; margin-bottom: 8px; }}
    .article-text {{ font-size: {font_size} !important; line-height: 1.7; color: {text_color}; opacity: 0.9; }}
</style>
""", unsafe_allow_html=True)

# 3. ROBOT VERIFICATION GATEWAY
if not st.session_state.verified:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        st.write("")
        st.title("🛡️ Secure Gateway Verification")
        st.subheader("Bharat Heritage Knowledge Portal")
        st.caption("Please pass the automated cryptographic challenge to unlock premium database nodes.")
        st.markdown("---")
        
        # Human Verification Fields
        math_challenge = st.number_input("Security Question: What is 14 + 6?", value=0, min_value=0)
        bot_checkbox = st.checkbox("I confirm that I am a human operator accesssing this cluster.")
        
        if st.button("Authenticate Identity 🚀", type="primary", use_container_width=True):
            if math_challenge == 20 and bot_checkbox:
                st.session_state.verified = True
                st.toast("Identity Confirmed! Provisioning dashboard...", icon="✅")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Authentication Refused. Check math parameters and declaration checkbox.")
    st.stop()

# 4. PROFESSIONAL MULTI-PAGE ROUTING
# Yahan hum pages ko programmatically define kar rahe hain
page_1 = st.Page("pages_content/group_a.py", title="Historic Monuments (1-10)", icon="🏛️", default=True)
page_2 = st.Page("pages_content/group_b.py", title="Natural Wonders (11-20)", icon="🏞️")

# Multi-page Navigation Object Create Karna
pg = st.navigation({
    "🗂️ Explore Datasets": [page_1, page_2]
})

# Sidebar Global Control Widgets Rendering
with st.sidebar:
    st.subheader("🇮🇳 Portal Controls")
    st.write("Welcome, Authorized User")
    st.markdown("---")
    
    # Live State controls linked to global stylesheet
    st.subheader("⚙️ UI Customization")
    st.session_state.theme_mode = st.selectbox("Application Skin", ["Light Modern", "Deep Space Dark"], 
                                                index=0 if st.session_state.theme_mode == "Light Modern" else 1)
    
    st.session_state.font_profile = st.selectbox("Reading Font Matrix", ["Standard", "Large Font (Reading Mode)"],
                                                 index=0 if st.session_state.font_profile == "Standard" else 1)
    
    st.markdown("---")
    if st.button("Lock Session 🔒", use_container_width=True):
        st.session_state.verified = False
        st.rerun()

# Selected page code execute karna
pg.run()