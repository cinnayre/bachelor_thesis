
from lizard import analyze_file
from pathlib import Path
import pandas as pd
import util

extensions = {"ts", "tsx", "js", "jsx", "css", "scss", "html", "htm", "xml", "json"} # zip?
folders_nirjas = ["\\frontend", "\\src", "\\test\\controller", "\\test\\rest"]

core = {"ts", "tsx", "js", "jsx"}

# Lizard based CC calculation
def calculate_cc_of_file(file_path: str, debug_print: bool =False) -> int:
    result = analyze_file(file_path)
    # print(result)
    sum_result = sum(f.cyclomatic_complexity for f in result.function_list)
    
    # delete debug later
    if debug_print and '.' in file_path and sum_result > 0:
        file_ext = file_path.split('.')[-1]
        if file_ext not in core:
                print(f"File: {file_path}, CC: {sum_result}")
            


    # if debug_print and result.function_list:
    #     print("Available Infos:", result.function_list[0].__dict__)
    #     for func in result.function_list:
    #         print(func.name, func.cyclomatic_complexity)
    #     print("Project total:", sum_result)
    return sum_result

def is_relevant_file(file) -> bool:
    f = str(file)
    if '.' in f:
        file_ext = f.split('.')[-1] 
        return file_ext in extensions
    return False

# very restrictive, but congruent with nirjas
def is_relevant_folder(file) -> bool: 
    f = str(file)
    for folder in folders_nirjas:
        if folder in f:
            return True
    return False

def calculate_cc_of_project(project_path: str) -> int:
    print(f"Calculating CC for project: {project_path}")
    start = pd.Timestamp.now()
    print(f"Started at {pd.Timestamp.now()}")
    total_cc = 0
    for file in Path(project_path).rglob("*"):
        
        if file.is_file() and is_relevant_file(file) and is_relevant_folder(file):
            try:
                # print(f"At: {pd.Timestamp.now()}")
                # print(f"{file}")
                cc_file = calculate_cc_of_file(str(file), False)
                total_cc += cc_file
                # print(f"CC of it: {cc_file}, new total: {total_cc}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")
                continue
    print(f"Finished at {pd.Timestamp.now()}, took {pd.Timestamp.now() - start}")
    print(f"Total CC for project {project_path}: {total_cc}")
    return total_cc

# takes some time - 2h?
def list_cc_per_project(term_path: str) -> list[int]:
    return util.apply_function_to_each_project(calculate_cc_of_project, term_path)

def count_and_list_irrelevant_files(project_path: str) -> tuple[dict[str, int], list[str]]:
    file_counts = {}
    file_list = []

    for file in Path(project_path).rglob("*"):
        if file.is_file() and (is_relevant_folder(file) and  is_relevant_file(file)):
            ext = file.suffix.lstrip(".").lower() or "no_ext"
            if ext == "no_ext" and 'gitignore' not in str(file) and 'gitkeep' not in str(file):
                print(f"File without extension: {file}")
            file_counts[ext] = file_counts.get(ext, 0) + 1
            file_list.append(str(file))

    # print("\nList of irrelevant files:")
    # for f in file_list:
    #     print(f)
    
    # print("Irrelevant files by extension:")
    # for ext, count in file_counts.items():
    #     print(f".{ext}: {count}")

    return file_counts, file_list


def list_irrelevant_files_per_project(term_path: str) -> list[tuple[dict[str, int], list[str]]]:
    """Apply irrelevant file counting to each project in the given term and print term totals."""
    results = util.apply_function_to_each_project(count_and_list_irrelevant_files, term_path)

    total_counts = {}
    for file_counts, _ in results:
        for ext, count in file_counts.items():
            total_counts[ext] = total_counts.get(ext, 0) + count

    print(f"In term '{term_path}' a total of:")
    for ext, count in total_counts.items():
        prefix = "" if ext.startswith(".") else "."
        print(f" {prefix}{ext}: {count}")

    return results

