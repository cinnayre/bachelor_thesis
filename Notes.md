# DF (CSV Files) Overview
*List all the files in which the extracted and calculated metrics are stored, i.e. the dataframes.*

- metrics_data_110825_2.csv
  - older version of basic metrics?
- Data_v1 - metrics_data_180825.csv
  - (681, 25)
  - Selfmade Basic metrics - File Count, LoC Count, Commit Count, ... see DF One
- nirjas_metrics_allterms_v1_080925.csv
  - (681, 40)
  - All combinations of DF Two - LoCC
- nirjas_aggregated_metrics_v2_150925.csv
  - (681, 100)
  - Aggregated combinations of DF Two / nirjas_metrics_allterms_v1
- new_unique_commit_authors_150925.csv
  - (681, 1)
  - removed bots from 'unique commit authors'
- cc_project_sum_lizard_metrics_v1_240925.csv
  - (681, 1)
  - Sum CC
- cc_project_sum_lizard_metrics_3folders_v2_260925.csv
  - (681, 1)
  - Sum CC 3folders
- aggregated_metrics_v4_061025.csv
  - (681, 102)
  - Selfmade Basics, Nirjas (LoCC), Aggregated Nirjas, 'unique commit authors' Update, Lizard CC
  - version 4 of all information together
- cleaned_aggregated_metrics_v4_061025.csv
  - (672,103)
  - all information together
    - invalid projects removed
    - terms added
  - smaller other versions before that
- commit_messages_term_1-4_121125.csv
  - to check content of commit messages
- commit_stats_all_terms_031125
  - (86483,19)
  - all commits of all 681 projects

# Metrics in DFs
*List columns (dimensions, extracted metrics) for big dataframes*
### DF One
- project index
- folder count
- file count
- file count tslike
- file count .ts
- file count .tsx
- file count .js
- file count .jsx
- commit count
- unique commit authors
- commit count per author
- first commit date
- last commit date
- lines of code
- lines of code tslike
- lines of code .ts
- lines of code .tsx
- lines of code .js
- lines of code .jsx
- lines of comments
- lines of comments tslike
- lines of comments .ts
- lines of comments .tsx
- lines of comments .js
- lines of comments .jsx
  
### Added at some point
- CC Sum
- CC Sum 3folders # sum of cc of only files in the 3 subfolders described below
- term

### DF Two
- /frontend .ts file_count
- /frontend .ts total_lines
- /frontend .ts sloc
- /frontend .ts total_lines_of_comments
- /frontend .ts blank_lines
- /frontend .js file_count
- /frontend .js total_lines
- /frontend .js sloc
- /frontend .js total_lines_of_comments
- /frontend .js blank_lines
- /src .ts file_count
- /src .ts total_lines
- /src .ts sloc
- /src .ts total_lines_of_comments
- /src .ts blank_lines
- /src .js file_count
- /src .js total_lines
- /src .js sloc
- /src .js total_lines_of_comments
- /src .js blank_lines
- /test/controller .ts file_count
- /test/controller .ts total_lines
- /test/controller .ts sloc
- /test/controller .ts total_lines_of_comments
- /test/controller .ts blank_lines
- /test/controller .js file_count
- /test/controller .js total_lines
- /test/controller .js sloc
- /test/controller .js total_lines_of_comments
- /test/controller .js blank_lines
- /test/rest .ts file_count
- /test/rest .ts total_lines
- /test/rest .ts sloc
- /test/rest .ts total_lines_of_comments
- /test/rest .ts blank_lines
- /test/rest .js file_count
- /test/rest .js total_lines
- /test/rest .js sloc
- /test/rest .js total_lines_of_comments
- /test/rest .js blank_lines
  
  ### Aggregated DF Two 
- 3 Folders file_count
- 3 Folders total_lines
- 3 Folders sloc
- 3 Folders total_lines_of_comments
- 3 Folders blank_lines
- /frontend file_count
- /frontend total_lines
- /frontend sloc
- /frontend total_lines_of_comments
- /frontend blank_lines
- /src file_count
- /src total_lines
- /src sloc
- /src total_lines_of_comments
- /src blank_lines
- /test/controller file_count
- /test/controller total_lines
- /test/controller sloc
- /test/controller total_lines_of_comments
- /test/controller blank_lines
- /test/rest file_count
- /test/rest total_lines
- /test/rest sloc
- /test/rest total_lines_of_comments
- /test/rest blank_lines
- TypeScript file_count
- TypeScript total_lines
- TypeScript sloc
- TypeScript total_lines_of_comments
- TypeScript blank_lines
- JavaScript file_count
- JavaScript total_lines
- JavaScript sloc
- JavaScript total_lines_of_comments
- JavaScript blank_lines


# Notes DF Two 

