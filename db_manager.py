import sqlite3
import datetime

def initialize_db(db_path="honeypot_iocs.db"):
    # Connect to the SQLite database (creates it if it doesn't exist)
    # Create a cursor object
    # Execute SQL to create an 'iocs' table if it doesn't exist
    # make table which has coloumns named : id (primary_key), indicatro(text)
    pass

#now inserting the and connecting to the batabase
def insert_ioc(indicator: str, ioc_type: str, db_path="honeypot_iocs.db"):
    #connect to db
    #get the current timestamp
    #Execute SQL INSERT statement to add indicator, ioc_type, time_stamp
    pass

def check_ioc_exists(indicator: str, db_path="honeypot_iocs.db"):
    #connect to bd
    #create a cursor object
    #execute SQL SELECT to search specific indicator in the column "indicator"
    #return TRUE if a record is found , else FALSE 
    pass