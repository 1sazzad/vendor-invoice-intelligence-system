import os
import sqlite3

db_path = "data/inventory.db"   # update path if file is inside data folder

# Check DB file size
size_mb = os.path.getsize(db_path) / (1024 * 1024)
print(f"Database Size: {size_mb:.2f} MB")

# Connect database
conn = sqlite3.connect(db_path)

# Get all tables
tables = conn.execute("""
SELECT name 
FROM sqlite_master 
WHERE type='table';
""").fetchall()

print("\nTables:")
print(tables)

# Count rows
print("\nRow Counts:")
for table in tables:
    table_name = table[0]
    count = conn.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    ).fetchone()[0]

    print(f"{table_name}: {count:,} rows")

conn.close()