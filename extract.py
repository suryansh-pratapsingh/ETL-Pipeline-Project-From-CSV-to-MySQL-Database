# extract.py
# Purpose: Read data from the source CSV file.

import pandas as pd
import logging

def extract_data(file_path):
    """
    Reads data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the CSV file,
                          or None if an error occurs.
    """
    logging.info(f"Starting data extraction from {file_path}...")
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        logging.info(f"Successfully extracted {len(df)} rows of data.")
        return df
    except FileNotFoundError:
        logging.error(f"Error: The file was not found at {file_path}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred during extraction: {e}")
        return None
