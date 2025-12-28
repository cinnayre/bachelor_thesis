from git import Repo
import util
from pathlib import Path
import pandas as pd

bots = {
    "cs-310-noreply@students.cs.ubc.ca", 
    "310-bot@students.cs.ubc.ca", 
    "autobot@students.cs.ubc.ca", 
    "classy@cs.ubc.ca"
}

def count_unique_commit_authors(repo_path: str) -> int:
    repo = Repo(repo_path)
    authors = {commit.author.email for commit in repo.iter_commits()}
    authors -= bots 
    # for a in authors:
    #     print(a.name, a.email)
    return len(authors)

def list_unique_commit_authors_per_project(path: str) -> list[int]:
    return util.apply_function_to_each_project(count_unique_commit_authors, path)

# Check how many projects each author has contributed to in a term, useful to identify bots --> see bots
def count_projects_per_author_df(term_path: str) -> pd.DataFrame:
    """Return DataFrame with columns [email, project_count]."""
    author_projects = {}

    for project in Path(term_path).iterdir():
        if not project.is_dir():
            continue

        repo = Repo(project)
        project_authors = {commit.author.email for commit in repo.iter_commits()}

        for email in project_authors:
            author_projects[email] = author_projects.get(email, 0) + 1

    return pd.DataFrame(
        [(email, count) for email, count in author_projects.items()],
        columns=["email", "project_count"]
    )

