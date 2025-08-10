# load.py
# Purpose: Load the transformed data into a MySQL database.

import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def load_data(df, db_config, table_name='users'):
    """
    Loads a DataFrame into a specified MySQL table.
    The table is created if it does not exist.

    Args:
        df (pandas.DataFrame): The DataFrame to load.
        db_config (dict): A dictionary with database connection details.
        table_name (str): The name of the target table.

    Returns:
        bool: True if the load was successful, False otherwise.
    """
    if df is None:
        logging.error("Input DataFrame is None. Cannot load data.")
        return False

    logging.info(f"Starting to load data into MySQL table '{table_name}'...")

    try:
        # Create a connection string for SQLAlchemy
        connection_string = (
            f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}"
            f"@{db_config['host']}/{db_config['database']}"
        )
        engine = create_engine(connection_string)

        # Load the DataFrame into the SQL table
        # 'if_exists='replace'' will drop the table first and then create a new one.
        # Use 'append' if you want to add data to an existing table.
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        logging.info(f"Successfully loaded {len(df)} rows into '{table_name}'.")
        return True

    except SQLAlchemyError as e:
        logging.error(f"An error occurred with the database connection or query: {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred during the load process: {e}")
        return False
