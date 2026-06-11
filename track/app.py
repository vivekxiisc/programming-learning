import streamlit as st
from streamlit_js_eval import get_geolocation
import pandas as pd

st.set_page_config(page_title="Vivek's Geo-Tracker", page_icon="📍")

st.title("📍 Real-Time Location Tracker")
st.write("Is app ki madad se aap apni ya kisi ki live location coordinates nikal sakte hain.")

# Professional Info Box
st.info("Note: Location access ke liye browser mein 'Allow' par click karna zaroori hai.")

# Button to trigger location fetching
if st.button("Get My Live Location"):
    with st.spinner("Fetching GPS coordinates..."):
        location = get_geolocation()
        
        if location:
            # Data extract karna
            lat = location['coords']['latitude']
            lon = location['coords']['longitude']
            accuracy = location['coords']['accuracy']
            
            st.success("Location successfully fetched!")
            
            # Displaying Coordinates in a professional card
            col1, col2, col3 = st.columns(3)
            col1.metric("Latitude", f"{lat:.4f}")
            col2.metric("Longitude", f"{lon:.4f}")
            col3.metric("Accuracy", f"{accuracy} meters")
            
            # --- Visual Map ---
            st.subheader("🗺️ Your Location on Map")
            map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(map_data)
            
            # Sharing Link (Google Maps par dekhne ke liye)
            google_maps_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            st.markdown(f"🔗 [View on Google Maps]({google_maps_link})")
            
        else:
            st.error("Location access denied ya browser ne allow nahi kiya.")

# --- Professional Footer ---
st.sidebar.markdown("---")
st.sidebar.write("👤 **Developer:** Vivek (BCA)")
st.sidebar.write("🛡️ **Privacy:** Yeh app sirf wahi location dikhata hai jise user 'Allow' karta hai.")