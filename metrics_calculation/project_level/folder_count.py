from pathlib import Path
import util

# In this case the projects in directory (one level down)
def count_direct_subfolders(path: str) -> int:
    return sum(1 for item in Path(path).iterdir() if item.is_dir())

# Counts all files in the given directory and its subdirectories
def count_all_nested_folders(path: str) -> int:
    total = count_direct_subfolders(path)
    for item in Path(path).iterdir():
        if item.is_dir():
            total += count_all_nested_folders(item)
    return total

# Counts all subfolder per folder (project in this case)
def list_nested_folder_counts_per_project(path: str) -> list[int]:
    return util.apply_function_to_each_project(count_all_nested_folders, path) 

