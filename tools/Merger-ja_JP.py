import json
import os
import glob
from collections import defaultdict

JSON_FOLDER = './template/ja_JP'
EXTENSIONS_FOLDER = './template/ja_JP/extensions'
MERGED_FILE = './localizations/ja_JP.json'
REPORT_FILE = './tools/report/report-ja_JP.txt'


def merge_json_files():
    # Get all JSON files in the folder
    json_files = glob.glob(os.path.join(JSON_FOLDER, '*.json'))
    if os.path.exists(EXTENSIONS_FOLDER):
        json_files += glob.glob(os.path.join(EXTENSIONS_FOLDER, '*.json'))

    # Put StableDiffusion.json as the first element in the list
    stable_diffusion_file = './template/ja_JP/StableDiffusion.json'
    if stable_diffusion_file in json_files:
        json_files.remove(stable_diffusion_file)
        json_files.insert(0, stable_diffusion_file)

    # Merge all JSON files
    merged = defaultdict(dict)
    duplicate_keys = defaultdict(list)
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for key, value in data.items():
                if isinstance(value, dict):
                    # Key already exists, recursively merge subkeys
                    merged[key].update(value)
                elif key in merged:
                    # Key already exists, add to list of duplicate keys
                    duplicate_keys[key].append(file)
                else:
                    merged[key] = value

    # Write merged JSON file
    with open(MERGED_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=4)

    # Write report file
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        if len(duplicate_keys) > 0:
            f.write('重複したkeyがあります: \n')
            for key, files in duplicate_keys.items():
                f.write(f'\n"{key}"\n')
                for file in files:
                    # Get the value for the key in the file
                    with open(file, 'r', encoding='utf-8') as f2:
                        data = json.load(f2)
                        value = data.get(key)
                    # Write the value for the key in the file
                    f.write(f'"{file}" - "{value}".\n')
        else:
            f.write('重複したkeyはありません')


if __name__ == '__main__':
    merge_json_files()