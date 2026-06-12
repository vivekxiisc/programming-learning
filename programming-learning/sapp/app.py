import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION ---
API_KEY = "AIzaSyAM1BhS4xPp5dnxi5g9uhMIpPChaPFPMMU"
# Force configuration to use stable settings
genai.configure(api_key=API_KEY)

# --- 2. FAIL-SAFE MODEL LOADING ---
@st.cache_resource
def load_stable_model():
    # 2026 mein 'gemini-1.5-flash' stable ho chuka hai, 
    # par agar 404 de raha hai toh hum backup models try karenge
    model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    
    for name in model_names:
        try:
            model = genai.GenerativeModel(name)
            # Chota sa check
            model.generate_content("test", generation_config={"max_output_tokens": 1})
            return model, name
        except Exception:
            continue
    return None, None

model, active_name = load_stable_model()

# --- 3. UI LAYOUT ---
st.set_page_config(page_title="Vivek's Medical AI", page_icon="🏥")

st.sidebar.title("👨‍💻 Project Info")
st.sidebar.markdown(f"**Developer:** Vivek\n**BCA Dept Project**")

if model:
    st.sidebar.success(f"✅ Active: {active_name}")
else:
    st.sidebar.error("❌ Connection Failed")

st.title("🏥 Smart AI Medical Assistant")

# --- 4. SEARCH LOGIC ---
if model is None:
    st.error("System Error: Google API is not responding to these model names.")
    st.info("Fix: Terminal mein 'pip install -U google-generativeai' run karke app restart karein.")
else:
    query = st.text_input("Dawai ya Symptoms puchiye:", placeholder="e.g. Omega 3 benefits")

    if st.button("Search AI"):
        if query:
            with st.spinner('Researching...'):
                try:
                    # Simple prompt for faster processing
                    prompt = f"Explain {query} in simple Hinglish with uses and side effects. Add a disclaimer."
                    response = model.generate_content(prompt)
                    
                    st.markdown("---")
                    st.subheader("📝 Result:")
                    st.write(response.text)
                except Exception as e:
                    # Agar quota limit (429) aaye toh user ko samjhao
                    if "429" in str(e):
                        st.warning("⚠️ Limit hit! Please wait 30 seconds and try again.")
                    else:
                        st.error(f"Error: {str(e)}")
        else:
            st.warning("Kuch toh likhiye!")

st.markdown("---")
st.caption("Developed by Vivek | BCA 2026")