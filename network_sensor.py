class solution:
    def triage_phishing_ips(self, email_metadata, watchlist_ips):
        # Initialize an empty list for flagged emails
        # added on 04-08-2026
        flagged_emails = []

        # convert list to set for O(1) time complexity lookup
        watchlist_set = set(watchlist_ips)

        # OUTER LOOP: For each parsed email artifact in email_metadata
        for email in email_metadata:
            # Extract sender_ip and reply_to_ip from the email artifact
            sender_ip = email.get('sender_ip')
            reply_to_ip = email.get('reply_to_ip')
            
            # Optimized O(1) lookup against the watchlist set
            if sender_ip in watchlist_set or reply_to_ip in watchlist_set:
                # Add the email to the flagged list
                flagged_emails.append(email)
                
        # Return the flagged emails list
        return flagged_emails