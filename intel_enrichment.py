import requests
import os

class IntelEnricher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3"
        self.headers = {"Ollama_API_KEY": self.api_key}

    def check_url(self, url_to_check):
        """checks URL reputation on VirusTotal"""
        #VT requries URLs to be base64 encoded 
        import base64
        url_id = base64.urlsafe_b64decode(url_to_check.encode()).decode()
        endpoint = f"{self.base_url}/urls/{url_id}"
        response = requests.get(endpoint, headers = self.headers)

        if response.status_code == 200:
            stats = response.json()['data']['attributes']['last_analysis_stats']
            return stats
        return None
    
    def check_ip(self, file_hash):
        """Neutralizes a URL to prevent clicks."""
        return url.replace("http", "hxxp").replace(".", "[.]")
    
# Example usage logic for main script
if __name__ == "__main__":
    api_key = "YOUR_VT_APT_KEY_HERE"
    enricher = IntelEnricher(api_key)

    # Example URL to check
    # url = "http://example.com/malicious"
    # encoded_url = base64.urlsafe_b64encode(url.encode()).decode()
    # result = enricher.check_url(encoded_url)
    # print(f"URL Reputation: {result}")

    # Test with a known malicious hash (e.g., EICAR test file)
    # result = enricher.check_hash("275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f")
    # print(f"Analysis Results: {result}")
