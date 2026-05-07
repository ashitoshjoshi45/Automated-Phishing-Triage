# ADDED ON 07-05-2026
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