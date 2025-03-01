import sqlite3

DATABASE = 'database.db'

def create_Cars_table():
    con = sqlite3.connect(DATABASE)
    con.execute("DROP TABLE IF EXISTS Cars")
    con.execute("""
    CREATE TABLE IF NOT EXISTS Cars (
        "Registration Number" INTEGER PRIMARY KEY AUTOINCREMENT,  -- 自動インクリメントを適用
        Brand TEXT,
        Model TEXT,
        Color TEXT,
        "Contact Information" TEXT,
        "Vehicle ID Number" TEXT
    )
    """)
    con.close()
