import sqlite3
import json
from datetime import datetime


# FUNCTION generate_blast_radius_report():
def generate_blast_radius_report(db_path="phishing_triage.db"):
#     1. CONNECT to the local SQLite database.
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()  
#     2. QUERY all extracted IOC's (IP's, Hashes, Senders) from the recent .eml ingestion.
        cursor.execute("""
            SELECT recipients, sender, subject, timestamp, iocs
            FROM emil_records
            WHERE timestamp >= datetime('now', '-7 days')  -- Adjust time frame as needed
#       """)   
        malicious_emails = cursor.fetchall()

        if not malicious_emails:
            print("[*] No recent malicious emails found in the database.")
            return

        # 3. IDENTIRY "Patient Zero"
        # Since we sorted by timestamp ASC, The first record id Patient Zero
        p_zero = malicious_emails[0]
        parient_zero = {
              "email": p_zero_record['recipient'],
              "timestamp": p_zero_record['timestamp'],
              "initial_vector": p_zero_record['iocs_value']
        }

        # 4. calculate "Full Scope"
        affected_users = set()
        ioc_spread = {}

        for event in malicious_events:
                affected_users.add(event['recipient'])

                # Track IOC spread
                ioc = event['ioc_value']
                if ioc not in ioc_spread:
                    ioc_spread[ioc] = []
                ioc_spread[ioc].append(event['recipient'])

        # 5. DATA AGGREGATION
        report = {
              "report_generated_at": datetime.now().isoformat(),
              "summary":{
                        "total_malicious_emails": len(malicious_emails),
                        "total_affected_users": len(affected_users),
                        "patient_zero": patient_zero
                },
                "affected_users": list(affected_users),
                "ioc_correlation_map": ioc_spread
        }
        #6. OUTPUT
        # saving as a JSON report for the AI SOC Analyst to review
        with open(report_filename, 'w') as f: 
                json.dump(report, f, indent=4)

        print(f"Report generated and saved as {report_filename}")

        #7. CLOSE database connection
        conn.close()


if __name__ == "__main__":
    generate_blast_radius_report()