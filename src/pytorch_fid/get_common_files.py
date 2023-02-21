# get files from folder A that matches the name with the file from folder B
# return the list of files in folder A that matches the name with the file from folder B
import os
import shutil
def get_common_files(folder_A, folder_B, folder_A_new):
    files_A = os.listdir(folder_A)
    files_B = os.listdir(folder_B)
    common_files = []
    for file_A in files_A:
        if file_A in files_B:
            common_files.append(file_A)
    # copy the files from folder A to an a new folder
    for file in common_files:
        shutil.copy(os.path.join(folder_A, file), os.path.join(folder_A_new, file))
    return common_files