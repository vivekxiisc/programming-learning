import streamlit as st
import yt_dlp
import os

# Page Config
st.set_page_config(page_title="Vivek's Pro Downloader", layout="wide", page_icon="📥")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; font-weight: bold; }
    .download-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Function to get video info using yt-dlp
def get_video_info(url):
    ydl_opts = {'quiet': True, 'noplaylist': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            return ydl.extract_info(url, download=False)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return None

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
page = st.sidebar.selectbox("Kahan se download karna hai?", 
    ["YouTube Hub", "Meta Hub (FB & Insta)", "DP & Thumbnails"])

# --- PAGE 1: YOUTUBE HUB ---
if page == "YouTube Hub":
    st.title("📺 YouTube Video & Audio Hub")
    st.write("Download any YouTube video in your preferred quality.")
    
    yt_url = st.text_input("Paste YouTube Link:", placeholder="https://www.youtube.com/watch?v=...")
    
    if yt_url:
        info = get_video_info(yt_url)
        if info:
            st.markdown(f"### 🎥 {info.get('title')}")
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(info.get('thumbnail'), use_container_width=True)
            
            with col2:
                # Video Qualities
                st.subheader("🎞️ Video Qualities")
                formats = info.get('formats', [])
                
                # Filtering unique resolutions
                video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('height')]
                res_options = sorted(list(set([f"{f['height']}p - {f['ext']}" for f in video_formats])), key=lambda x: int(x.split('p')[0]), reverse=True)
                
                selected_res = st.selectbox("Resolution Chunein:", res_options)
                
                # Audio Qualities
                st.subheader("🎵 Audio Qualities")
                audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']
                audio_options = [f"{f.get('abr', 'Unknown')}kbps - {f['ext']}" for f in audio_formats]
                
                selected_audio = st.selectbox("Audio Quality Chunein:", audio_options)
                
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button("🚀 Download Video"):
                        st.success(f"Processing {selected_res}... Check your terminal/server.")
                with btn_col2:
                    if st.button("🎸 Download MP3"):
                        st.success(f"Converting to {selected_audio}...")

# --- PAGE 2: META HUB (FB & INSTA) ---
elif page == "Meta Hub (FB & Insta)":
    st.title("📱 Meta Downloader (Facebook & Instagram)")
    
    # Tabs for separation as requested
    tab1, tab2 = st.tabs(["📸 Instagram (Reels/Stories)", "🔵 Facebook Videos"])
    
    with tab1:
        st.subheader("Instagram Downloader")
        insta_link = st.text_input("Paste Instagram URL:", key="insta")
        st.info("Reels, IGTV aur Stories ke liye link daalein.")
        if st.button("Get Insta Media"):
            st.info("Fetching from Instagram...")

    with tab2:
        st.subheader("Facebook Video Downloader")
        fb_link = st.text_input("Paste Facebook Video URL:", key="fb")
        col_fb1, col_fb2 = st.columns(2)
        with col_fb1:
            if st.button("Download SD Quality"):
                st.info("Downloading Facebook SD...")
        with col_fb2:
            if st.button("Download HD Quality"):
                st.info("Downloading Facebook HD...")

# --- PAGE 3: DP & THUMBNAILS ---
elif page == "DP & Thumbnails":
    st.title("🖼️ Profile & Thumbnail Hub")
    
    choice = st.radio("Select Type:", ["YouTube Thumbnail", "Instagram DP"])
    
    if choice == "YouTube Thumbnail":
        thumb_url = st.text_input("Paste YouTube Link for Thumbnail:")
        if thumb_url and "v=" in thumb_url:
            video_id = thumb_url.split("v=")[1].split("&")[0]
            resolutions = {
                "Max Quality": f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
                "High Quality": f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
                "Medium Quality": f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
            }
            
            sel_thumb = st.selectbox("Quality Chunein:", list(resolutions.keys()))
            st.image(resolutions[sel_thumb], caption=sel_thumb)
            st.markdown(f"[📥 Download Thumbnail]({resolutions[sel_thumb]})")

    elif choice == "Instagram DP":
        st.subheader("Instagram Profile Picture")
        insta_user = st.text_input("Enter Instagram Username:", placeholder="e.g. vivek_dev")
        if st.button("Fetch DP"):
            st.info("Private accounts ka DP fetch nahi ho sakta.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("👤 **Developer:** Vivek (BCA)")
st.sidebar.write("🎯 **Target:** TCS Ignite 2026")