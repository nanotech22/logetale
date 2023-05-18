import json
from arx3 import *
from remove_duplicates_from_json import *


#   
#
#   Just change this to the arxiv link of the newest paper to add it
#   And then run the file
#   Automatically removes duplicates
#
#
arxiv_link = "https://arxiv.org/abs/1908.04936"





def add_entry_to_json(file_path, entry):
    try:
        with open(file_path, 'r+') as file:
            contents = file.read()

            if not contents.strip():  # Check if the file is empty
                data = []
            else:
                data = json.loads(contents)  # Load existing JSON data

            data.append(entry)  # Append new entry

            file.seek(0)  # Reset file pointer to the beginning
            json.dump(data, file, indent=4)  # Write updated data back to the file

        print("Entry added successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON data in '{file_path}'.")

# Example usage
file_path = 'data.json'
# new_entry = {"name": "John", "age": 25, "city": "New York"}



paper = Paper(arxiv_link)
paper.extract_info()

# Convert the Paper object to JSON
paper_json = paper.to_json()
print(paper_json)
new_entry = paper_json


add_entry_to_json(file_path, new_entry)

#  Automatically removes duplicates
remove_duplicates_from_json(file_path)

