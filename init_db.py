import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()
    
    # Create the Cars table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Customer TEXT NOT NULL,
            Color TEXT NOT NULL,
            Brand TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized and Cars table created.")
