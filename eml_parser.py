import os 
import re
from email import policy
from email.parser import BytesParser

def triage_eml(file_path):
    if not os.path.exists(file_path):
        return {"error": f"File '{file_path}' not found."}

    try:
        with open(file_path, 'rb') as f:
            # BytesParser with policy.default is the safest way to handle malformed emails
            msg = BytesParser(policy=policy.default).parse(f)
    except Exception as e:
        return {"error": f"Failed to parse EML: {str(e)}"}
    
    # Initialize the triage report
    triage_report = {
        "metadata": {
            "subject": str(msg.get('subject', 'No Subject')),
            "from": str(msg.get('from', 'Unknown Sender')),
            "to": str(msg.get('to', 'Unknown Recipient')),
            "date": str(msg.get('date', 'Unknown Date')),
            # Fetch all 'Received' headers to track the email's origin path
            "hops": msg.get_all('received', [])
        },
        "urls": set(), # Using a set to avoid duplicate URLs
        "attachments": [],
        "body_text": ""
    }

    # --- INNER LOOP: Artifact Extraction ---
    for part in msg.walk():
        content_type = part.get_content_type()
        content_disposition = str(part.get("Content-Disposition", ""))

        # 1. Process Text/HTML for Body and URLs
        if content_type in ["text/plain", "text/html"]:
            try:
                content = part.get_content()
                if content_type == "text/plain":
                    triage_report["body_text"] += content

                # Regex to find URLs
                found_urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', content)
                triage_report["urls"].update(found_urls) # Adds only unique URLs
            except Exception:
                pass 

        # 2. Extract Attachment metadata
        elif "attachment" in content_disposition or part.get_filename():
            filename = part.get_filename()
            if filename:
                triage_report["attachments"].append(filename)

    # Convert set back to list for JSON compatibility
    triage_report["urls"] = list(triage_report["urls"])
    return triage_report

# Example for your local testing before pushing:
# print(triage_eml("sample_phish.eml"))