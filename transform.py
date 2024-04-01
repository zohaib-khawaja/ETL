import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform_data(extracted_data):
    """
    Transforms the extracted data. This function cleans, normalizes, and prepares the data for loading.

    :param extracted_data: The data extracted in the form of a list of dictionaries.
    :return: A DataFrame containing the transformed data.
    """
    logging.info("Starting data transformation")

    # Convert the list of dictionaries to a pandas DataFrame for easier manipulation
    df = pd.DataFrame(extracted_data)

    # Example transformation steps:
    # Filter out unnecessary columns (assuming 'userId', 'id', 'title', 'body' are the relevant columns)
    columns_to_keep = ['userId', 'id', 'title', 'body']
    df = df[columns_to_keep]

    # Rename columns for consistency (if needed)
    df.rename(columns={'userId': 'User_ID', 'id': 'ID'}, inplace=True)

    # Fill in missing values or drop them
    df['body'] = df['body'].fillna('No content')

    logging.info("Data transformation complete")
    return df

# If this script is run directly, use test data for the transformation process
if __name__ == "__main__":
    # Dummy data for testing the transformation process
    test_data = [
        {'userId': '1', 'id': '101', 'title': 'Test Title 1', 'body': 'Test Body 1'},
        {'userId': '2', 'id': '102', 'title': 'Test Title 2', 'body': 'Test Body 2'}
    ]
    transformed_data = transform_data(test_data)
    print(transformed_data)