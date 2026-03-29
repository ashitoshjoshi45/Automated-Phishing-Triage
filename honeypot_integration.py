# Import the new data
import re
import data_base_manager

def extract_iocs(text):
    """
    Extract IP addresses from log entries or email bodies
    """

    iocs = []
    #Basic regex for extracting IPv4 addresses.
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)
    iocs.extend(ips)
    return iocs

def ingest_honeypot_data(honeypot_logs):
    """
    Parses logs from the honeypot to extract malicious indicators and 
    adds them to our persistent local database.
    """ 
    new_threats_added = 0 

    for log in honeypot_logs:
        extracted_iocs = extracted_iocs(log)
        for ioc in extracted_iocs:
            # insert_ioc returns True if it's a new entry,  False if it's a duplicate
            if data_base_manager.insert_ioc(ioc):
                new_threats_added += 1

    return f"[+] Integration complete. {new_threats_added} new unique threats added to the database."

def triage_email(email_content):
    """
    Analyzes an incoming phishing email and compares its indicators
    against the data captured by the honeypots in our database. 
    """
    email_indicators = extract_iocs(email_content)

    # Check the extractedd email IOC's against our SQLite database
    confirmed_threats = data_base_manager.check_email_against_db(email_indicators)

    if confirmed_threats:
        return f"[CRITICAL] Threat matched with honeypot data! Known IOCs found: {confirmed_threats}"
    
    return "[INFO] Standard scan complete. No honeypot overlap detected."