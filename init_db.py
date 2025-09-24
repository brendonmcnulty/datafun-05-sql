import sqlite3
from pathlib import Path

DB_PATH = Path("project.sqlite3")
SQL_PATH = Path("create_tables.sql")

def main() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        script = SQL_PATH.read_text(encoding="utf-8")
        conn.executescript(script)
    print(f"Initialized database at {DB_PATH.resolve()}")

if __name__ == "__main__":
    main()
