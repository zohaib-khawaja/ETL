# ETL Application

## Overview

This ETL (Extract, Transform, Load) application is designed to automate the process of extracting data from a REST API, transforming the data, and loading it into a database. It is containerized for easy deployment and scaling.


## Features

- **Data Extraction**: Connects to any REST API to extract data.
- **Data Transformation**: Transforms extracted data using pandas for data manipulation.
- **Data Loading**: Loads the transformed data into a specified database.

## Prerequisites

- Docker installed on your machine.
- Access to a REST API for data extraction.
- A target database for data loading.


## Installation

1. Pull the Docker image from Docker Hub:
docker pull leggoboyo/etl-app:latest

2. Run the Docker container, specifying the necessary environment variables:
docker run -e DATABASE_URI='your_database_connection_uri' -e TABLE_NAME='your_target_table' leggoboyo/etl-app:latest


## Configuration

The application can be configured through the following environment variables:

- `DATABASE_URI`: The URI for the target database where data will be loaded.
- `TABLE_NAME`: The name of the target table in the database.

Example for a SQLite database:

DATABASE_URI='sqlite:///test.db'
TABLE_NAME='test_table'


## Usage

Once the container is running, it will automatically start the ETL process:

1. **Extract**: Pulls data from the configured REST API endpoint.
2. **Transform**: Processes the data according to the transformation rules defined in `transform.py`.
3. **Load**: Inserts the transformed data into the specified database and table.