import pandas as pd
from util import (
    concat_results, 
    aggregate_file_counts_by_extension,
    aggregate_loc_counts_by_extension,
    aggregate_locc_counts_by_extension
)
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
)

# Define the file extensions to be used in the analysis
file_extensions = ['.ts', '.tsx', '.js', '.jsx']

# extract data and combine into dictionary
def extract_data() -> dict:
# for each metric, we can use the util.concat_results to get the data for all terms
    data = {
        # folder and file counts
        # "folder count": concat_results(folder_count.list_nested_folder_counts_per_project),
        # "file count": concat_results(file_count.list_file_counts_per_project),
        # **{f"file count {ext}": aggregate_file_counts_by_extension(ext) for ext in file_extensions},
        
        # commit related metrics
        # "commit count": concat_results(commit_count.list_commit_counts_per_project),
        # "unique commit authors": concat_results(commit_authors.list_unique_commit_authors_per_project),
        # "commit count per author": concat_results(commit_count_per_author.list_commit_counts_per_author_per_project),
        # "first commit date": concat_results(commit_dates.list_first_commit_date_per_project),
        # "last commit date": concat_results(commit_dates.list_last_commit_date_per_project),
        
        # "lines of code": concat_results(loc_count.list_lines_of_code_per_project),
        # **{f"lines of code {ext}": aggregate_loc_counts_by_extension(ext) for ext in file_extensions},
        # lines of code (comment) metrics 
        # "lines of comments": concat_results(locc_count.list_lines_of_comments_per_project),
        # **{f"lines of comments {ext}": aggregate_locc_counts_by_extension(ext) for ext in file_extensions},
    }
    return data

# create data frame with data
def create_dataframe(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    return df

# save data frame to csv file
def save_dataframe(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, index=True)

# load data frame from csv file
def load_dataframe(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename, index_col=0)

def extract_and_export_metrics(filename: str = "metrics_data.csv") -> pd.DataFrame:
    data = extract_data()
    df = create_dataframe(data)
    save_dataframe(df, filename)
    return df