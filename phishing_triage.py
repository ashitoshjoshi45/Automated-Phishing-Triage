#added-on 11-08-2026
import re

class Solution:
    IP_PATTERN = re.compile(r"(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))")
  
#   if length of url is greater than 75 then
#     return "[HIGH RISK]: URL length exceeds safety threshold."
    def analyze_phishing_url(self, url:str) -> str:
        if len(url) > 75:
            return "[HIGH RISK]: URL length exceeds safety threshold."
        
#   else if url matches ip_pattern then
#     return "[HIGH RISK]: URL uses raw IP address."
        elif self.IP_PATTERN.search(url):
            return "[HIGH RISK]: URL uses raw IP address." 

#   else if url contains "@" symbol then
#     return "[MEDIUM RISK]: URL contains '@' symbol."
        elif '@' in url:
            return "[MEDIUM RISK]: URL contains '@' symbol."
#   else
#     return "[LOW RISK]: No obvious static indicators found."
        else:
            return "[LOW RISK]: No obvious static indicators found."
# Eample
analyzer =  Solution()
print(analyzer.analyze_phishing_url("http://192.168.1.1/login"))