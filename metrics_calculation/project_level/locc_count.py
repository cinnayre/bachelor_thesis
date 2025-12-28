from pathlib import Path
import util

# not very efficient, could be improved (not needed when only run once)
# ts and js: //, /* (start or inline), * (start only) 
# strings and regex are edge cases, that are falsely counted
# html and css: <!--, 
# Tsx files?

def count_lines_of_comments(path: str) -> int:
    """
    Recursively counts all comment lines in all files under the given path.
    This is a very simple heuristic: 
    - For JS/TS/TSX/JSX, lines starting with // or /* or * are counted.
    - FUTURE: misses inline commens with // at the end of the line and multiline comments that don't start each line with *
    - For HTML/CSS, lines containing <!-- or */ are counted.
    """
    total_comments = 0
    for file in Path(path).rglob("*"):
        if file.is_file():
            try:
                with file.open("r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        stripped = line.strip()
                        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") \
                           or stripped.startswith("<!--") or stripped.startswith("*/"):
                            total_comments += 1
            except (OSError, UnicodeDecodeError):
                continue
    return total_comments


def list_lines_of_comments_per_project(path: str) -> list[int]:
    """
    Returns a list with the LoCc count for each project directory inside `path`.
    """
    return util.apply_function_to_each_project(count_lines_of_comments, path)


def count_lines_of_comments_by_extension(path: str, extension: str) -> int:
    """
    Recursively counts comment lines only in files matching the given extension.
    """
    total_comments = 0
    for file in Path(path).rglob(f"*{extension}"):
        if file.is_file():
            try:
                with file.open("r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        stripped = line.strip()
                        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") \
                           or stripped.startswith("<!--") or stripped.startswith("*/"):
                            total_comments += 1
            except (OSError, UnicodeDecodeError):
                continue
    return total_comments


def list_locc_by_extension_per_project(path: str, extension: str) -> list[int]:
    """
    Returns a list with LoCc count for the given extension for each project in `path`.
    """
        # We use a lambda here to pass the 'extension' argument along with each project path.
    return util.apply_function_to_each_project(
        lambda project_path: count_lines_of_comments_by_extension(project_path, extension), path
    )


# Correctness unclear
def count_comments_in_file(file_path: str) -> int:
    """
    Count the number of comment lines in a source file.

    Supports: .ts, .tsx, .js, .jsx, .html, .css, .scss
    Handles:
      - Line comments (`//`)
      - Block comments (`/* ... */`) (multi-line included)
      - HTML comments (`<!-- ... -->`) (multi-line included)

    Args:
        file_path (str): Path to the file

    Returns:
        int: Number of comment lines
    """
    ext = Path(file_path).suffix.lower()
    comment_lines = 0

    # Flags for multi-line comment modes
    in_block_comment = False
    in_html_comment = False

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            stripped = line.strip()

            # --- HTML comment handling ---
            if ext in {".html", ".htm", ".tsx", ".jsx"}:
                if not in_html_comment and ("<!--" in stripped):
                    in_html_comment = True
                    comment_lines += 1
                    if "-->" in stripped: # FIX: switch starts and end with contains
                        in_html_comment = False
                elif in_html_comment:
                    comment_lines += 1
                    if "-->" in stripped:
                        in_html_comment = False
                continue  # skip HTML lines (no JS parsing here)

            # --- Line comments (JS, TS, SCSS) ---
            if "//" in stripped and not in_block_comment:
                # crude heuristic: if `//` appears, treat as a comment line
                comment_lines += 1
                continue

            # --- Block comments (/* ... */) ---
            if "/*" in stripped and not in_block_comment:
                in_block_comment = True
                comment_lines += 1
                if "*/" in stripped:
                    in_block_comment = False
                continue
            elif in_block_comment:
                comment_lines += 1
                if "*/" in stripped:
                    in_block_comment = False
                continue

    return comment_lines

# does the same as locc_count_nirjas
def count_comments_in_directory(path: str, extensions=None) -> int:
    """
    Recursively count all comment lines in files under a directory.

    Args:
        path (str): Root directory
        extensions (set[str], optional): Which extensions to include.
                                         Defaults to common code files.

    Returns:
        int: Total comment lines across all files
    """
    if extensions is None:
        extensions = {".ts", ".tsx", ".js", ".jsx", ".html", ".css", ".scss"}

    total_comments = 0
    for file in Path(path).rglob("*"):
        if file.suffix.lower() in extensions and file.is_file():
            total_comments += count_comments_in_file(str(file))
    return total_comments