Attributes in Dataframe
```
folders_nirjas = ['/frontend', '/src', '/test/controller', '/test/rest']
# language
file_types_nirjas = { 
    '.ts': 'TypeScript',
    '.js': 'JavaScript',
}
# comment metric
attribute_nirjas = ['file_count', 'total_lines', 'sloc', 'total_lines_of_comments', 'blank_lines']
Is sloc = total_lines - blank_lines - total_lines_of_comments
```

- folder + language + comment metric: = DF Two
  - /frontend .ts blank_lines
  - 4 x 2 x 5
- folder + metric --> in frontend blank_lines
  - 4 x 5
- language + metric --> in all folders typescript blank_lines
  - 2 x 5
- metric --> in all folder blank_lines
  - 5

# DF Commit level
- GenAI Period
- Term
- Project
- Author Name
- Author Email
- Date
- Repository
- Insertions
- Deletions
- Total Lines
- Files Changed
- Diff Lines
- File Count
- Unit Size (DMM)
- Complexity (DMM) 
- Interface (DMM)
- Commit Hash
- Merge Commit
- Default Branch

# Learnings

In VS Code you don’t need to rely only on Ctrl + Left Click. Here are faster ways for multi-cursor editing:

- Alt + Click → add a new cursor at any point.
- Ctrl + Alt + ↑ / ↓ → add a cursor on the line above or below.
- Ctrl + D → select the next occurrence of the word under the cursor.
- Ctrl + Shift + L → select all occurrences of the word under the cursor (multi-cursor everywhere).
- Alt + Shift + Drag (mouse) → create a rectangular block selection (column editing).

Most efficient: Ctrl + Alt + ↑ / ↓ and Ctrl + Shift + L for repeating patterns.

### How to use Jupyter Notebooks in VS Code
You can connect Juypter Notebook with VS Code by: 
1. Starting `juypter notebook` in the terminal
2. Copy jupyter kernel link from the window that opens automatically
3. Open ipynb file in VS Code
4. Attempt running a cell
5. In the appearing pop up choose existing running kernel
6. Enter jupyter kernel link and press Enter

### About Python
- `*` in a function defintion is a syntax marker meaning: “all parameters after this must be passed by keyword.” Example: 
  - `def foo(x: int, *, inplace: bool = False) -> int:`
  - That makes `inplace` keyword-only, so callers must do `inplace=True` (and can’t do `foo(x, True)` by accident).
- Loading Issues
  - In Jupyter, import helpers.project_config as cfg is cached, so edits to project_config.py won’t take effect until you reload the module or restart the kernel.
  - If a path/config value from that file looks “wrong” after you change it, restart the kernel and rerun all relevant cells to ensure you’re not using a stale import.
- `pd.merge(suffixes="")` keyword explaine
  - suffixes is for when both DataFrames have overlapping non-key column names.
  - Example: if both have a column called dev (or any other same-named column not used as a join key), pandas needs a way to rename them so they don’t collide.
  - suffixes=("", "_bot") means:
    - left df keeps dev
    - right df’s dev becomes dev_bot
  - So you might get columns like dev and dev_bot.
- Remove all rows that contain non number values from dataframe:
  - `df = df[~df[cols].isna()]`
# Main Metrics

## Project-Level Dataset
- LoC (maybe filter language or folder) 3_folders_total_lines x s
- LoCC (maybe filter language or folder) 3_folders_total_lines_of_comments 
- SLoC (maybe filter language or folder) 3_folders_sloc x s
- CC (maybe filter language or folder) 3_folders_cc_sum x
- comment_density (maybe filter language or folder) 3_folders_total_lines_of_comments / 3_folders_total_lines x

Metadata:
- project_id
- term
- genai_period

Additional interessting things:
- blank lines, sloc

## Commit-Level Dataset
- insertions
- deletions
- total_lines (insertions + deletions, code_churn) x s
- diff_lines (insertions - deletions)
- file_count (files_changed)
  
[0,1]
- unit_size_dmm x
- complexity_dmm x
- interface_dmm x

Flags:
- merge_commit
- default_branch

Metadata:
- project_id
- term
- genai_period
- date
- dev_id (from name and email, dev1, dev2, ..., bot, unclear)
- commit_hash

Calculate from Commit-Level Dataset:
- commits_per_developer - # of commits per developer x 
- contribution_per_developer - sum(churn per commit) of dev x s
- commit_contribution_ratio (developer_commit_fraction) - # of commits dev / # of commits project x
- relative_code_churn - sum(churn per commit) of dev / sum(churn of commit) of project x

# Notes
- Provides a clear, typed function with input validation and a descriptive
docstring. Constants are defined for default parameters.
- Violin plot helper following project Python coding standards.
  - Creates a violin plot for a numeric column grouped by `x`. Performs
input validation and documents behavior.
