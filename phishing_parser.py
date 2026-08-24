# added on 18-08-2026

import email
from email import policy
import re
#function parse_phishing_email(eml_file_path)
def parse_phishing_email(eml_file_path):
#   initialize artifacts dictionary to store sender, subject, and urls
    artifacts = {
        "sender": None,
        "subject" : None,
        "urls": []
    }
  # open the eml_file_path and parse the email content
  # extract the "From" and "Subject" fields
    try:
        with open(eml_file_path, 'r') as f:
            msg = email.message_from_file(f, policy=policy.default)
            artifacts["sender"] = msg.get("From")
            artifacts["subject"] = msg.get("Subject")
  # check if the email contains multiple parts
        if msg.is_multipart():
            body = ""
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type in ["text/plain", "text/html"]:
                    body += part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='replace')
  # Added om 24-08-2026
  # outer loop: iterate through each part of the email
            for part in msg.walk():
       
        #    inner loop / condition: if the part is text/plain or text/html
                if part.get_content_type() in ["text/plain", "text/html"]:
#       append the content to our main body string
                    charset = part.get_content_charset() or 'utf-8'
                    body += part.get_payload(decode=True).decode(charset, errors='replace')

    # use regular expressions to find all URLs in the extracted body
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s"\'<>]*')
    artifacts["urls"] = list(set(re.findall(url_pattern, body)))
  
  # return the dictionary of extracted artifacts
    return artifacts
# end function

# added on 16-08-2026

# function triage_phishing_artifacts(artifacts)
#   initialize risk_score to 0
#   initialize analysis_report dictionary to store findings and final action
#
#   # 1. Analyze Sender Domain
#   extract domain from artifacts["sender"]
#   query domain_reputation_api(domain) # e.g., check age, SPF/DKIM records, threat intel
#   if domain is newly registered OR has known bad reputation:
#       increase risk_score by 30
#       append "Suspicious Sender Domain" to analysis_report["findings"]
#
#   # 2. Analyze Extracted URLs
#   for each url in artifacts["urls"]:
#       query threat_intel_api(url) # e.g., VirusTotal, URLScan.io
#       if api_response flags url as malicious or phishing:
#           increase risk_score by 50
#           append "Malicious URL Detected" to analysis_report["findings"]
#           break loop # early exit if we already have a critical hit
#       else if api_response shows suspicious redirects:
#           increase risk_score by 20
#           append "Suspicious URL Redirect" to analysis_report["findings"]
#
#   # 3. Determine Triage Action based on score thresholds
#   if risk_score >= 50:
#       set analysis_report["action"] = "Quarantine Email & Alert SOC"
#       set analysis_report["severity"] = "High"
#   else if risk_score >= 20:
#       set analysis_report["action"] = "Flag for Manual Analyst Review"
#       set analysis_report["severity"] = "Medium"
#   else:
#       set analysis_report["action"] = "Close as False Positive"
#       set analysis_report["severity"] = "Low"
#
#   return analysis_report
# end function