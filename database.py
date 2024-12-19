# database.py
import sqlite3

def initialize_db(db_file, table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create the table if it doesn't already exist
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT,
            schedule TEXT,
            subreddit TEXT,
            title TEXT,
            url TEXT,
            timestamp REAL
        )
        """)

        # Commit changes and close the connection
        conn.commit()
        print(f"Table '{table_name}' created or already exists.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Close the database connection
        conn.close()
