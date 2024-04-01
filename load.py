import logging
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Replace the DATABASE_URI and TABLE_NAME with your actual database URI and table name when
# using this script in your ETL process. Also, ensure your database and table are correctly
# set up to accept the data structure you're loading.


def load_data(transformed_data, database_uri, table_name):
    """
    Loads the transformed data into the specified database table.

    :param transformed_data: DataFrame containing the data to load
    :param database_uri: Database connection URI string
    :param table_name: Name of the table to load data into
    """
    logging.info("Starting data load process")

    # Create database engine
    engine = create_engine(database_uri)

    # Load data into the database
    try:
        transformed_data.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        logging.info("Data loaded successfully into the database")
    except Exception as e:
        logging.error(f"Error loading data into the database: {e}")
        raise e

# Example usage
if __name__ == "__main__":
    # Dummy transformed data for testing the loading process
    import pandas as pd
    test_data = {
        'column1': ['value1', 'value2'],
        'column2': ['2020-01-01', '2020-01-02'],
        'column3': [100, 200]
    }
    transformed_data = pd.DataFrame(test_data)

    # Database URI and table name for testing
    DATABASE_URI = 'sqlite:///:memory:'  # Example in-memory SQLite database for testing
    TABLE_NAME = 'example_table'

    # Call the load function
    load_data(transformed_data, DATABASE_URI, TABLE_NAME)