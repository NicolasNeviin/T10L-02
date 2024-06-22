import json
import os

# Assuming quiz_data.json is in the same directory as this script
file_path = os.path.join(os.path.dirname("C:/Mini It Project/Project/Test/quiz_data.json"), 'quiz_data.json')

try:
    with open(file_path, 'r') as file:
        quiz_data = json.load(file)
    print(quiz_data)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except json.JSONDecodeError:
    print("Failed to decode JSON file.")

