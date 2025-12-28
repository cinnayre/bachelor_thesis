from pathlib import Path
from itertools import chain
from metrics_calculation import (
    file_extension_count,
    loc_count,
    locc_count,
)

TERM_1_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1" # 21T1
TERM_2_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T2" # 21T2
TERM_3_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2023W-T2" # 23T2
TERM_4_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2024W-T1" # 24T1

term_paths = [TERM_1_PATH, TERM_2_PATH, TERM_3_PATH, TERM_4_PATH]

def concat_results(foo: callable, paths: list[str]=term_paths) -> list:
    """
    Applies foo to each element in paths and concatenates the resulting lists.

    Args:
        foo (callable): A function that takes one argument and returns a list.
        paths (list): Iterable of arguments to pass to foo.

    Returns:
        list: Concatenated results from foo for all paths.
    """
    return list(chain.from_iterable(map(foo, paths)))

# function to apply method to each project in term
# Maybe modify with *arg and **kwargs to pass additional arguments instead of lambda
def apply_function_to_each_project(foo, term_path):
    return [foo(folder) for folder in Path(term_path).iterdir() if folder.is_dir()]

# Aggregate functions for metrics with file extensions
def aggregate_file_counts_by_extension(extension: str) -> list[int]:
    return concat_results(
        lambda path: file_extension_count.list_file_counts_for_extension_per_project(path, extension)
    )

def aggregate_loc_counts_by_extension(extension: str) -> list[int]:
    return concat_results(
        lambda path: loc_count.list_loc_by_extension_per_project(path, extension)
    )

def aggregate_locc_counts_by_extension(extension: str) -> list[int]:
    return concat_results(
        lambda path: locc_count.list_locc_by_extension_per_project(path, extension)
    )