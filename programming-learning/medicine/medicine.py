import wikipediaapi

def get_medicine_info(name):
    # Wikipedia API setup (Language English)
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent="MedicalApp/1.0 (contact: vivek@example.com)"
    )
    
    # Medicine search
    page = wiki.page(name)
    
    if page.exists():
        # Pehle 600 characters as 'Uses' nikalna
        summary = page.summary[:600] + "..."
        return {
            "title": page.title,
            "uses": summary,
            "url": page.fullurl
        }
    return None