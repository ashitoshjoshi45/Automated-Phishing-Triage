import os
import sqlite3
import logging
import alert_system 
from email import message_from_file 

# [ADDRESSED ON 2026-04-27] Configure error logging to a local file
logging.basicConfig(
    filename='triage_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_database():
    """Creates the database and schema for storing phishing telemetry."""
    conn = sqlite3.connect("phishing_triage.db")
    cursor = conn.cursor()

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
            
            sender = msg.get('From', 'Unknown Sender')
            recipient = msg.get('To', 'Unknown Recipient')
            subject = msg.get('Subject', 'No Subject')

            # Database Insertion
            conn = sqlite3.connect("phishing_triage.db")
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO eml_records (recipients, sender, subject, iocs) 
                              VALUES (?, ?, ?, ?)""", 
                           (recipient, sender, subject, "None Detected"))
            conn.commit()
            conn.close()

            # [UPDATED 2026-06-07] Trigger risk-based alerting via alert_system module
            alert_system.alert_dispatcher(subject, "email", 1)

            print(f"    [+] Logged to DB: {subject} | From: {sender}")