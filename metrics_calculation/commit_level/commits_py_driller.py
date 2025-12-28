"""
Commit Processing Script.

This module provides functionality for analyzing and processing commits across
multiple academic terms. It can be executed directly or imported as part of a
larger analysis pipeline.

Each term represents a cohort of projects (repositories). Commit analysis is
computationally intensive and may require several hours per term, depending on
the number of commits analyzed.

Usage:
    Run from the project root directory:
        python commit_py_driller.py
"""

# imports
import os
import csv
import time

import pandas as pd
from pydriller import Repository

from helpers.project_config import TERM_PATHS, TERM_SIZES

"""
Term configuration imports.

The term-related paths and corresponding project counts are imported from
`helpers.term_paths` to ensure that these values are defined and maintained
in a single, consistent location (helpers/term_paths.py). 

The commented section below is included for reference and clarity.
"""


# Example structure (for reference only):
# TERM_SIZES = [
#     153,
#     147,
#     181,
#     200
# ]
#
# TERM_PATHS = [
#     "TERM_1_PATH",
#     "TERM_2_PATH",
#     "TERM_3_PATH",
#     "TERM_4_PATH"
# ]


# global constants
TOTAL_PROJECTS_RECEIVED = sum(TERM_SIZES)

term_length = {
            1: TERM_SIZES[0],
            2: TERM_SIZES[1],
            3: TERM_SIZES[2],
            4: TERM_SIZES[3],
        }


# core functions
def get_term(path: str) -> int | str:
    """Return the term number (as integer) corresponding to a given project path based on constant term substrings in path."""
    term_map = {"2021W-T1": 1, "2021W-T2": 2, "2023W-T2": 3, "2024W-T1": 4}
    for key, val in term_map.items():
        if key in path:
            return val
    print(f"Path does not match known terms: {path}")
    return "Unknown Term"


def get_gen_ai_period(path: str):
    """Find if repo is in genAI period based on term."""
    term = get_term(path)
    if term in [1, 2]:
        return False
    elif term in [3, 4]:
        return True
    print("Failed to return genAI period")
    

