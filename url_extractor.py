import re

def extract_urls(email_text: str):
    """
    Scans raw email text and extracts all HTTP/HTTPS URL's.
    Useful for identifying mailicious links in potential phishing
    email.
    """

    #Regex pattern to match http and https URLs
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*'

    found_urls = re.findall(url_pattern, email_text)

if __name__ ==  "__main__":
    #sample suspicious email body
    sample_text = """
    URGENT : Your account will be suspended in 24 hours.
    Please verify your credentials immediately at:
    http://secure-update-login-alert.com/auth
    
    If you needd help, visit our support page:
    https://support.billing-services.net/help
    """

    print("Scanning email body for URL's...\n")
    urls = extract_urls(sample_text)

    if urls:
        print("Etractred URL's for Threat Intelligence Analysis:")
        for u in urls:
            print(f"[+] {u}")
    else:
        print("No URL's found in the email.")