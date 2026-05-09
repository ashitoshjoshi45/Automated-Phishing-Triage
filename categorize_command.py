# ADDED ON 07-05-2026
# ADDED ON 09-05-2026
def categorize_command(command_string):
    # Iterate through the dictionary where:
    # Key = MITRE Technique (e.g., 'Execution (T1204)')
    # Value = List of keywords (e.g., ['chmod +', './'])
    
    MITRE_MAP = {
        'Resource Development (T1587)': ['curl -O', 'wget ', 'Invoke-WebRequest'],
        'Execution (T1204)': ['chmod +', './'],
        'Discovery (T1033)': ['whoami', 'uname'],
        'Impact (T1485)' : ['rm -rf /']
                              
    }

    # Outer-loop to iterate throygh each technique and its keyword list
    for technique, keywords in MITRE_MAP.items():
        pass
    
    # If the loop finishes without a match
    return "Unknown/General Activity"
#  FUNCTION categorize_command(command_string):
#     # Iterate through the dictionary where:
#     # Key = MITRE Technique (e.g., 'Execution (T1204)')
#     # Value = List of keywords (e.g., ['chmod +', './'])
    
#     FOR each TECHNIQUE and KEYWORDS in MITRE_MAP:
#         FOR each KEYWORD in KEYWORDS:
#             IF KEYWORD is present inside command_string:
#                 RETURN TECHNIQUE
    
#     # If the loop finishes without a match
#     RETURN "Unknown/General Activity"