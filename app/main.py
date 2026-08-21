import json

from git_analyzer import (
    open_repository,
    get_latest_commit,
    get_commit_info,
    get_changed_files,
    get_commit_diff
)

from language_detector import detect_language


repo_path = r"D:\BookBazaar"

repo = open_repository(repo_path)

commit = get_latest_commit(repo)

info = get_commit_info(commit)


print("\n===== LATEST COMMIT =====")

print("Commit ID :", info["commit_id"])
print("Author    :", info["author"])
print("Message   :", info["message"])
print("Date      :", info["date"])


print("\n===== CHANGED FILES =====")

files = get_changed_files(commit)

for file in files:

    language = detect_language(file["file"])

    # Add language information to JSON data
    file["language"] = language

    print(
        file["change_type"],
        ":",
        file["file"],
        "→",
        language
    )


print("\n===== CODE DIFF =====")

diffs = get_commit_diff(commit)

for item in diffs:

    language = detect_language(item["file"])

    # Add language information to each diff
    item["language"] = language

    print("\nFILE:", item["file"])
    print("LANGUAGE:", language)
    print("CHANGE TYPE:", item["change_type"])
    print("-" * 60)
    print(item["diff"])


review_data = {
    "commit": info,
    "changed_files": files,
    "diffs": diffs
}


with open("review_data.json", "w", encoding="utf-8") as file:

    json.dump(
        review_data,
        file,
        indent=4,
        default=str
    )


print("\nReview data saved to review_data.json")