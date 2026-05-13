import sqlite3
import os

db_path = "baseDatos/gestion.db"
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
for name, sql in cur.fetchall():
    print(f"Table: {name}")
    print(sql)
    print("-" * 20)
con.close()
