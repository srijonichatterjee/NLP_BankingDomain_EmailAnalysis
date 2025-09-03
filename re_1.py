#Regular Expression
import re

text = "The quick brown fox jumps over the lazy dog."
match = re.search(r"fox", text)
if match:
    print(f"Found: {match.group()}")

all_words = re.findall(r"\b\w+\b", text) # Find all words
print(all_words)