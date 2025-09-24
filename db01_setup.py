import sqlite3
from pathlib import Path

DB_PATH = Path("project.sqlite3")

def run_sql_file(cursor, filepath: Path):
    """Read and execute a SQL file."""
    script = filepath.read_text(encoding="utf-8")
    cursor.executescript(script)
    print(f"Executed {filepath.name}")

def main():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        # Run the SQL files in order
        run_sql_file(cur, Path("sql_create/01_drop_tables.sql"))
        run_sql_file(cur, Path("sql_create/02_create_tables.sql"))
        run_sql_file(cur, Path("sql_create/03_insert_records.sql"))
        conn.commit()
    print(f"Database setup complete: {DB_PATH.resolve()}")

if __name__ == "__main__":
    main()
