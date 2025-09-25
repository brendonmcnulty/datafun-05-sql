import sqlite3
from pathlib import Path

DB_PATH = Path("project.sqlite3")
QUERIES = [
    Path("sql_queries/query_aggregation.sql"),
    Path("sql_queries/query_filter.sql"),
    Path("sql_queries/query_sorting.sql"),
    Path("sql_queries/query_group_by.sql"),
    Path("sql_queries/query_join.sql"),
]

def run_select(conn: sqlite3.Connection, sql_path: Path):
    sql = sql_path.read_text(encoding="utf-8").strip()
    print(f"\n=== {sql_path.name} ===")
    cur = conn.execute(sql)
    # print headers
    cols = [d[0] for d in cur.description]
    print(" | ".join(cols))
    print("-" * (len(" | ".join(cols))))
    # print rows
    for row in cur.fetchall():
        print(" | ".join(str(v) for v in row))

def main():
    with sqlite3.connect(DB_PATH) as conn:
        for path in QUERIES:
            run_select(conn, path)
    print("\nAll queries executed.")

if __name__ == "__main__":
    main()
