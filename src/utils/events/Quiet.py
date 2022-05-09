# event utils for dong quiet file operations
# all python subprocesses will use cwd as their cwd
from src.utils.DirUtils import DirUtils
import subprocess
import os


def quiet_run(process, loc_args):
    du = DirUtils()
    CWD = du.get_work_dir()
    subprocess_dir = du.get_subprocesses_dir()
    cmd_path = os.path.join(
        subprocess_dir, 'quiet_' + str(process)) + '.py'

    cmd = ['python3', cmd_path] + list(loc_args)
    print(cmd)

    ret = subprocess.Popen(cmd, cwd=(CWD))

    return ret
