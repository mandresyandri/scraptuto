import sqlite3
def create_models():
    conn = sqlite3.connect('data-scrap.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scraped_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
        title TEXT, 
        date TEXT,
        lieu TEXT
    )
    """)
    conn.commit()
    return "Data créée"

create_models()