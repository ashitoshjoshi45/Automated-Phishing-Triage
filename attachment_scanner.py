#Added on 28-07-2026
# // title: attachment hash extraction and comparison
import hashlib
# class solution:
class solution:
#     def extract_and_compare_hashes(email_attachments, threat_database):
        def extract_and_compare_hashes(self, email_attachments, threat_database):
            flagged_list = []        
# // Initialize an empty list for flagged malicious hashes
#         // OUTER LOOP: For each attachment in email_attachments
            for attachment in email_attachments:
                content = attachment.get('content', b'')
                name = attachment.get('name', 'unknown_file')
#             // Compute the SHA-256 hash of the current attachment
                hasher = hashlib.sha256()
                hasher.update(content)
                file_hash = hasher.hexdigest()
#             
#              // INNER LOOP: For each known_malicious_hash in threat_database
                for known_hash in threat_database:
#                 // If the computed attachment hash matches the known_malicious_hash
                    if file_hash == known_hash:         
                # Add the matched hash and attachment name to the flagged list
                        flagged_list.append({"name": name, "hash": file_hash})
                        break
         # Return the flagged list
# end function
            return flagged_list

