import sqlite3
# Add the name of your database inside the quotes
conn = sqlite3.connect('people.db')
cursor = conn.cursor()
### Add SQL to define your table inside the quotes below
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
               user_id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               password INTEGER NOT NULL,
               auth_level INTEGER NOT NULL)
                ''')
conn.commit()
conn.close()
# Add the name of your database in the quotes below
print("Database 'people.db' created successfully.")