import pandas as pd
import util
import dataframe_utils
from metrics_calculation import (
    file_count,
    folder_count,
    commit_count,
    commit_dates,
    commit_authors,
    commit_count_per_author,
    file_extension_count,
    loc_count,
    locc_count,
    locc_count_nirjas,
    cyclomatic_complexity,
)
from lizard import analyze_file
from pydriller import Repository
from helpers.project_config import TERM_PATHS



TERM_1_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1" # 21T1
TERM_2_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T2" # 21T2
TERM_3_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2023W-T2" # 23T2
TERM_4_PATH = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2024W-T1" # 24T1

term_paths = [TERM_1_PATH, TERM_2_PATH, TERM_3_PATH, TERM_4_PATH]

def development_one(): 

    # works and returns a list of numbers or wanted datapoints

    # concat_results is helper function from util that applies the function to each term, the list version of a function uses the apply_function_to_each_project helper function from util which applies the function to each project in the term path

    print(
    )
    print(
    )

    sampleproject = TERM_2_PATH + "/project_team576"
    # Check for one project that method works (sample project)

    # print(f"Last commit date for {sampleproject}: {commit_count.find_last_commit_date(sampleproject)}")

# takes forever therefore run once then comment out
# runtime without lines of code: around 90 minutes
# runtime only lines of code: i guess around 60 minutes
def create_dataframe_one():
    print("Running create_dataframe_one() to extract and export metrics...")
    print(f"Full version takes around 90 minutes. Started at {pd.Timestamp.now()}")
    # dataframe_utils.extract_and_export_metrics("metrics_data_110825_2.csv")
    
def development_two():
    
    # locdf = dataframe_utils.load_dataframe("metrics_data_110825_2.csv")
    # restdf = dataframe_utils.load_dataframe("metrics_data_110825.csv")
    # print(locdf.count())
    # print(restdf.count())

    # Example: insert row 2 of df2 between row 3 and 4 of df1
    # row_to_insert = locdf  # Keep as DataFrame (double brackets)

    # print(row_to_insert.count())

    # df_result = pd.concat(
    #     [restdf.iloc[:11], 
    #      row_to_insert,
    #      restdf.iloc[11:]],
    # )

    # print(df_result)

    # print(locc_count.count_comments_in_file("C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team042/src/rest/Server.ts"))
    # print(loc_count.count_lines_of_code("C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team042/src/rest"))
    # commit_authors.count_unique_commit_authors("C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team059")
    pass

# debug example paths of projects
p0 = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team037" # Index 0
p1 = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team038" # Index 1
p2 = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team064"
p3 = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team059"
p4 = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2024W-T1/project_team228" # Index 678 (before cleaning)
p14 = "C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1/project_team051"

def debug_print_files_sorted_by_extension(path_test:str):
    # uncomment debug version in file_extension_count.py to see all files printed
    print("JavaScript paths")
    file_extension_count.count_files_by_extension(path_test, ".js")
    print("JavaScript X paths")
    file_extension_count.count_files_by_extension(path_test, ".jsx")
    print("TypeScript paths")
    file_extension_count.count_files_by_extension(path_test, ".ts")
    print("TypeScript X paths")
    file_extension_count.count_files_by_extension(path_test, ".tsx")

def development_three():  
    # debug_print_files_sorted_by_extension(p4)

    # locc_count_nirjas.dummy()

    # locc_count_nirjas.apply_nirjas_metrics_to_each_project(TERM_1_PATH)
    #dataframe_utils.save_dataframe(locc_count_nirjas.sf, "output/nirjas_metrics_term1_v1_080925.csv")
    pass

# Calculates nirjas metrics for all terms and saves to csv
# nirjas attributes = ["file_count", "total_lines", "sloc", "total_lines_of_comments", "blank_lines"]
def create_dataframe_two():
    print("Running create_dataframe_two() to calculate nirjas metrics...")
    print(f"Full version takes around 30 minutes. Started at {pd.Timestamp.now()}")
    
    output_file = "output/nirjas_metrics_allterms_v1_080925.csv"

    # Call one per term path
    all_dfs = [locc_count_nirjas.apply_nirjas_metrics_to_each_project(tp) for tp in TERM_PATHS]
    # Concatenate results
    final_df = pd.concat(all_dfs, ignore_index=True)
    dataframe_utils.save_dataframe(final_df, output_file)

    print(f"Finished at {pd.Timestamp.now()}")
    print(final_df.shape)
    print(final_df.head())



def investigate():
    # commit_authors.count_unique_commit_authors(p2)
    # dfm = commit_authors.count_projects_per_author_df(TERM_4_PATH)
    # dfm.sort_values(by="project_count")
    # print(dfm[dfm["project_count"] > 1].head())
    data_x = util.concat_results(commit_authors.list_unique_commit_authors_per_project)
    print(len(data_x), type(data_x)) # yields 681 <class 'list'>
    # print(type(data_x[0]), len(data_x[0]), data_x[0])
    dfc = pd.DataFrame({"unique commit authors": data_x})
    print(dfc.head())
    # dataframe_utils.save_dataframe(dfc, "output/new_unique_commit_authors_150925.csv")

# investigate()




# PYDRILLER - Commit based metrics

