from pathlib import Path
import util

# not very efficient, could be improved (not needed when only run once)

def count_lines_of_code(path: str) -> int:
    """
    Recursively counts all lines of code in all files under the given path.
    Binary files and unreadable files are skipped.
    """
    total_lines = 0
    for file in Path(path).rglob("*"):
        if file.is_file():
            try:
                with file.open("r", encoding="utf-8", errors="ignore") as f:
                    total_lines += sum(1 for _ in f)
            except (OSError, UnicodeDecodeError):
                continue
    return total_lines


def list_lines_of_code_per_project(path: str) -> list[int]:
    """
    Returns a list with the LoC count for each project directory inside `path`.
    """
    return util.apply_function_to_each_project(count_lines_of_code, path)


def count_lines_of_code_by_extension(path: str, extension: str) -> int:
    """
    Recursively counts LoC only in files matching the given extension.
    """
    total_lines = 0
    for file in Path(path).rglob(f"*{extension}"):
        if file.is_file():
            try:
                with file.open("r", encoding="utf-8", errors="ignore") as f:
                    total_lines += sum(1 for _ in f)
            except (OSError, UnicodeDecodeError):
                continue
    return total_lines


def list_loc_by_extension_per_project(path: str, extension: str) -> list[int]:
    """
    Returns a list with LoC count for the given extension for each project in `path`.
    """
    # We use a lambda here to pass the 'extension' argument along with each project path.
    return util.apply_function_to_each_project(
        lambda project_path: count_lines_of_code_by_extension(project_path, extension), path
    )