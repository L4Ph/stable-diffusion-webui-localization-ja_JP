import json
import os
import glob
from collections import defaultdict

TEMPLATE_FOLDER = './template'
LOCALIZATIONS_FOLDER = './localizations'
REPORT_FILE = os.path.join(os.getcwd(), 'tools', 'report', 'report.txt')


def merge_json_files(lang_folder):
    # Get all JSON files in the folder
    json_files = glob.glob(os.path.join(lang_folder, '*.json'))
    extensions_folder = os.path.join(lang_folder, 'extensions')
    if os.path.exists(extensions_folder):
        json_files += glob.glob(os.path.join(extensions_folder, '*.json'))

    # Put StableDiffusion.json as the first element in the list
    stable_diffusion_file = os.path.join(lang_folder, 'StableDiffusion.json')
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
    lang_code = os.path.basename(lang_folder)
    merged_file = os.path.join('localizations', f'{lang_code}.json')
    with open(merged_file, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=4)

    # Write report file
    report_file = os.path.join('tools', 'report', f'report-{lang_code}.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
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



def merge_all_languages():
    # Create localizations folder if it does not exist
    if not os.path.exists(LOCALIZATIONS_FOLDER):
        os.mkdir(LOCALIZATIONS_FOLDER)

    # Merge all languages
    for lang_folder in glob.glob(os.path.join(TEMPLATE_FOLDER, '*_*')):
        merge_json_files(lang_folder)


if __name__ == '__main__':
    merge_all_languages()
