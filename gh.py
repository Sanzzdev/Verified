import os
import subprocess
from datetime import datetime, timedelta

# Ganti dengan URL repositori GitHub kamu
GITHUB_REPO_URL = "https://github.com/Sanzzdev/Verified.git"

# Nama direktori lokal untuk repositori
repo_name = "Verified"

# Membuat direktori dan menginisialisasi repositori Git
if not os.path.exists(repo_name):
    os.makedirs(repo_name)
    os.chdir(repo_name)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "add", "origin", GITHUB_REPO_URL])
else:
    os.chdir(repo_name)

# Periode komit, misalnya satu tahun terakhir
start_date = datetime.now() - timedelta(days=365)

# Loop untuk setiap hari selama satu tahun
for i in range(366):  # 366 hari termasuk tahun kabisat
    date = start_date + timedelta(days=i)
    with open("README.md", "a") as file:
        file.write(f"Commit on {date.date()}\n")
    
    # Menambahkan perubahan ke staging dan membuat komit
    subprocess.run(["git", "add", "."])
    commit_message = f"Commit on {date.date()}"
    subprocess.run(["git", "commit", "-m", commit_message])

    # Mengatur tanggal komit
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = date.isoformat()
    env["GIT_AUTHOR_DATE"] = date.isoformat()
    subprocess.run(["git", "commit", "--amend", "--no-edit"], env=env)

# Push semua komit ke GitHub
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "push", "-u", "origin", "main"])
