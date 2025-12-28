from pathlib import Path
import util

# Only one level down
def count_files_in_directory(path: str) -> int:
    return sum(1 for item in Path(path).iterdir() if item.is_file())

# Counts also in subfolders
def count_all_files_recursively(path: str) -> int:
    total = count_files_in_directory(path)
    for item in Path(path).iterdir():
        if item.is_dir():
            total += count_all_files_recursively(item)
    return total

# Counts all files per folder (project in this case)
def list_file_counts_per_project(path: str) -> list[int]:
    return util.apply_function_to_each_project(count_all_files_recursively, path) 
