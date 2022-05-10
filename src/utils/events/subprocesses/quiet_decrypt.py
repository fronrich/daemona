# quietly decrypts a file and then stores it's path and key

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

    # for each object in the array, if the used path exists, decrypt at used path

    # check that the current file hasn't been encrypted
    used_paths = ransom_json.keys()

    # if the file was already encrypted don't rencrypt it
    for used_path in used_paths:
        if abs_path == used_path:
            rans_obj = ransom_json[used_path]
            enc_path = rans_obj['enc_path']
            key = rans_obj['key']

            # read the encrypted file
            enc_file = open(enc_path, "r+")
            data = enc_file.read()
            enc_file.close()

            # decrypt
            fernet = Fernet(key)
            dec_data = fernet.decrypt(data.encode()).decode('utf-8')

            # write decrypted data to file
            file = open(used_path, "w")
            file.write(dec_data)
            file.close()

            # delete the current obj from the ransom dict
            ransom_json.pop(used_path)

            # rewrite the new json
            du.write_json(cache_dir, 'ransom.json', ransom_json)

            return 1
    
    # nothing was decrypted
    return -1

main()