import os
import json
import sys

def merge_json_files(base_json_path, new_json_dir_path, output_json_path):
    """
    Merges the contents of a base JSON file with the contents of multiple new JSON files,
    writing the result to an output JSON file.

    Args:
        base_json_path (str): The path to the base JSON file.
        new_json_dir_path (str): The path to the directory containing the new JSON files.
        output_json_path (str): The path to the output JSON file.
    """
    try:
        # Load the base JSON data
        with open(base_json_path, encoding='utf-8') as f:
            base_data = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{base_json_path}' contains invalid JSON data.")
        return

    # Merge the new JSON data with the base data
    new_data = {}
    for filename in os.listdir(new_json_dir_path):
        file_path = os.path.join(new_json_dir_path, filename)
        try:
            with open(file_path, encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    if key not in base_data:
                        new_data[key] = value
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' contains invalid JSON data.")
            return

    merged_data = {**base_data, **new_data}

    # Write the merged data to the output file
    try:
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=4, sort_keys=True)
    except OSError as e:
        print(f"Error: Could not write to file '{output_json_path}': {str(e)}")

if __name__ == '__main__':
    # Check that the user has provided input and output file paths as command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python merge_json_files.py <base_json_path> <new_json_dir_path> <output_json_path>")
    else:
        # Call the merge_json_files function with the provided paths
        base_json_path = sys.argv[1]
        new_json_dir_path = sys.argv[2]
        output_json_path = sys.argv[3]
        merge_json_files(base_json_path, new_json_dir_path, output_json_path)
