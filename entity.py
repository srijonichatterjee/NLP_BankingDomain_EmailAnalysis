import spacy
import re

nlp= spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {}

    # Named entities from spaCy
    for ent in doc.ents:
        if ent.label_ == "DATE":
            entities["date"] = ent.text
        elif ent.label_ == "GPE": #Geo political entity/location
            entities["branch"] = ent.text
        elif ent.label_ == "MONEY":
            entities["amount"] = ent.text
        elif ent.label_ == "PERSON":
            entities["name"] = ent.text

    # Regex for account number
    acc_match = re.search(r'(account|a/c)[^\d]{0,10}(\d{8,})', text, re.IGNORECASE)
    if acc_match: 
     entities["account_number"] = acc_match.group(2)

    return entities

text = "₹5000 was deducted from my account, holder name: SRIJONI, A/C: 12345678 on 10th June at Kolkata branch."
print(extract_entities(text))