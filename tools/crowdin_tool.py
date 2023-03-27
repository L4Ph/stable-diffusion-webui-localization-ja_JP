import os
import json
from tqdm import tqdm
from crowdin_api import CrowdinClient

# setup variables
project_token = os.environ['crowdin_api_token']
project_id = 552413
dirs = {
    'stablediffusion': 345,
    'extension': 347
}

# function to get file progress and print to markdown strings
def get_crowdin_progress(client, project_id, file_id):
    file_progress = client.translation_status.get_file_progress(
        projectId=project_id, fileId=file_id)['data'][0]['data']['translationProgress']
    return file_progress

def get_extension_url(file_name, file_path):
    if file_name == 'StableDiffusion':
        return 'https://github.com/AUTOMATIC1111/stable-diffusion-webui'
    elif file_name == 'ExtensionList':
        return 'https://raw.githubusercontent.com/wiki/AUTOMATIC1111/stable-diffusion-webui/Extensions-index.md'

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for key in data.keys():
                if '.git' in key:
                    return key.replace('.git', '')

    print(f"url not found at '{file_path}'")
    return ''

client = CrowdinClient(token=project_token)

# fetch all crowdin source files
file_scope = {}
for name, dir_id in dirs.items():
    files = client.source_files.with_fetch_all().list_files(
        projectId=project_id, directoryId=dir_id)['data']
    file_scope[name] = files

# generate progress markdown strings
progress_list = []
for name, files in file_scope.items():
    progress_list.append(f"\n<details>\n<summary>{name.capitalize()} ローカライズの進捗</summary>\n\n")
    for filedata in tqdm(files, desc=f"Requesting {name} files: "):
        file_id = filedata['data']['id']
        file_name = filedata['data']['name'].replace('.json', '')
        file_path = filedata['data']['path'].replace('/main/', './')
        file_progress = get_crowdin_progress(client, project_id, file_id)
        check_box = '[ ]' if file_progress < 100 else '[x]'
        extension_url = get_extension_url(file_name, file_path)
        progress_list.append(f"- {check_box} ![{file_name} translated {file_progress}%](https://geps.dev/progress/{file_progress}?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [{file_name}]({extension_url})")
    progress_list.append('</details>\n\n')

# update README.md with new progress markdown strings
with open('./README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

start_index = readme_content.find('## ローカライズの進捗')
end_index = readme_content.find('## Special Thanks!✨')
top_content = readme_content[0:start_index]
bottom_content = readme_content[end_index:len(readme_content)]
new_content = top_content + ''.join(progress_list) + bottom_content

with open('./README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)
