# symptom.py

# Yeh dictionary symptoms ke basis par medicine suggest karegi
symptom_map = {
    "fever": "Paracetamol, Ibuprofen",
    "headache": "Aspirin, Paracetamol",
    "cold": "Cetirizine, Loratadine",
    "cough": "Dextromethorphan, Honey-based syrup",
    "stomach pain": "Antacids, Meftal Spas",
    "body pain": "Diclofenac, Ibuprofen"
}

def get_suggestion(symptom):
    """Symptom ke basis par medicine suggest karne wala function"""
    if not symptom:
        return "Please enter a symptom."
        
    symptom = symptom.lower().strip()
    # Dictionary mein search karna, agar nahi mile toh default message dena
    return symptom_map.get(symptom, "Data not found. Please consult a professional doctor.")