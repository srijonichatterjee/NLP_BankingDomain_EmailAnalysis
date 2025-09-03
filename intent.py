import spacy
from textblob import TextBlob
import re

def detect_intent(text):
    if "close my account" in text:
        return "Account Closure"
    elif "unauthorized" in text or "deduction" in text:
        return "Raise Complaint"
    elif "loan" in text:
        return "Loan Inquiry"
    else:
        return "General Inquiry"
    

text1 = "I want to close my account immediately."
# Output: "Account Closure"

text2 = "There was an unauthorized deduction of ₹5000."
# Output: "Raise Complaint"

text3 = "What are the requirements for a personal loan?"
# Output: "Loan Inquiry"

text4 = "Hi, I need help understanding my bank statement."
# Output: "General Inquiry"

if __name__ == "__main__":
 print(detect_intent(text1))
 print(detect_intent(text2))
 print(detect_intent(text3))
 print(detect_intent(text4))
