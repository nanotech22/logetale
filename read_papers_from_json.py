import json
from arx3 import *


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()

            if not contents.strip():
                print("The JSON file is empty.")
            else:
                try:
                    data = json.loads(contents)
                    if isinstance(data, list):  # Check if data is a JSON array
                        for entry in data:
                            #print("entry in data")
                            paper_json = Paper.from_json(entry)
                            paper_json.display_info()
                    elif isinstance(data, dict):  # Check if data is a single JSON object
                        #print("entry in dict")
                        #print(data)
                        paper_json = Paper.from_json(data)
                    else:
                        print("Invalid JSON format.")
                except json.JSONDecodeError:
                    print(f"Error decoding JSON data in '{file_path}'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Example usage
file_path = 'data.json'
read_json_file(file_path)