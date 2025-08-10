ETL Pipeline Project: From CSV to MySQL Database
Course: Data Engineering Fundamentals

Student: [Your Name Here]

Date: August 10, 2025

1. Project Overview
This project demonstrates a complete, automated ETL (Extract, Transform, Load) pipeline built with Python. The objective was to create a robust system that reads raw user data from a CSV file, cleans and transforms it into a usable format, and then loads it into a structured MySQL database.

The pipeline is designed to be modular, maintainable, and includes comprehensive logging for tracking and debugging purposes.

2. The ETL Process
The pipeline follows the standard three-stage ETL process:

[E]xtract: Data is read from the source source_data.csv file into a Pandas DataFrame. The script is designed to handle potential file errors gracefully.

[T]ransform: The raw data undergoes a series of cleaning and formatting operations:

Handling of missing values (e.g., filling total_orders with 0).

Correction of data types (e.g., converting date strings to datetime objects).

Standardization of string data (e.g., capitalizing names).

Validation of data integrity (e.g., removing records with invalid email addresses).

[L]oad: The cleaned, transformed data is loaded into a users table within a MySQL database. The script automatically creates the table based on the DataFrame's schema if it doesn't already exist, ensuring a seamless first-time setup.

3. Technology Stack
Language: Python 3

Core Libraries:

Pandas: For data manipulation and transformation.

SQLAlchemy: For robust and engine-agnostic database interaction.

mysql-connector-python: The specific database driver for connecting to MySQL.

Database: MySQL Server

Logging: Python's built-in logging module.

4. Project Structure
The project is organized into modular scripts for clarity and separation of concerns:

/ETL-Project/
├── source_data.csv     # The raw source data file.
├── config.py           # Stores database credentials (Excluded from version control).
├── extract.py          # Contains the data extraction logic.
├── transform.py        # Contains all data cleaning and transformation logic.
├── load.py             # Contains the logic for loading data into MySQL.
├── main_etl.py         # The main driver script that orchestrates the pipeline.
└── etl_run.log         # Log file generated after each run.

5. Setup and Execution Guide
Follow these steps to set up and run the ETL pipeline on a local machine.

Step 1: Prerequisites
Ensure you have Python and MySQL Server installed.

Step 2: Install Dependencies
Install the required Python libraries using pip:

pip install pandas sqlalchemy mysql-connector-python

Step 3: Database Setup
Connect to your MySQL instance and create the target database:

CREATE DATABASE etl_project;

Step 4: Configure Credentials
Open the config.py file and update the DB_CONFIG dictionary with your MySQL username and password.

# config.py
DB_CONFIG = {
    'user': 'your_mysql_user',      # <-- REPLACE
    'password': 'your_mysql_password', # <-- REPLACE
    'host': 'localhost',
    'database': 'etl_project'
}

Step 5: Run the Pipeline
Execute the main script from your terminal:

python main_etl.py

6. Results and Verification
Upon successful execution, the script will log its progress to both the console and the etl_run.log file.

Screenshot 1: Successful Console Output
The terminal output confirms that each stage of the ETL process completed without errors.

(Replace the block below with your actual screenshot)



Screenshot 2: Data Verification in Database
The cleaned data can be verified by connecting to the etl_project database and querying the users table. The table contains 9 rows of validated data, reflecting the transformations applied (e.g., no invalid emails, capitalized names).

(Replace the block below with your actual screenshot from DBeaver, MySQL Workbench, etc.)



This confirms the successful completion of the ETL pipeline, moving data from a raw source file to a clean, structured database table, ready for analysis.
