#This is the old code for reference if needed. The new code is at thr bottm of this file.

# import requests
# import os

# class IntelEnricher:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.base_url = "https://www.virustotal.com/api/v3"
#         self.headers = {"Ollama_API_KEY": self.api_key}

#     def check_url(self, url_to_check):
#         """checks URL reputation on VirusTotal"""
#         #VT requries URLs to be base64 encoded 
#         import base64
#         url_id = base64.urlsafe_b64decode(url_to_check.encode()).decode()
#         endpoint = f"{self.base_url}/urls/{url_id}"
#         response = requests.get(endpoint, headers = self.headers)

#         if response.status_code == 200:
#             stats = response.json()['data']['attributes']['last_analysis_stats']
#             return stats
#         return None
    
#     def check_ip(self, file_hash):
#         """Neutralizes a URL to prevent clicks."""
#         return url.replace("http", "hxxp").replace(".", "[.]")
    
# # Example usage logic for main script
# if __name__ == "__main__":
#     api_key = "YOUR_VT_APT_KEY_HERE"
#     enricher = IntelEnricher(api_key)

#     # Example URL to check
#     # url = "http://example.com/malicious"
#     # encoded_url = base64.urlsafe_b64encode(url.encode()).decode()
#     # result = enricher.check_url(encoded_url)
#     # print(f"URL Reputation: {result}")

#     # Test with a known malicious hash (e.g., EICAR test file)
#     # result = enricher.check_hash("275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f")
#     # print(f"Analysis Results: {result}")


import os
import requests
import base64
from dotenv import load_dotenv

# 1. Securely load environment variables from the .env file
load_dotenv()

class IntelEnricher:
    def __init__(self):
        # 2. Fetch the API key securely. No more hardcoded keys!
        self.api_key = os.getenv("VT_API_KEY")
        if not self.api_key:
            raise ValueError("🚨 VT_API_KEY is missing! Please check your .env file.")
        
        self.base_url = "https://www.virustotal.com/api/v3"
        # FIX: VirusTotal strictly requires 'x-apikey' as the header name
        self.headers = {
            "accept": "application/json",
            "x-apikey": self.api_key
        }

    def check_ip(self, ip_address):
        """Queries VirusTotal for IP address reputation."""
        print(f"🔍 [INTEL] Scanning IP: {ip_address}...")
        endpoint = f"{self.base_url}/ip_addresses/{ip_address}"
        
        response = requests.get(endpoint, headers=self.headers)
        
        if response.status_code == 200:
            # Safely navigate the JSON response using .get()
            return response.json().get('data', {}).get('attributes', {}).get('last_analysis_stats')
        else:
            return f"Error: Received status code {response.status_code}"

    def check_url(self, url_to_check):
        """Checks URL reputation on VirusTotal."""
        print(f"🔍 [INTEL] Scanning URL: {url_to_check}...")
        # VT requires URLs to be base64 encoded without padding
        url_id = base64.urlsafe_b64encode(url_to_check.encode()).decode().strip("=")
        endpoint = f"{self.base_url}/urls/{url_id}"
        
        response = requests.get(endpoint, headers=self.headers)
        
        if response.status_code == 200:
            return response.json().get('data', {}).get('attributes', {}).get('last_analysis_stats')
        else:
            return f"Error: Received status code {response.status_code}"

    def defang_ioc(self, ioc):
        """Neutralizes a URL or IP to prevent accidental clicks in the final report."""
        return ioc.replace("http", "hxxp").replace(".", "[.]")

    def check_vt_threshold(vt_results, threshold=5):
        """
        Analyzes VT results and flags IOC's above the malicious threshold.
        """

        malicious_count = vt_results.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious', 0)

        if malicious_count >= threshold:
            return{
                "is_flagged" : True,
                "severity" : "CRITICAL" if malicious_count > 10 else "HIGH",
                "count" : malicious_count,
                "message": f"IOC flagged: {malicious_count} engines detected this as malicious."
            }
        
        return {"is_flagged": False, "count": malicious_count, "message": f"IOC is clean: {malicious_count} engines detected this as malicious."}
# Test logic to ensure it runs correctly
if __name__ == "__main__":
    enricher = IntelEnricher()
    
    # Let's test it with Google's public DNS IP
    test_ip = "8.8.8.8"
    result = enricher.check_ip(test_ip)
    
    print(f"\n📊 Results for {test_ip}:")
    print(result)