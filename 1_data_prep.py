import csv
import json

file_path = "Mental_Health_FAQ.csv"

def load_knowledge_base(file_path: str) -> dict:
    data = {}
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                key = row[0]  # Assuming the first column contains the keys
                value = row[1]  # Assuming the second column contains the values
                data[key] = value
        return data
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist or is empty

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Example usage:
knowledge_base = load_knowledge_base(file_path)

# Modify knowledge_base as needed...

save_knowledge_base(file_path.replace(".csv", ".json"), knowledge_base)  # Saving as JSON for consistency
