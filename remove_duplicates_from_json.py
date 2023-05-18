import json

def remove_duplicates_from_json(file_path):
    try:
        with open(file_path, 'r+') as file:
            data = json.load(file)  # Load JSON data

            # Identify duplicate entries
            unique_data = []
            duplicates = set()
            for entry in data:
                entry_hash = hash(json.dumps(entry, sort_keys=True))
                if entry_hash not in duplicates:
                    unique_data.append(entry)
                    duplicates.add(entry_hash)

            # Write the unique entries back to the file
            file.seek(0)
            file.truncate()
            json.dump(unique_data, file, indent=4)

        print("Duplicates removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON data in '{file_path}'.")

# Example usage
file_path = 'data.json'
remove_duplicates_from_json(file_path)
