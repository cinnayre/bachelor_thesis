from git import Repo
import util

def find_last_commit_date(repo_path):
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())
    if commits:
        return commits[0].committed_datetime.date()
    
def list_last_commit_date_per_project(path: str) -> list[int]:
    return util.apply_function_to_each_project(find_last_commit_date, path)

def find_first_commit_date(repo_path):
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())
    if commits:
        return commits[-1].committed_datetime.date()
    
def list_first_commit_date_per_project(path: str) -> list[int]:
    return util.apply_function_to_each_project(find_first_commit_date, path)
