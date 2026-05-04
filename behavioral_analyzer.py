#Define a dictionary "MITRE_MAP" where:
""" 'wget', 'curl' -> 'Resource Devlopment' (T1588)
    'chmod +', './' -> 'Execution' (T1204)
    'whoami', 'uname' -> 'Discovery' (T1033)
    'rm -rf /' -> 'Impact' (T1485) 
    """

# Define function categorize_command(command_string):
#   LOOP through keywords in MITER_MAP:
#     IF any keyword is in command_string:
#       RETURN the corresponding MITRE technique