def flag_vt_iocs(vt_results, malicious_threshold=2):
    """
    this parese VirusTotal API v3 responses and flags IOCs as malicious if they have more than the specified number of malicious detections.
    
    Args: 
        vt_results (dict): A dictionary containing the VirusTotal API v3 response for an IOC.
        malicious_threshold (int): The number of malicious detections required to flag an IOC as malicious. Default is 2.
    

    Returns:
        list: A list of IOCs that are flagged as malicious based on the specified threshold.
    """
    flagged_iocs = []

    for ioc_value, vt_data in vt_results.items():
        try:
            #navigate the VT v3 JSON structure to get the vendor consensus
            attributes = vt_data.get('data', {}).get('attributes', {})
            stats = attributes.get('last_analysis_stats', {})

            malicious_count = stats.get('malicious', 0)
            suspicious_count = stats.get('suspicious', 0)

            #Evaluate agaist the threshold
            if malicious_count >= malicious_threshold:
                flagged_iocs.append({
                    'ioc': ioc_value,
                    'type':attributes.get('type', 'unknown'), #hash, domain, ip_address
                    'malicious_count': malicious_count,
                    'suspicious_count': suspicious_count,
                    'reason': f"Crossed threshold: {malicious_count} vendors flagged as malicious."
                })
        
        except AttributeError:
            print(f"[!] Error parsing VT response structure for IOC: {IOC_VALUE}")
            continue

    return flagged_iocs
# Simulating the raw JSON responses gathered in Phase 3.2 
vt_api_responses = {
    "103.15.22.1":{
        "data": {"attributes" :{"type": "ip_address", "last_analysis_stats": {"malicious": 5, "suspicious": 1, "harmless": 60}}}
    },
    "https://secure-login-update.com":{
        "data":{"attributes": {"type": "url", "last_analysis_stats":{"malicious": 1, "suspicious": 2, "harmless": 80}}}

    },
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": {
        "data": {"attributes": {"type": "file", "last_analysis_stats": {"malicious": 0, "suspicious": 0, "harmless": 70}}}  
    }
}

# Run the triage
actionable_iocs = flag_vt_iocs(vt_api_responses, malicious_threshold=2)

print("🚨 FLAGGED IOCs FOR SOC REVIEW 🚨")
for ioc in actionable_iocs:
    print(f"- [{ioc['type'].upper()}] {ioc['ioc']} | {ioc['reason']}")