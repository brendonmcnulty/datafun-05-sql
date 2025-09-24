# datafun-05-sql

This project introduces working with **SQL** inside Python using the built-in `sqlite3` module.  
We’ll create and manage a lightweight, file-based database (SQLite) and practice writing SQL queries in Python scripts.

---

## Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/<your-username>/datafun-05-sql.git
cd datafun-05-sql
2. Create and Activate Virtual Environment
bash
Copy code
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install Requirements
bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
4. Git Commands (repeat often)
bash
Copy code
git status
git add .
git commit -m "your message here"
git push origin main
git pull
Project Structure
pgsql
Copy code
datafun-05-sql/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ create_tables.sql     # SQL to create authors/books tables
├─ init_db.py            # Python script to initialize project.sqlite3
├─ project.sqlite3       # SQLite database file (created after running init_db.py)
├─ data/
│  ├─ authors.csv
│  └─ books.csv
└─ sql_create/
   └─ 03_insert_records.sql  # example from instructor repo
