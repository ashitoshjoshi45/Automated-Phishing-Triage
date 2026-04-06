# FUNCTION generate_blast_radius_report():
#     1. CONNECT to the local SQLite database.
#     2. QUERY all extracted IOC's (IP's, Hashes, Senders) from the recent .eml ingestion.
#     3. IDENTIFY "Patient Zero":
#         a. Sort all email records by 'timestamp' in ascending order.
#         b. The first recipitent of the earliest detected malicious email in marked as Patient Zero.
#     4. CALCULATE "Full Scope":
#         a. Count unique recipitents affected by the same IOC's (eg. , same Phishing URL or Sender).
#         b. Group commonalities (e.g., "5 users recieved emails from the same malicious IP found in Honeypot logs").
#     5. DATA AGGREGATION:
#         a. Create a list of all internal endpoints/users reached.
#         b. Map the correlation between Honeypot triggers and user inboxes.
#     6. OUTPUT:
#         a. Print or save a summary report (JSON or Markdown) detailing the Timeline and Scope.
#     7. CLOSE database connection. 