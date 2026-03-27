import re

class EmailTriage:
    def extract_iocs(self, email_raw_text):

        #LOGIC I used is:
        #1. used regular expressions to find IPv4 address
        #2. use Regex to find URL's and Domains
        #3. Store these in a 'results' dictionary
        #4. return dict for further threat intel enrichment

        iocs = {
            "ips": re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', email_raw_text),
            "urls": re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email_raw_text)

        }

        return iocs