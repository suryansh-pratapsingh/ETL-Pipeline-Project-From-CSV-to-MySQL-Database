# transform.py
# Purpose: Clean, format, and prepare the data for loading.

import pandas as pd
import logging

def transform_data(df):
    """
    Transforms the raw data by cleaning and formatting it.

    Args:
        df (pandas.DataFrame): The input DataFrame to be transformed.

    Returns:
        pandas.DataFrame: The transformed and cleaned DataFrame.
    """
    if df is None:
        logging.warning("Input DataFrame is None. Skipping transformation.")
        return None

    logging.info("Starting data transformation...")

    # 1. Handle missing values
    # Fill missing 'total_orders' with 0 and convert to integer
    df['total_orders'] = df['total_orders'].fillna(0).astype(int)
    # Drop rows where 'email_address' is missing
    df.dropna(subset=['email_address'], inplace=True)
    logging.info("Handled missing values.")

    # 2. Correct data formats
    # Convert date columns to datetime objects
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['last_login_date'] = pd.to_datetime(df['last_login_date'])
    logging.info("Converted date columns to datetime format.")

    # 3. Clean string data
    # Capitalize the 'full_name'
    df['full_name'] = df['full_name'].str.title()
    logging.info("Formatted 'full_name' to title case.")

    # 4. Validate data
    # Remove rows with invalid email addresses
    initial_rows = len(df)
    df = df[df['email_address'].str.contains('@', na=False)]
    rows_removed = initial_rows - len(df)
    if rows_removed > 0:
        logging.warning(f"Removed {rows_removed} rows with invalid email addresses.")

    # 5. Reset index after dropping rows
    df.reset_index(drop=True, inplace=True)

    logging.info(f"Data transformation complete. Final dataset has {len(df)} rows.")
    return df