# How many commits to a file, sorted by frequency 
# Example output: Rooms.jsx, Commit Count: 5
def get_commit_count_per_file(project_path: str) -> dict[str: int] :
    file_commit_counts = {}

    for commit in Repository(project_path).traverse_commits():
        for mf in commit.modified_files:
            if mf.filename not in file_commit_counts:
                file_commit_counts[mf.filename] = 0
            file_commit_counts[mf.filename] += 1

    sorted_files = sort_files(file_commit_counts)
    
    return sorted_files

# files below is a dictionary {filename: commit_count} as result of the get_commit_count_per_file method

# Sort files by value
def sort_files(files: dict[str: int], reverse=False) -> dict[str: int]:
    sorted_files = sorted(files.items(), key=lambda x: x[1], reverse=reverse)
    return sorted_files
    
def print_files(files: dict[str: int]) -> None:
    for filename, count in files:
        print(f"File: {filename}, Commit Count: {count}")

def unique_file_count(files: dict[str: int]) -> int:
    return len(files)

# example output: Extension: .ts, Count: 15
# This means that to 15 unique .ts files was committed in the project.
def unique_file_count_by_extension(files: dict[str: int]) -> dict[str: int]:
    extensions = {}
    for filename, count in files:
        ext = filename.split('.')[-1] if '.' in filename else ''
        if ext and ext not in extensions:
            extensions[ext] = 0
        if ext:
            extensions[ext] += 1
    sorted_ext = sort_files(extensions)
    return sorted_ext

# example output: Extension: .ts, Count: 189
# This means that in sum 189 commits were made to .ts files in the project.
def summed_file_count_by_extension(files: dict[str: int]) -> dict[str: int]:
    extensions = {}
    for filename, count in files:
        ext = filename.split('.')[-1] if '.' in filename else ''
        if ext and ext not in extensions:
            extensions[ext] = 0
        if ext:
            extensions[ext] += count
    sorted_ext = sort_files(extensions)
    return sorted_ext

# Try Out Pydriller based metrics
def calculate_commit_based_metrics(project_path: str):
    # How many commits to a file, sorted by frequency 
    files = get_commit_count_per_file(project_path)
    # print_files(files)

    # How many different files was commited to in the project
    # =? file count
    unique_file_count_var = unique_file_count(files)
    print(f"Amount of files commited to: {unique_file_count_var}")

    # This means that to so many unique files with certain extension was committed in the project.
    unique_file_count_by_extension_var = unique_file_count_by_extension(files)
    print("Unique file commit count:")
    print_files(unique_file_count_by_extension_var)

    # How many different extensions are there in a project
    print(f"Amount of different ext in project: {len(unique_file_count_by_extension_var)}")

    # This means that in sum so many commits were made to files with a certain extension in the project.
    # summed_file_count_by_extension_var = summed_file_count_by_extension(files)
    # print("File commit count:")
    # print_files(summed_file_count_by_extension_var)

# calculate_commit_based_metrics(p0)




# LIZARD


# Lizard based file count
def count_functions_per_file(file_path: str) -> int:
    result = analyze_file(file_path)
    return len(result.function_list)

# Try Out Lizard based metrics
def lizard():
    
    file = "C:/Bibliothek\\Career\\UZH\\BA BT Bachelor Arbeit Thesis\\CPSC310_termData\\CPSC310-2021W-T1\\project_team038\\src\\controller\\InsightFacade.ts"
    file2 = "C:/Bibliothek\\Career\\UZH\\BA BT Bachelor Arbeit Thesis\\Code V2\\testfiles\\simplefunctions.ts"
    file3 = "C:/Bibliothek\\Career\\UZH\\BA BT Bachelor Arbeit Thesis\\Code V2\\testfiles\\simplebranches_cc_test.py"
    file4 = "C:/Bibliothek\\Career\\UZH\\BA BT Bachelor Arbeit Thesis\\CPSC310_termData\\CPSC310-2021W-T1\\project_team038\\frontend\\components\\background.module.css"
    file5 = "C:/Bibliothek\\Career\\UZH\\BA BT Bachelor Arbeit Thesis\\CPSC310_termData\\CPSC310-2021W-T1\\project_team047\\package.json"

    # cyclomatic_complexity.calculate_cc_of_file(file5, debug_print=True)
    # print("Function Count:", count_functions_per_file(file3))
    cyclomatic_complexity.calculate_cc_of_project(p4) 

# lizard()


# Calculates cc per project for all terms and saves to csv
# careful takes long to run
def create_dataframe_three():
    print("Running create_dataframe_three() to calculate cc per project for all terms...")
    start_time = pd.Timestamp.now()
    print(f"Full version takes around 2h for 681 projects. Started at {start_time}") # 16:30

    
    output_file = "output/cc_project_sum_lizard_metrics_3folders_v2_260925.csv"

    # Call one per term path
    cc_sum_data = {
        "CC Sum": util.concat_results(cyclomatic_complexity.list_cc_per_project) 
    }

    cc_df = dataframe_utils.create_dataframe(cc_sum_data)
    dataframe_utils.save_dataframe(cc_df, output_file) 

    # 18:10 = 1h40
    print(f"Finished at {pd.Timestamp.now()}, took: {pd.Timestamp.now() - start_time}")

# create_dataframe_three()

print(TERM_PATHS[0])
# cyclomatic_complexity.list_irrelevant_files_per_project(TERM_4_PATH)
