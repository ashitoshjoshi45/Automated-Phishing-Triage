import email
from email import policy
from email.parser import BytesParser
import re
import hashlib

def parse_email(file_path):
    with open(file_path, 'rb') as f:
        #use policy.default to handle modern email formatting easily
        msg = BytesParser(policy=policy.default).parse(f)

    # 1. Extract Basic Headers
    report = {
        "from" : msg['from'],
        "to" : msg['to'],
        "subject" : msg['subject'],
        "date" : msg['date'],
        "return_path" : msg['return_path'],
        "urls" : [],
        "ips" : [],
        "attachments" : []
    } 

    # 2. Extract the body and URL's
    body_part = msg.get_body(prefencelist=('plain', 'html'))
    body = body_part.get_content() if body_part else ""

    # improved Regex to find URL's on 16-03-2026 @ 17:51
    url_pattern = r'http?://[^\s<>"]+|www\.[^\s<>"]+'
    report["urls"] = list(set(re.findall(url_pattern, body)))

    # regex for IP addresses (Extracted from Received headers)
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    received_headers = msg.get_all('received', [])
    for header in received_headers:
        found_ips = re.findall(ip_pattern, str(header))
        report["ips"].extend(found_ips)

    #clean up duplicate IP'S
    report["ips"] = list(set(report["ips"]))
    
    # 3. Extract Attachment Metadata
    for part in msg.iter_attachments():
        filename = part.get_filename()
        if filename:
            file_data = part.get_payload(decode=True) # Ensure we get r
            file_hash = hashlib.sha256(file_data).hexdigest()
            report["attachments"].append({
                "filename": filename,
                "sha256" : file_hash
            }) 

    return report

# ----TEST execution -----
# result = parse_email('suspicious_email.eml')
# print(result)
#   result = parese_email('suspicious_email.eml')
#   import json
#   print(json.dumps(result, indent = 4))