import streamlit as st
import requests
from googletrans import Translator

# --- CONFIGURATION ---
st.set_page_config(page_title="Vivek| Multi-Lingual Dictionary", page_icon="📖", layout="wide")
translator = Translator()

def get_english_data(word):
    """Fetches comprehensive dictionary data from Free Dictionary API."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    return None

def translate_to_hindi(text):
    """Translates English text to Hindi."""
    try:
        translation = translator.translate(text, dest='hi')
        return translation.text
    except:
        return "अनुवाद उपलब्ध नहीं है"

# --- UI HEADER ---
st.title("📖 Vivek Dictionary")
st.markdown("### Professional English-Hindi Lexicon & Sentence Builder")
st.info("Enter a word below to get definitions, synonyms, antonyms, and usage examples.")

# --- SEARCH BAR ---
word_input = st.text_input("Enter Word:", placeholder="e.g., Resilience").strip()

if word_input:
    data = get_english_data(word_input)
    
    if data:
        # Layout Columns
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader(f"🔤 Word: {data['word'].capitalize()}")
            if 'phonetic' in data:
                st.write(f"🔊 Phonetic: {data.get('phonetic', '')}")
            
            # Meanings & Definitions
            for meaning in data['meanings']:
                part_of_speech = meaning['partOfSpeech']
                st.markdown(f"**Part of Speech:** *{part_of_speech}*")
                
                definition = meaning['definitions'][0]['definition']
                st.success(f"**English Definition:** {definition}")
                
                # Hindi Translation
                hindi_def = translate_to_hindi(definition)
                st.warning(f"**हिंदी परिभाषा:** {hindi_def}")
                st.divider()

        with col2:
            # Synonyms & Antonyms
            st.subheader("🔗 Relations & Context")
            
            syns = []
            ants = []
            for meaning in data['meanings']:
                syns.extend(meaning.get('synonyms', []))
                ants.extend(meaning.get('antonyms', []))
            
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Synonyms (समानार्थी):**")
                st.write(", ".join(syns[:5]) if syns else "None found")
            with c2:
                st.write("**Antonyms (विलोम):**")
                st.write(", ".join(ants[:5]) if ants else "None found")

            # Sentence Maker
            st.subheader("📝 Sentence Builder")
            examples = []
            for meaning in data['meanings']:
                for d in meaning['definitions']:
                    if 'example' in d:
                        examples.append(d['example'])
            
            if examples:
                for i, ex in enumerate(examples[:3]):
                    st.write(f"{i+1}. {ex}")
                    st.caption(f"🇮🇳 {translate_to_hindi(ex)}")
            else:
                st.write("Generating AI context...")
                # Fallback: simple sentence construction
                fallback_sentence = f"The word '{word_input}' is very important in professional communication."
                st.write(f"1. {fallback_sentence}")
                st.caption(f"🇮🇳 {translate_to_hindi(fallback_sentence)}")

    else:
        st.error("Word not found. Please check the spelling.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("Developed for Professional Lexicography")