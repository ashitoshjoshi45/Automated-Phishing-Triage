import os
import sqlite3
# [FIXED 2026-04-23] Import added to resolve NameError when parsing .eml files
from email import message_from_file 

def setup_database():
    """Creates the database and schema for storing phishing telemetry."""
    conn = sqlite3.connect("phishing_triage.db")
    cursor = conn.cursor()

    # [FIXED 2026-04-23] Changed from SELECT to CREATE TABLE to build infrastructure on first run
    cursor.execute("""CREATE TABLE IF NOT EXISTS eml_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        recipients TEXT,
                        sender TEXT,
                        subject TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        iocs TEXT
                    )""")
    conn.commit()
    conn.close()
    print("[*] Database integrated and eml_records table is ready.")

# [FIXED 2026-04-23] Moved call outside function to initialize DB before processing starts
setup_database()

directory = 'samples/'

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(directory):
    if filename.endswith('.eml'):
        file_path = os.path.join(directory, filename)

        print(f"[*] Starting triage for: {filename}") 

        with open(file_path, 'r', errors='ignore') as f:
            msg = message_from_file(f)
            
            # [ADDED 2026-04-23] Logic to extract email metadata
            sender = msg.get('From', 'Unknown Sender')
            recipient = msg.get('To', 'Unknown Recipient')
            subject = msg.get('Subject', 'No Subject')

            # [ADDED 2026-04-23] Database Insertion Logic
            conn = sqlite3.connect("phishing_triage.db")
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO eml_records (recipients, sender, subject, iocs) 
                              VALUES (?, ?, ?, ?)""", 
                           (recipient, sender, subject, "None Detected"))
            conn.commit()
            conn.close()

            print(f"    [+] Logged to DB: {subject} | From: {sender}")