import sqlite3
from pathlib import Path

DB_PATH = Path("project.sqlite3")

def run_sql_file(cursor, filepath: Path):
    script = filepath.read_text(encoding="utf-8")
    cursor.executescript(script)
    print(f"Executed {filepath.name}")

def main():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        run_sql_file(cur, Path("sql_features/update_records.sql"))
        run_sql_file(cur, Path("sql_features/delete_records.sql"))
        conn.commit()
    print("Feature scripts applied.")

if __name__ == "__main__":
    main()
