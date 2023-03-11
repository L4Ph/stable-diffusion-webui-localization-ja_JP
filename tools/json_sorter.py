import os
import json
import sys

# This script reads a JSON file, sorts the keys alphabetically, and writes the sorted data to
# a new JSON file with a '_sorted' suffix in the filename.

def test_sorted_json_file(original_file_path, sorted_file_path):
    """
    Tests that the sorted JSON file contains the same data as the original JSON file.

    Args:
        original_file_path (str): The path to the original JSON file.
        sorted_file_path (str): The path to the sorted JSON file.
    """
    # Load the original JSON data
    with open(original_file_path, encoding='utf-8') as f:
        original_data = json.load(f)

    # Load the sorted JSON data
    with open(sorted_file_path, encoding='utf-8') as f:
        sorted_data = json.load(f)

    # Sort the keys of the original JSON data
    sorted_original_data = json.loads(json.dumps(original_data, sort_keys=True))

    # Compare the sorted original data with the sorted data from the file
    assert sorted_original_data == sorted_data

def sort_json_file(input_file_path):
    """
    Sorts the key-value pairs in a JSON file alphabetically by key and writes the sorted data
    to a new JSON file with a '_sorted' suffix in the filename.

    Args:
        input_file_path (str): The path to the input JSON file.
    """
    try:
        # Check if the input file exists
        if not os.path.exists(input_file_path):
            raise FileNotFoundError(f"File '{input_file_path}' not found.")

        with open(input_file_path, encoding='utf-8') as input_file:
            # Load the JSON data from the input file
            main_data = json.load(input_file)
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{input_file_path}' contains invalid JSON data.")
        return

    # Create a new output file path by adding a '_sorted' suffix to the input file path
    output_file_path = os.path.splitext(input_file_path)[0] + '_sorted.json'
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Write the sorted data to the output file as JSON with sorted keys
            json.dump(main_data, output_file, ensure_ascii=False, indent=4, sort_keys=True)
    except OSError as e:
        print(f"Error: Could not write to file '{output_file_path}': {str(e)}")

    # Test that the sorted JSON file contains the same data as the original JSON file
    test_sorted_json_file(input_file_path, output_file_path)


if __name__ == '__main__':
    # Check that the user has provided an input file path as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python sort_json.py <input_file_path>")
    else:
        # Call the sort_json_file function with the input file path
        input_file_path = sys.argv[1]
        sort_json_file(input_file_path)
