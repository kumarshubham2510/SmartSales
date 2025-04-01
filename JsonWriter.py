import os
import json
from main import slides

def read_text_files_to_json(directory_path, json_file_path):
    # List to hold the contents of all the text files
    all_texts = [x for x in slides]

    # Check if the directory exists
    if not os.path.exists(directory_path):
        print("Directory does not exist.")
        return

    # Loop through the files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Only process text files (optional: you can adjust extensions)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                all_texts.append({"filename": filename, "content": file_content})

    # Write the collected texts into a JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(all_texts, json_file, ensure_ascii=False, indent=4)
        print(f"Texts from files have been saved to {json_file_path}")

# Example usage
directory_path = './JsonFilesforSlides'
json_file_path = 'output_texts.json'  # Replace with the desired output JSON file path

read_text_files_to_json(directory_path, json_file_path)