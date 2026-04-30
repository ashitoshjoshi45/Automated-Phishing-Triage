# IOC Neutralization Logic
# Goal: Prevent accidental execution of malicious links in SOC reports.

DEFINE function 'defang_url' (input_string):
    1. SEARCH for "http" and REPLACE with "hxxp"
    2. SEARCH for "https" and REPLACE with "hxxps"
    3. SEARCH for all periods "." and REPLACE with "[.]"
    4. RETURN the modified string