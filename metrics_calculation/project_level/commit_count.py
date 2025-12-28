from git import Repo
import util

def count_number_of_commits(repo_path: str) -> int:
    repo = Repo(repo_path)
    return sum(1 for _ in repo.iter_commits())

def list_commit_counts_per_project(path: str) -> list[int]:
    return util.apply_function_to_each_project(count_number_of_commits, path)



