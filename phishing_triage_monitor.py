import sqlite3
import time


# Opening the connection here is risky for long-running SOC scripts.
# If a crash happens, the 'indicators.db' might stay locked.
db_connection = sqlite3.connect('indicators.db')

def fetch_new_emails():
    """
    Simulates fetching new emails for triage.
    In a real scenario, this would poll an API or IMAP server.
    """
    return [
        {'sender': 'admin@secure-bank-update.com', 'score': 85},
        {'sender': 'colleague@company.com', 'score': 10}
    ]

def process_email_data(email):
    """
    Processes and logs triage results.
    ERROR: Uses the global connection without proper error handling or closing.
    """
    """ -----planned on 02-05-2026
    1. REMOVE the global 'db_connection' variable from the top of the script.
    2. DEFINE a new function 'get_connection()' that creates and returns a fresh connection.
    3. MODIFY 'process_email_data(email)':
        a. OPEN a connection using 'get_connection()'.
        b. USE a 'with' statement (Context Manager) for the connection.
        c. EXECUTE the INSERT query.
        d. Logic inside 'with' automatically commits and handles the cursor.
    4. MODIFY 'main_triage_loop()':
        a. REMOVE the 'db_connection.close()' from the 'finally' block as it's no longer global.
        b. ADD a 'try-except' block around the specific DB call to handle individual failures without crashing the whole loop.
        cursor = db_connection.cursor()
    """
    # Simple insertion logic
    query = "INSERT INTO triage_results (sender, score) VALUES (?, ?)"
    cursor.execute(query, (email['sender'], email['score']))
    
    # Commit changes
    db_connection.commit()
    print(f"[+] Triage result saved for: {email['sender']} (Score: {email['score']})")

def main_triage_loop():
    """
    Outer loop to continuously monitor for phishing threats.
    """
    print("[*] Automated Phishing Triage System Started...")
    print("[!] WARNING: Initializing with global DB connection...")

    try:
        while True:
            print("\n[*] Checking for new incoming emails...")
            new_emails = fetch_new_emails()

            if not new_emails:
                print("[-] No new items found. Sleeping...")
            else:
                print(f"[+] Found {len(new_emails)} items. Processing...")
                for email in new_emails:
                    process_email_data(email)

            # Polling interval
            time.sleep(10) 

    except KeyboardInterrupt:
        print("\n[!] System shutdown requested. Closing connection...")
        # If the script is killed here, it's usually fine, but if it 
        # crashes elsewhere, the DB lock persists.
        db_connection.close()

if __name__ == "__main__":
    main_triage_loop()