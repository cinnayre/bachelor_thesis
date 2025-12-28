from pathlib import Path
import subprocess
import ast
import pandas as pd
from itertools import product

folders_nirjas = ["/frontend", "/src", "/test/controller", "/test/rest"]
# language
file_types_nirjas = { 
    ".ts": "TypeScript",
    ".js": "JavaScript"
}
# comment metric
attribute_nirjas = ["file_count", "total_lines", "sloc", "total_lines_of_comments", "blank_lines"]

def extract_metadata(res: dict):
    if not isinstance(res, dict):
        print("expected dict but got", type(res).__name__, "- indicates multiple instead of one file")
        print("the path is:", path)
        return
    
    # find metrics we care about
    mlc = len(res["multi_line_comment"]) # error
    total_lines = res["metadata"]["total_lines"]
    sloc = res["metadata"]["sloc"] + mlc # fix error
    locc = res["metadata"]["total_lines_of_comments"] - mlc # fix error
    blank_lines = res["metadata"]["blank_lines"]

    # return result
    return total_lines, sloc, locc, blank_lines

def update_metrics_row(df: pd.DataFrame, folder: str, lang_key: str, metadata: dict) -> None:
    """Update a one-row DataFrame with extracted metrics for a given folder + language."""
    total_lines, sloc, locc, blank_lines = extract_metadata(metadata)
    prefix = f"{folder} {lang_key}"

    df.at[0, f"{prefix} file_count"] += 1
    df.at[0, f"{prefix} total_lines"] += total_lines
    df.at[0, f"{prefix} sloc"] += sloc
    df.at[0, f"{prefix} total_lines_of_comments"] += locc
    df.at[0, f"{prefix} blank_lines"] += blank_lines

def append_repo_metrics(repo_path: str) -> pd.DataFrame:
    """Analyze repo folders with nirjas and return a one-row DataFrame of aggregated metrics."""
    # initialize one-row DataFrame with zeros
    columns = [
        f"{folder} {ftype} {attr}"
        for folder, ftype, attr in product(folders_nirjas, file_types_nirjas.keys(), attribute_nirjas)
    ]
    df = pd.DataFrame(0, index=[0], columns=columns)

    for folder in folders_nirjas: # dimension folders 3x
        result = subprocess.run(
            ["nirjas", repo_path + folder],
            capture_output=True,
            text=True,
            check=True,
        )
        files = ast.literal_eval(result.stdout)

        # filter for language (2x) and update row with metrics (5x)
        for file_dict in files: 
            lang = file_dict["metadata"]["lang"]
            for key, label in file_types_nirjas.items():
                if lang == label:
                    update_metrics_row(df, folder, key, file_dict)

    return df

def apply_nirjas_metrics_to_each_project(term_path: str) -> pd.DataFrame:
    """Apply metrics to all projects in a given term and return DataFrame with one row per project."""
    project_dfs = []

    print(f"Term: {term_path}")
    print(f"Started at: {pd.Timestamp.now()}")
    for project in Path(term_path).iterdir():
        if project.is_dir():
            project_df = append_repo_metrics(str(project))  # return one-row DataFrame
            project_dfs.append(project_df)

    # Concatenate all projects from a term into one big DataFrame
    if project_dfs:
        print(f"Term: {term_path}")
        print(f"Finished at: {pd.Timestamp.now()}")  
        return pd.concat(project_dfs, ignore_index=True)
    print("no projects found in", term_path)
    return pd.DataFrame()  # empty if no projects