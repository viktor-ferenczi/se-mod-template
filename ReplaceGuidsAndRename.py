""" Replaces project GUIDs and renames the solution

Tested on Python 3.12, should work on any recent 3.x

"""

import os
import re
import sys
import uuid

DRY_RUN = 1

PT_MOD_NAME = r'^([A-Z][a-z_0-9]+)+$'
RX_MOD_NAME = re.compile(PT_MOD_NAME)

TEMPLATE_NAME = 'ModTemplate'
TEMPLATE_NAME_WITH_SPACES = 'Mod Template'


def generate_guid():
    return str(uuid.uuid4())


def replace_text_in_file(replacements, path):
    is_project = path.endswith('.sln') or path.endswith('.csproj') or path.endswith('.shproj')
    encoding = 'utf-8-sig' if is_project else 'utf-8'

    with open(path, 'rt', encoding=encoding) as f:
        text = f.read()

    original = text

    for k, v in replacements.items():
        text = text.replace(k, v)

    if DRY_RUN or text == original:
        return

    with open(path, 'wt', encoding=encoding) as f:
        f.write(text)


def input_mod_name():
    while 1:
        mod_name = input('Name of the mod (in CapitalizedWords format): ')
        if not mod_name:
            break

        if RX_MOD_NAME.match(mod_name):
            break

        print('Invalid mod name, it must match regexp: ' + PT_MOD_NAME)

    return mod_name


def main():
    if not os.path.isfile(f'{TEMPLATE_NAME}.sln'):
        print('Run this script only once from the working copy (solution) folder')
        sys.exit(-1)

    mod_name = 'ModName' if DRY_RUN else input_mod_name()
    if not mod_name:
        return
    
    mod_name_with_spaces = re.compile('([A-Z])').subn(r' \1', mod_name)[0].lstrip()

    replacements = {
        TEMPLATE_NAME: mod_name,
        TEMPLATE_NAME_WITH_SPACES: mod_name_with_spaces,
        'FAE04EC0-301F-11D3-BF4B-00C04F79EFBC': generate_guid().upper(),
        'F7EA06E6-FC5B-4777-AF67-D3E8BB9D24D2': generate_guid().upper(),
    }
    
    def iter_paths():
        for dirpath, dirnames, filenames in os.walk('.'):
            if (
                    '\\.git' in dirpath or 
                    '\\.idea' in dirpath or 
                    '\\bin' in dirpath or 
                    '\\obj' in dirpath
            ):
                continue
            
            if not (dirpath == '.' or 
                    dirpath.startswith(f'.\\{TEMPLATE_NAME}')):
                continue
                
            for dirname in dirnames:
                if dirname == TEMPLATE_NAME:
                    yield os.path.join(dirpath, dirname)

            for filename in filenames:
                ext = filename.rsplit('.')[-1]
                if ext in ('sln', 'csproj', 'cs', 'bat', 'md', 'txt'):
                    yield os.path.join(dirpath, filename)

    paths = list(iter_paths())
    for path in paths:
        print(path)
                        
    for path in reversed(paths):
        dir_path, filename = os.path.split(path)
        if os.path.isfile(path):
            replace_text_in_file(replacements, path)
        if TEMPLATE_NAME in filename:
            if not DRY_RUN:
                os.rename(path, os.path.join(dir_path, filename.replace(TEMPLATE_NAME, mod_name))) 
        

if __name__ == '__main__':
    main()