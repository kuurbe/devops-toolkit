import subprocess

def get_commit_summary():
    try:
        output = subprocess.check_output(["git", "log", "--oneline"])
        commits = output.decode().strip().split('\n')
        print(f"Total commits: {len(commits)}")
        print("Recent commits:")
        for commit in commits[:5]:
            print(f" - {commit}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_commit_summary()
