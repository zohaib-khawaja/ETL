import logging
import os
from extract import extract_data
from transform import transform_data
from load import load_data

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can use os.getenv('VARIABLE_NAME') to access your environment variables
database_uri = os.getenv('DATABASE_URI')
table_name = os.getenv('TABLE_NAME')


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting ETL process")

    # Extract phase
    extracted_data = extract_data('https://jsonplaceholder.typicode.com/posts')
    
    # Transform phase
    transformed_data = transform_data(extracted_data)
    
    # Load phase
    database_uri = os.getenv('DATABASE_URI', 'your_default_database_connection_uri')
    table_name = os.getenv('TABLE_NAME', 'your_default_target_table')
    load_data(transformed_data, database_uri, table_name)

    logging.info("ETL process completed successfully")

if __name__ == '__main__':
    main()