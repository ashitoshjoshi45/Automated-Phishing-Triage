import sqlite3
from datetime import datetime
from collections import defaultdict

class CorrelationEngine:
    def __init__(self, db_path="threat_intel.db"):
        self.db_path = db_path
        self.indicator_registry = defaultdict(list)
        self.campaigns = []

    def load_extracted_data(self):
        """
        Fetches all processed email metadata from the persistent SQLite DB.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Pulling data extracted from .eml files in previous steps
        cursor.execute("SELECT id, sender, source_ip, attachment_hash, timestamp, recipient FROM processed_emails")
        data = cursor.fetchall()
        conn.close()
        return data

    def run_correlation(self):
        """
        Main execution loop to identify campaign links and blast radius.
        """
        records = self.load_extracted_data()
        
        # Inner Loop: Building the registry of indicators
        for row in records:
            # We correlate based on IP and Attachment Hash
            indicators = [row['source_ip'], row['attachment_hash']]
            for indicator in indicators:
                if indicator:
                    self.indicator_registry[indicator].append(dict(row))

        self._generate_report()

    def _generate_report(self):
        """
        Analyzes the registry to find clusters and Patient Zero.
        """
        print(f"{'='*60}")
        print(f"INTERNAL THREAT INTEL: BLAST RADIUS REPORT")
        print(f"{'='*60}\n")

        processed_ids = set()

        for indicator, emails in self.indicator_registry.items():
            if len(emails) > 1:
                # Identify Patient Zero (Earliest Timestamp)
                emails.sort(key=lambda x: x['timestamp'])
                patient_zero = emails[0]
                
                # Calculate Blast Radius
                recipients = {e['recipient'] for e in emails}
                campaign_id = f"CMP-{indicator[:8]}"

                print(f"Campaign Detected: {campaign_id}")
                print(f"  - Correlation Factor: {indicator}")
                print(f"  - Patient Zero: {patient_zero['recipient']} (at {patient_zero['timestamp']})")
                print(f"  - Blast Radius: {len(recipients)} unique internal targets")
                print(f"  - Targets: {', '.join(recipients)}")
                print("-" * 30)

if __name__ == "__main__":
    engine = CorrelationEngine()
    engine.run_correlation()