# Paths
TERM_1_PATH = 'C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T1' # 21T1
TERM_2_PATH = 'C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2021W-T2' # 21T2
TERM_3_PATH = 'C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2023W-T2' # 23T2
TERM_4_PATH = 'C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/CPSC310_termData/CPSC310-2024W-T1' # 24T1

TERM_PATHS = [
    TERM_1_PATH,
    TERM_2_PATH,
    TERM_3_PATH,
    TERM_4_PATH
]

version_path = 'Code V3/'
base_path = 'C:/Bibliothek/Career/UZH/BA BT Bachelor Arbeit Thesis/' + version_path

# Datasets
project_level_dataset_path_raw = base_path + 'output/interim_results/project_level_dataset_raw_231225.csv'
commit_level_dataset_path_raw = base_path + 'output/interim_results/commit_stats_all_terms_031125.csv'

project_level_dataset_path_normalized = base_path + 'output/project_level_dataset_normalized.csv'
commit_level_dataset_path_normalized = base_path + 'output/commit_level_dataset_normalized.csv'

project_level_dataset_path_cleaned = base_path + 'output/project_level_dataset_cleaned.csv'
commit_level_dataset_path_cleaned = base_path + 'output/commit_level_dataset_cleaned.csv'
dev_level_dataset_path_cleaned = base_path + "output/dev_level_dataset_cleaned.csv"

# Plots
plots_path = base_path + "visualization/plots"

# Constants

# Number of projects per term
TERM_SIZES = [
    153,
    147,
    181,
    200
]

# from sns.color_palette('bright')
TERM_COLORS = [
    '#023eff', 
    '#ff7c00', 
    '#1ac938', 
    '#e8000b'
]

# Deadlines
# CPSC310-2021W-T1
t1_c0 = '2021-09-20'
t1_c1 = '2021-10-12'
t1_c2 = '2021-11-01'
t1_c3 = '2021-11-29'

# CPSC310-2021W-T2
t2_c0 = '2022-01-21'
t2_c1 = '2022-02-11'
t2_c2 = '2022-03-04'
t2_c3 = '2022-04-01'

# CPSC310-2023W-T2:
t3_c0 = '2024-01-26'
t3_c1 = '2024-02-16'
t3_c2 = '2024-03-15'
t3_c3 = '2024-04-04'

# CPSC310-2024W-T1
t4_c0 = '2024-09-20'
t4_c1 = '2024-10-11'
t4_c2 = '2024-11-01'
t4_c3 = '2024-11-22'

term_1_deadlines = [t1_c0, t1_c1, t1_c2, t1_c3]
term_2_deadlines = [t2_c0, t2_c1, t2_c2, t2_c3]
term_3_deadlines = [t3_c0, t3_c1, t3_c2, t3_c3]
term_4_deadlines = [t4_c0, t4_c1, t4_c2, t4_c3]

term_deadlines = [*term_1_deadlines, *term_2_deadlines, *term_3_deadlines, *term_4_deadlines]




project_cols = ['3_folders_total_lines', '3_folders_sloc','cc_sum_3folders', 'comment_density']

commit_cols = ['total_lines', 'unit_size_dmm', 'complexity_dmm', 'interface_dmm', ]

dev_cols = [
    'commits_per_developer', 
    'contribution_per_developer',
    'commit_contribution_ratio', 
    'relative_code_churn', 
    ]