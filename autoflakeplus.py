# Author: Manish Puri

import subprocess
import os
import shutil
import filecmp

"""This program will remove any unused imports from files in specified directory and subdirectories."""

dir_src = os.getcwd()

"""This function makes a backup of python files before running autoflake"""


def navigate_and_copy(src):
    f = open("log_files_copy.txt", "w")
    for item in os.listdir(src):
        s = os.path.join(src, item)
        dst = s+".bak"
        if os.path.isdir(s):
            navigate_and_copy(s)
        elif s.endswith(".py"):
            f.write(os.path.abspath(s))
            f.write("\n")
            shutil.copy(s, dst)
    f.close()


"""This function runs autoflake on directories and subdirectories"""


def autoflake_run():
    try:
        subprocess.call(
            ['autoflake', '-i', '-r', '--remove-all-unused-imports', dir_src])

        print("Autoflake process was run on all subdirectories ")
    except:
        print('Path file error. Please make sure directory exists.')


"""This function does a cleanup of unnecessary backups"""


def file_compare(src):
    f = open("log_deleted_backups.txt", "w")
    for item in os.listdir(src):
        s = os.path.join(src, item)
        dst = s+".bak"
        if os.path.isdir(s):
            file_compare(s)
        elif s.endswith(".py"):
            if (filecmp.cmp(s, dst)) == True:
                f.write(os.path.abspath(s))
                f.write("\n")
                os.remove(dst)
    f.close()


navigate_and_copy(dir_src)
autoflake_run()
file_compare(dir_src)
