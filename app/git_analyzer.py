from git import Repo

def open_repository(repo_path):
    return Repo(repo_path)
def get_latest_commit(repo):
    return repo.head.commit
def get_commit_info(commit):
    return {
        "commit_id": commit.hexsha,
        "author": commit.author.name,
        "message": commit.message.strip(),
        "date": commit.committed_datetime
    }
