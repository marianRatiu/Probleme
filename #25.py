# This week, we're going to start to work on a small application that detects whether files have been changed or otherwise tampered with. The aim here isn't to compete with such systems as Tripwire, but rather to work a bit with hashing, data storage, and reporting.
#
# This exercise will extend over several weeks. This week, we'll start the process by writing a program that collects information about files, and creates a data structure from that information.
#
# In other words: You should write a function, get_file_info, that takes a single argument, "pathname," the name of a directory. The program will then go through each of the files in that directory, as well as in any subdirectories, and will calculate the SHA-1 of that file.
#
# The program should then produce (and print) a data structure -- a list of dictionaries -- in which each dictionary will contain the following information:
# full path and filename
# file timestamp
# SHA-1 of the file's contents
# This exercise combines a number of different things:
# The use of os.walk to go through an entire directory/tree structure
# The use of os.stat to retrieve information about files
# The calculation of a hash function (SHA-1, in this case) on a file's contents


import os
import hashlib
from datetime import datetime


def get_file_info(pathname):
    file_data = []

    for root, dirs, files in os.walk(pathname):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                file_stat = os.stat(full_path)
                file_timestamp = datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

                sha1 = hashlib.sha1()
                with open(full_path, 'rb') as f:
                    while chunk := f.read(8192):
                        sha1.update(chunk)

                file_data.append({
                    'path_name': full_path,
                    'time': file_timestamp,
                    'SHA-1': sha1.hexdigest()
                })
            except Exception as e:
                print(f"Error processing file {full_path}: {e}")

    return file_data


pathname = 'test'
file_info_list = get_file_info(pathname)
for info in file_info_list:
    print(info)
