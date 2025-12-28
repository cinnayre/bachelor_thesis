from pathlib import Path
import util

def count_files_by_extension(path: str, extension: str) -> int:
    """
    Recursively counts all files with the given extension in the specified path.
    Example: count_files_by_extension("/repo", ".ts") -> 321
    """
    # For debugging purposes, print each file found
    count = 0
    for item in Path(path).rglob(f"*{extension}"):
        if item.is_file():
            print(item.name)
            print(item)
            count += 1
    return count
    return sum(1 for item in Path(path).rglob(f"*{extension}") if item.is_file())

def list_file_counts_for_extension_per_project(path: str, extension: str) -> list[int]:
    """
    Applies count_files_by_extension() to each project in the given path.
    Returns a list of counts, one entry per project.
    """
    # We use a lambda here to pass the 'extension' argument along with each project path.
    return util.apply_function_to_each_project(
        lambda project_path: count_files_by_extension(project_path, extension),
        path
    )
