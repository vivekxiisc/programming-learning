import streamlit as st

st.title("🏛️ Group A: Architectural Icons & Monuments")
st.caption("Displaying database ledger records 01 through 10.")
st.markdown("---")

articles_a = [
    ("01. Taj Mahal (Agra)", "A global symbol of immense love, this white ivory-marble mausoleum is widely celebrated as one of the Seven Wonders of the World."),
    ("02. Qutub Minar (Delhi)", "The tallest brick minaret in existence worldwide, showcasing intricate ancient Indo-Islamic engineering footprints."),
    ("03. Gateway of India (Mumbai)", "Erected to commemorate the landing of King George V, it stands proud overlooking the vast Arabian Sea."),
    ("04. Red Fort (Delhi)", "The historic seat of power for the Mughal dynasty, where India's Prime Minister hoist the tricolor flag every Independence Day."),
    ("05. Hawa Mahal (Jaipur)", "The high-walled 'Palace of Winds' configured with 953 small casements designed for royal winds to cascade freely."),
    ("06. Ajanta & Ellora Caves (Maharashtra)", "Monolithic rock-cut temple structures featuring legendary ancient Buddhist, Hindu, and Jain frescoes."),
    ("07. Golden Temple (Amritsar)", "Sri Harmandir Sahib, the central spiritual sanctum of Sikhism, famous for its pure gold architecture and mega open kitchens."),
    ("08. Konark Sun Temple (Odisha)", "Conceived as a colossal cosmic chariot with intricately carved stone wheels, dedicated entirely to the Sun God."),
    ("09. Mysore Palace (Karnataka)", "An outstandingly grand royal residency known globally for its breathtaking aesthetic lighting displays during festivals."),
    ("10. Victoria Memorial (Kolkata)", "A grand white marble palace dedicated to Queen Victoria, displaying a fusion of British Revivalist and Mughal styles.")
]

for title, desc in articles_a:
    st.markdown(f"""
    <div class="article-card">
        <h3 class="article-title">{title}</h3>
        <p class="article-text">{desc}</p>
    </div>
    """, unsafe_allow_html=True)