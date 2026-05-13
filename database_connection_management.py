#------ added on 13-05-2026 -------
#STEP 1 : Define a helper function to manage connection creation
#FUNCTION get_db_connection():
    #CREATE a connection to 'indicators.db'
    #SET the row factory to sqlite3.Row for better data handling
    #RETURN the connection

#STEP 2 : Modify process_email_data to use the new connection management
#FUNCTION process_email_data(email_packet):
    # TRY: 
        # Utilize a context manager (with statement) to ensure proper resource management
        # WITH get_db_connection() AS connection:
            # CREATE a cursor from the connection

            # Extract sender and score from the email_packet
            # sender = email_packet['sender']
            # score = email_packet['score']
            # timestamp = datetime.now().isoformat()

            # Execute the INSERT query to store triage results
            # query = "INSERT INTO triage_results (sender, score, timestamp) VALUES (?, ?, ?)"
            # WITH (sender, threat_score , timestamp)

            # The context manager will automatically commit the transaction and close the connection
            
            # EXCEPT sqlite3.Error AS e:
            # LOG the specific error message "Failed to write to the database: {e}"
            # SEND alert to alert_system.py
    
            #FINALLY:
            # The connection is closed automatically by the 'with' block
            # or explcitily here to ensure no locks remain on indicators.db
            # CLOSE connectino if still open