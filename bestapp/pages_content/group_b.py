import streamlit as st

st.title("🏞️ Group B: Bio-Diversity & Spiritual Wonders")
st.caption("Displaying database ledger records 11 through 20.")
st.markdown("---")

articles_b = [
    ("11. Varanasi Spiritual Ghats (UP)", "One of the oldest continually inhabited metropolitan points on Earth, famous for riverfront evening ceremonies."),
    ("12. Sundarbans Mangrove Ecosystem", "The world's largest single block of tidal halophytic mangrove forest, serving as the premium sanctuary for Royal Bengal Tigers."),
    ("13. Backwaters of Kerala", "A magnificent labyrinthine chain of brackish lagoons and lakes running parallel to the Arabian Sea coast, famous for houseboats."),
    ("14. Valley of Flowers (Uttarakhand)", "A stunning high-altitude Himalayan valley renowned for its carpets of rare alpine flowers and endangered wildlife species."),
    ("15. Thar Desert Sand Dunes (Jaisalmer)", "The golden sandy heartland of Rajasthan, boasting vibrant nomadic culture, camel safaris, and pristine forts."),
    ("16. The Western Ghats Mountain Range", "An ancient mountain range older than the Himalayas, formally recognized as a global biological diversity super-hotspot."),
    ("17. Khajuraho Temples (MP)", "Celebrated worldwide for their unique Nagara-style architectural symmetry and expressive, highly detailed stone sculptures."),
    ("18. Great Rann of Kutch (Gujarat)", "One of the largest salt deserts in the world, morphing into a surreal, hyper-reflective white expanse on full moon nights."),
    ("19. Meenakshi Temple (Madurai)", "A historic masterpiece of Dravidian architecture, featuring massive multi-colored gateway towers covered in thousands of icons."),
    ("20. Kaziranga Biosphere (Assam)", "A dense wildlife sanctuary housing two-thirds of the entire global population of the prehistoric Great Indian One-Horned Rhinoceros.")
]

for title, desc in articles_b:
    st.markdown(f"""
    <div class="article-card">
        <h3 class="article-title">{title}</h3>
        <p class="article-text">{desc}</p>
    </div>
    """, unsafe_allow_html=True)