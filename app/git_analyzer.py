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


# Testing
repo_path = r"D:\BookBazaar"

repo = open_repository(repo_path)

commit = get_latest_commit(repo)

info = get_commit_info(commit)

print("\n===== LATEST COMMIT =====")
print("Commit ID :", info["commit_id"])
print("Author    :", info["author"])
print("Message   :", info["message"])
print("Date      :", info["date"])

def get_changed_files(commit):
    if not commit.parents:
        return []

    parent = commit.parents[0]
    diffs = parent.diff(commit)

    changed_files = []

    for diff in diffs:
        changed_files.append({
            "file": diff.a_path or diff.b_path,
            "change_type": diff.change_type
        })

    return changed_files

print("\n===== CHANGED FILES =====")

files = get_changed_files(commit)

for file in files:
    print(file["change_type"], ":", file["file"])