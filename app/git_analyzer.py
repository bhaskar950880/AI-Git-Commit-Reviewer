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


def get_commit_diff(commit):
    if not commit.parents:
        return []

    parent = commit.parents[0]
    diffs = parent.diff(commit, create_patch=True)

    commit_diffs = []

    for diff in diffs:
        commit_diffs.append({
            "file": diff.a_path or diff.b_path,
            "change_type": diff.change_type,
            "diff": diff.diff.decode("utf-8", errors="replace")
        })

    return commit_diffs