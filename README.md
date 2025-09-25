# DataFun-05-SQL

This project integrates **Python and SQL** using the built-in `sqlite3` library and a lightweight SQLite database.  
It demonstrates how to create a schema, insert records, update and delete data, and run SQL queries from Python.

---

## Project Progress

- [ ] Step 1–3: Project Setup  
  - Repo created (`datafun-05-sql`) with default `README.md`.  
  - `.gitignore` and `requirements.txt` added and pushed.  
  - Virtual environment `.venv` created and activated.  
  - Dependencies installed from `requirements.txt`.  

- [ ] Step 4: Schema Design and Database Initialization  
  - Added `sql_create/01_drop_tables.sql` (drops existing tables).  
  - Added `sql_create/02_create_tables.sql` (creates `authors` and `books` tables).  
  - Added `sql_create/03_insert_records.sql` (inserts at least 10 authors and 10 books).  
  - Created `db01_setup.py` to run these scripts in order and initialize `project.sqlite3`.  
  - Verified tables and data in VS Code using **SQLite Viewer (Florian Klampfer)**.  

- [ ] Step 5: Cleaning and Feature Engineering  
  - Added `sql_features/update_records.sql` (demonstrates UPDATEs).  
  - Added `sql_features/delete_records.sql` (demonstrates DELETEs).  
  - Created `db02_features.py` to apply these scripts.  
  - Verified changes in SQLite Viewer:  
    - Corrected title for *Harry Potter and the Philosopher's Stone* (`b10`).  
    - Updated publication year for *1984* (`b02`).  
    - Deleted *Fahrenheit 451* (`b06`).  

- [ ] Step 6: Queries and Aggregations  
  - Added `sql_queries/query_aggregation.sql` (COUNT, MIN, MAX).  
  - Added `sql_queries/query_filter.sql` (WHERE filter).  
  - Added `sql_queries/query_sorting.sql` (ORDER BY).  
  - Added `sql_queries/query_group_by.sql` (GROUP BY with JOIN).  
  - Added `sql_queries/query_join.sql` (INNER JOIN).  
  - Created `db03_queries.py` to run these SQL queries and print results to the terminal.

---

## Project Structure
datafun-05-sql/
├── sql_create/
│ ├── 01_drop_tables.sql
│ ├── 02_create_tables.sql
│ └── 03_insert_records.sql
├── sql_features/
│ ├── update_records.sql
│ └── delete_records.sql
├── sql_queries/
│ ├── query_aggregation.sql
│ ├── query_filter.sql
│ ├── query_sorting.sql
│ ├── query_group_by.sql
│ └── query_join.sql
├── db01_setup.py
├── db02_features.py
├── db03_queries.py
├── project.sqlite3
├── data/
│ ├── authors.csv
│ └── books.csv
├── .gitignore
├── README.md
└── requirements.txt

---

