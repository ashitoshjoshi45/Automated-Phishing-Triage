import os
import json
from datetime import datetime 
# I used oletools as it's th eindustry standard for soc analysis
from oletools.olevba import VBA_Parser

def analyze_attachment(file_path):
    
    # Attempts to extract VBA macro source code from a given file and analyze it for potential malicious behavior.
    
    if not os.path.exists(file_path):
        print(f"[!] File not found: {file_path}")
        return None
     
    # Step 1: parse the file for OLE streams.
    try:
        parser = VBA_Parser(file_path)
        filename = os.path.basename(file_path)
        
        if parser.detect_macros():
            print(f"[+] Macros detected in {os.path.basename(file_path)}")
            results = parser.analyze_macros()

            findings = []
            if results:
                for kw_type, keword, description in results:
                    findings.append({
                        "type": kw_type,
                        "keyword": keyword,
                        "description": description
                    })

            # structure data and export to JSON 
            report_data = {
                "file_name": filename,
                "analysis_time": datetime.now().strformat("%Y-%m-%d %H:%M:%S"),
                "macros_found" : True,
                "suspicious_counts": len(findings),
                "findings": findings
            }

            if export_json:
                json_file = f"reports/{filename}_analysis.json"
                os.makedirs("reports", exist_ok=True)
                with open(son_file, 'w') as jf:
                    json.dump(report_data, jf, indent = 4)
                print(f"[#] Analysis report saved to {json_file}")

            parser.close()
            return report_data

    # Step 2: Detect if VBA Macros are embedded.
        else:
            print(f"[-] No macros found in {os.path.basename(file_path)}")
            return None
    
    except Exception as e:
        print(f"[!] Error Parsing file: {e}")
        return None
    """
    step 3. Ectrect code and check for suspecious API calls(Run, Shell, etc)
    Step 4: Return the result of the analysis.
    """
if __name__ == "__main__":
    # Example usage
    sample_file = 'samples/suspicious_attachment.docm'  # Replace with your actual file path
    analyze_attachment(sample_file)