import os, sys, shutil

def clear_dir(directory):
    abs_filepath = os.path.abspath(directory)
    files = os.listdir(abs_filepath)
    if len(files) == 0:
        return
    for file in files:
        new_filepath = os.path.join(abs_filepath, file)
        try:
            if os.path.isfile(new_filepath):
                os.remove(new_filepath)
            else:
                clear_dir(new_filepath)
                os.rmdir(new_filepath)
        except:
            raise Exception (f"Error in deleting file {new_filepath}")

def copy_dir(source, target):
    copied_files = []
    abs_source = os.path.abspath(source)
    abs_target = os.path.abspath(target)
    files = os.listdir(abs_source)
    if len(files) == 0:
        return
    for file in files:
        new_filepath = os.path.join(abs_source, file)
        try:
            if os.path.isfile(new_filepath):
                shutil.copy(new_filepath, abs_target)
                copied_files.append(new_filepath)
            else:
                os.mkdir(os.path.join(abs_target, file))
                copy_dir(new_filepath, os.path.join(abs_target, file))
        except:
            raise Exception (f"Error in copying file {new_filepath}")
    return copied_files
