import sqlite3
import datetime

# define local database fiel name
DB_NAME = 'local_threat_intel.db'

def initialize_database():
    """Creates the database and the honeypot_iocs table if they dont't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # use UNIQUE for indicator_value so we don't store duplicates
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS honeypot_iocs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            indicator_value TEXT UNIQUE NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("[+] Database initialized successfully.")

def insert_ioc(indicator):
    """Inserts a new IOC into the database, ignore duplicates."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()

    try:
        cursor.execute('''
            INSERT INTO honeypot_iocs (indicator_value, timestamp)
            VALUES (?, ?)
        ''', (indicator, timestamp))
        conn.commit()
        #Return TRUE is successfully added
        result = True
    
    except sqlite3.IntegrityError:
        # triggers if the indicator exists in preior due to the UNIQUE constrains
        result = False

    conn.close()
    return result

def check_email_against_db(email_iocs):
    """Checks a list of extracted email IOCs against the database in a single query."""
    if not email_iocs:
        return []

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create placeholders (?, ?, ?) for the number of IOCs provided
    placeholders = ', '.join(['?'] * len(email_iocs))
    query = f'SELECT indicator_value FROM honeypot_iocs WHERE indicator_value IN ({placeholders})'

    try:
        cursor.execute(query, email_iocs)
        # fetchall() returns a list of tuples like [('1.1.1.1',), ('malicious.com',)]
        results = cursor.fetchall()
        
        # Flatten the list of tuples into a simple list of strings
        confirmed_threats = [row[0] for row in results]
        
    except sqlite3.Error as e:
        print(f"[-] Database error: {e}")
        confirmed_threats = []
    finally:
        conn.close()

    return confirmed_threats

