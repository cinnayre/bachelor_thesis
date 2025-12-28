from git import Repo
import util
from collections import Counter

def count_commits_per_author(repo_path: str, debug: bool = False) -> list[int]:
    repo = Repo(repo_path)
    author_counts = Counter(commit.author.email for commit in repo.iter_commits())

    if debug:
        print("DEBUG: Commits per author (email: count):")
        for author, count in author_counts.most_common():
            print(f"  {author}: {count}")

    return [count for _, count in author_counts.most_common()]

def list_commit_counts_per_author_per_project(path: str) -> list[list[int]]:
    return util.apply_function_to_each_project(count_commits_per_author, path)

# Debug version for all projects
# def list_commit_counts_per_project(path: str, debug: bool = False) -> list[list[int]]:
#     return util.apply_function_to_each_project(
#         lambda repo_path: count_commits_per_author(repo_path, debug),
#         path
#     )
