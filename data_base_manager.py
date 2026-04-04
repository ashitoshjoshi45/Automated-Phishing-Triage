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
    """Checks a list of etractedd email IOC's against the persistent database in a single query."""
    if not email_iocs:
        return[]
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    #create placeholder (? , ? , ?) for the number of IOC's provided
    placeholders = ', '.join(['?'] * len(email_iocs))
    query = f'SELECT indicator_value FROM honeypot_iocs WHERE indicator_value IN ({placeholders})'


    try:
        cursor.execute(query, email_iocs)
        #fetchall() returns a list of tuples like[('1.1.1.1',), ('malicious.com',)]
        results = cursor.fetchall()

    for ioc in email_iocs:
        cursor.execute('SELECT indicator_value FROM honeypot_iocs WHERE indicator_value = ?', (ioc,))
        match = cursor.fetchone()
        if match:
            #match[0] contains the actual string from the database
            confirmed_threats.append(match[0])

    conn.close()
    return confirmed_threats

# this is to ensure the DB exists
initialize_database() 