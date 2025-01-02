import os
import subprocess
from datetime import datetime

# Global Var
file_path = "counter.txt"

def increment_counter():
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0\n")

    with open(file_path, "r") as f:
        try:
            counter = int(f.read().strip())
        except ValueError:
            counter = 0

    counter += 1

    with open(file_path, "w") as f:
        f.write(f"{counter}\n")
    
    return counter


def git_commit_and_push(counter):
    try:
        subprocess.run(["git", "add", file_path], check=True)
        timestamp = datetime.now().strftime("%m-%d-%Y %H:%M")
        commit_message = f"Auto-update counter to {counter} at {timestamp}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    counter = increment_counter()
    git_commit_and_push(counter)