def process_commits(term_path: str):
    """
    Performs the repository mining and saves data into 
    csv-file.
    Get all commits in all projects for a given term.

    Args:
        term_path (str): path to the term we are mining

    Returns:
        dataframe: dataframe with all projects of the term
        str: filepath to the csv file containing the commit data
    """
    commit_records = []

    # Once per term
    term_number = get_term(term_path)
    gen_ai_period = get_gen_ai_period(term_path)
    
    # Define CSV file path
    timestr = time.strftime("%d%m%y")
    output_csv_filename = f"commit_stats_term_{term_number}_{timestr}.csv"
    output_path = "./output/"
    os.makedirs(output_path, exist_ok=True)  # Ensure directory exists
    csv_filepath = os.path.join(output_path, output_csv_filename)

    # Define CSV column headers (in Title Case)
    fieldnames = [
        "GenAI Period", "Term", "Project", 
        "Author Name", "Author Email", "Date", "Repository",
        "Insertions", "Deletions", "Total Lines", "Files Changed",
        "Diff Lines", "File Count",
        "Unit Size (DMM)", "Complexity (DMM)", "Interface (DMM)", 
        "Commit Hash", "Merge Commit", "Default Branch"
    ]

    file_exists = os.path.exists(csv_filepath)

    # Read existing data to show progress
    # TODO: Is this needed?
    if file_exists:
        existing_df = pd.read_csv(csv_filepath)
        if existing_df.empty:
            print("CSV is empty. Starting fresh.")
            print(f"Remaining projects to process: {TOTAL_PROJECTS_RECEIVED}")
        else:
            print(f"CSV contains commit data. {existing_df.shape[0]} commits already processed.")
            print(f"Last project processed: {existing_df['Project'].iloc[-1]}")
            remaining_projects = TOTAL_PROJECTS_RECEIVED - existing_df['Project'].nunique()
            print(f"Remaining projects to process: {remaining_projects}")
    else:
        print("No CSV file found. Starting from scratch.")
        print(f"Remaining projects to process: {TOTAL_PROJECTS_RECEIVED}")

    with open(csv_filepath, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is newly created
        if not file_exists:
            writer.writeheader()

        project_index = sum(term_length[t] for t in range(1, term_number))

        project_paths_of_term = []
        for d in os.listdir(term_path):
            full_path = os.path.join(term_path, d)
            if os.path.isdir(full_path):
                project_paths_of_term.append(full_path)

        # https://accessibleai.dev/post/extracting-git-data-pydriller/
        for proj_path in project_paths_of_term:
            print(f"Processing project {project_index} of term {term_number}")
            
            # Traversing all commits of a project
            # TODO: Check order of traversing?
            for commit in Repository(path_to_repo=proj_path, histogram_diff=True).traverse_commits():

                # data extracted from each commit
                record = {
                    "GenAI Period": gen_ai_period,
                    "Term": term_number, 
                    "Project": project_index,

                    "Author Name": commit.author.name.strip(),  
                    "Author Email": commit.author.email,
                    "Date": commit.committer_date.date(),
                    "Repository": commit.project_name,
                    
                    "Insertions": commit.insertions,
                    "Deletions": commit.deletions,
                    "Total Lines": commit.lines,
                    "Files Changed": commit.files,

                    "Diff Lines": commit.insertions - commit.deletions,

                    "Unit Size (DMM)": commit.dmm_unit_size,
                    "Complexity (DMM)": commit.dmm_unit_complexity,
                    "Interface (DMM)": commit.dmm_unit_interfacing,

                    "Commit Hash": commit.hash,
                    "Merge Commit": commit.merge,
                    "Default Branch": commit.in_main_branch,

                    # "Commiter": commit.commmiter, # We save the email and the name
                    # "Modified Files": commit.modified_files, # list of modified files
                    # 'Message': commit.msg
                }
            
                commit_records.append(record)
                writer.writerow(record)
            
            project_index += 1
        
    # Convert the list of records into a DataFrame and save to CSV
    df = pd.DataFrame(commit_records)
    print(f"***CSV file saved as {output_csv_filename} in {output_path}.***")

    # Return the DataFrame for further analysis if needed
    return df, csv_filepath


def extract_commit_messages(term_path: str):
    """
    Get all commit messages in all projects for a given term.

    Args:
        term_path (str): path to the term we are mining

    Returns:
        dataframe: dataframe with all projects of the term
        str: filepath to the csv file containing the commit messages
    """
    commit_records = []

    # Once per term
    term_number = get_term(term_path)
    gen_ai_period = get_gen_ai_period(term_path)
    
    # Define CSV file path
    timestr = time.strftime("%d%m%y")
    output_csv_filename = f"commit_messages_term_{term_number}_{timestr}.csv"
    output_path = "./output/"
    os.makedirs(output_path, exist_ok=True)  # Ensure directory exists
    csv_filepath = os.path.join(output_path, output_csv_filename)

    # Define CSV column headers (in Title Case)
    fieldnames = [
        "Commit Hash", "Commit Message"
    ]

    file_exists = os.path.exists(csv_filepath)

    print("Starting extraction of commit messages...")
    with open(csv_filepath, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is newly created
        if not file_exists:
            writer.writeheader()

        project_index = sum(term_length[t] for t in range(1, term_number))

        project_paths_of_term = []
        for d in os.listdir(term_path):
            full_path = os.path.join(term_path, d)
            if os.path.isdir(full_path):
                project_paths_of_term.append(full_path)

        # https://accessibleai.dev/post/extracting-git-data-pydriller/
        for proj_path in project_paths_of_term:
            print(f"Processing project {project_index} of term {term_number}")
            
            # Traversing all commits of a project
            # TODO: Check order of traversing?
            for commit in Repository(path_to_repo=proj_path, histogram_diff=True).traverse_commits():

                # data extracted from each commit
                record = {
                    "Commit Hash": commit.hash,
                    'Commit Message': commit.msg
                }
            
                commit_records.append(record)
                writer.writerow(record)
            
            project_index += 1
        
    # Convert the list of records into a DataFrame and save to CSV
    df = pd.DataFrame(commit_records)
    print(f"***CSV file saved as {output_csv_filename} in {output_path}.***")

    # Return the DataFrame for further analysis if needed
    return df, csv_filepath


# utility function
def merge_commit_data(term_files: list[str]) -> pd.DataFrame:
    """
    Merge all per-term commit CSV files into a single comprehensive dataset.

    This function combines the commit data produced for each term into
    a unified CSV file. It assumes that the individual term files share the same
    schema (columns).

    Args:
        term_files (list[str[]): File paths for the CSV files per term.

    Returns:
        pd.DataFrame: Merged DataFrame containing all commit data across terms.
    
    Example:
        >>> merge_commit_data(term_files)
        Merged 4 term files into 'output/commit_stats_all_terms_{timestr}.csv'.

    """


    # Define CSV file path
    timestr = time.strftime("%d%m%y")
    output_csv_filename = f"commit_stats_all_terms_{timestr}.csv"
    output_path = "./output/"
    os.makedirs(output_path, exist_ok=True)  # Ensure directory exists
    csv_filepath = os.path.join(output_path, output_csv_filename)

    dfs = [pd.read_csv(f) for f in term_files]
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv(csv_filepath, index=False)

    print(f"Merged {len(term_files)} term files into '{csv_filepath}'.") 

    return merged_df

# runner
def run_process_commits() -> None:
    """
    Execute commit processing for each academic term.

    Notes:
        - Processing a single term may take several hours for large repositories.
        - Uncomment individual lines below to process specific terms as needed.
    """

    print("Processing commits for selected terms...")

    # Uncomment individual lines as needed:
    # process_commits(TERM_PATHS[0])
    # process_commits(TERM_PATHS[1])
    # process_commits(TERM_PATHS[2])
    # process_commits(TERM_PATHS[3])

    print("Commit processing completed.")

    print("Extracting commit messages for selected terms...")
    # extract_commit_messages(TERM_PATHS[0])
    extract_commit_messages(TERM_PATHS[1])
    extract_commit_messages(TERM_PATHS[2])
    extract_commit_messages(TERM_PATHS[3])
    print("Completed...")


# main guard
if __name__ == "__main__":
    # This is how it would be performed when performing the commit mining
    print("Starting commit processing...")
    run_process_commits()

    term_files = [
                "./output/commit_stats_term_1_231025.csv",
                "./output/commit_stats_term_2_251025.csv",
                "./output/commit_stats_term_3_251025.csv", 
                "./output/commit_stats_term_4_261025.csv"
                ]
    

    # Merge commit data to a single file
    # merge_commit_data(term_files)
