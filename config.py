# config.py
# Purpose: Store database credentials securely.
# NEVER commit this file to a public repository.

DB_CONFIG = {
    'user': 'root',      # <-- REPLACE with your MySQL username
    'password': 'w', # <-- REPLACE with your MySQL password
    'host': 'localhost',           # <-- REPLACE with your MySQL host if not local
    'database': 'etl_project'      # The database name we'll be using
}
