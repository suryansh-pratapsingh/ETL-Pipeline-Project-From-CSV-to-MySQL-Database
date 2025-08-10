# main_etl.py
# Purpose: Orchestrate the entire ETL process.

import logging
from config import DB_CONFIG
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    """
    Main function to run the ETL pipeline.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("etl_run.log"), # Log to a file
            logging.StreamHandler()             # Log to the console
        ]
    )

    logging.info("=============================================")
    logging.info("========= Starting ETL Process =========")
    logging.info("=============================================")

    # Define file path and table name
    csv_file_path = 'source_data.csv'
    table_name = 'users'

    # --- Step 1: Extract ---
    raw_data = extract_data(csv_file_path)

    if raw_data is not None:
        # --- Step 2: Transform ---
        transformed_data = transform_data(raw_data)

        if transformed_data is not None:
            # --- Step 3: Load ---
            success = load_data(transformed_data, DB_CONFIG, table_name)
            if success:
                logging.info("ETL Process Completed Successfully.")
            else:
                logging.error("ETL Process Failed during the load phase.")
        else:
            logging.error("ETL Process Failed during the transform phase.")
    else:
        logging.error("ETL Process Failed during the extract phase.")

    logging.info("=============================================")
    logging.info("========== ETL Process Finished ==========")
    logging.info("=============================================")


if __name__ == '__main__':
    main()
