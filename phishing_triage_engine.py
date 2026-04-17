import os

# Assuming 'samples/' is where you store .eml or .msg files
directory = 'samples/'

# Ensure the directory exists to avoide errors
if not os.path.exists(directory):
    os.makedirs(directory)

# outer loop to iterate through the email samples
for filename in os.listdir(directory):
    if filename.endswith('.eml'):
        file_path = os.path.join(directory, filename)

        # This is where we will call our triage function
        print(f"[*] Starting triage for: {filename}") 

        with open(file_path, 'r', errors='ignore') as f:
            msg = message_from_file(f)

        # placeholder for the inner logic we will write next
        # result = triage_email(file_path)
        

