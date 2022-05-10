# forgets all the ransom codes meaning your files are lost forever :)
# fmt: off
import sys
import os

sys.path.append(os.getcwd())
from src.utils.DirUtils import DirUtils
# fmt: on

def main():
    du = DirUtils()
    cache_dir = du.get_cache_dir()
    # rewrite the new json
    du.write_json(cache_dir, 'ransom.json', {})

main()

