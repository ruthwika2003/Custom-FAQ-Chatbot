import json
from difflib import get_close_matches

# Load the knowledge base
def load_knowledge_base(C:\Users\ruthw\Downloads\Mental_Health_FAQ.csv: str) -> dict:
  with open(C:\Users\ruthw\Downloads\Mental_Health_FAQ.csv, 'r') as file:
    data: dict = json.load(file)
  return data


def save_knowledge_base(C:\Users\ruthw\Downloads\Mental_Health_FAQ.csv: str, data: dict):
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=2)
