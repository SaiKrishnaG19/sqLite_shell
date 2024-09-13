# SQLAlchemy Interactive Shell, Schema Creation, and Data Generation

## Overview

This project provides a hands-on approach to learning SQL and database management using SQLAlchemy and SQLite. It consists of three Python scripts that help you interact with databases, create database schemas, and generate random data for testing. It’s perfect for beginners and learners who want real-world experience with database operations, schema design, and SQL queries.

## Key Components

- **Interactive SQL Shell**: Run SQL queries in a live environment and manage transactions.
  
- **Schema Creation**: Define and create a complete database schema with multiple entities (users, products, customers, orders).
  
- **Data Generation**: Automatically generate random data for your tables to simulate real-world scenarios.

## Why Use This Project?

This project provides practical experience in SQL and database management that can be directly applied to real-world projects. You'll learn to:

- Interact with a database dynamically.
  
- Create and manage a complex relational database schema.
  
- Generate meaningful data to simulate user and order management systems.
  
- Handle transaction management (BEGIN, COMMIT, ROLLBACK) interactively.

It’s an excellent resource for beginners, developers, and anyone wanting to explore SQLAlchemy and databases in Python.

## Getting Started

### Prerequisites

- Python 3.x installed
- SQLAlchemy package installed (`pip install sqlalchemy`)
- Faker package for data generation (`pip install faker`)
- SQLite database for local storage

### Instructions

#### 1. Interactive SQL Shell

This script allows you to run SQL queries directly on an SQLite database, making it perfect for learning SQL, testing queries, or working on small projects.

**Steps to Run:**

1. **Edit the Database URL**: Update the `database_url` in the script with your local database path.

   ```python
   database_url = r"sqlite:///path_to_your_database.db"
   ```

2. **Run the Script**:

   ```bash
   python sql_shell.py
   ```

3. **Enter SQL Queries**: Type `exit` or `quit` to leave the shell. You can run queries like `SELECT * FROM table_name;` and view the results.

4. **Transaction Management**:
   - Begin a transaction with `BEGIN` or `BEGIN TRANSACTION`.
   - Commit using `COMMIT`.
   - Rollback using `ROLLBACK`.

#### 2. Schema Creation Script

The schema creation script defines the following entities:

- **User**: Represents user accounts.
- **Product**: Stores information about products.
- **Customer**: Customer details linked to users.
- **Order**: Records customer orders.
- **OrderItem**: Items in each order.

**Steps to Run:**

1. **Edit the Database Path**: Update the database URL in the schema script:

   ```python
   db_path = r"sqlite:///path_to_your_database.db"
   ```

2. **Run the Script**:

   ```bash
   python schema.py
   ```

3. **Check Database**: Once the script is executed, the tables will be created in your SQLite database.

#### 3. Data Generation Script

This script helps in generating random data for the database, simulating real-world user interactions such as product purchases.

**Available Tables for Data Generation:**

- **products**: Generate random products.
- **customers**: Generate random customer profiles.
- **orders**: Generate orders with different statuses.
- **order_items**: Generate order items associated with existing orders and products.
- **cutomized**: you can also create custome tables and generate data for customized table data.


**Steps to Run:**

1. **Edit the Database Path**: Update the database URL in the data generation script:

   ```python
   db_path = r"sqlite:///path_to_your_database.db"
   ```

2. **Run the Script**:

   ```bash
   python gendata.py
   ```

3. **Choose a Table**: When prompted, enter the table name you want to generate data for.

4. **Input the Number of Records**: Specify how many records you want to generate.

5. **Review Data**: After generation, review the data by querying the corresponding tables in the database.

## Example Use Cases

- **Learning SQL**: The interactive shell lets you practice SQL in a real database environment, learning how to write queries, manipulate data, and handle transactions.

- **Database Design**: Use the schema creation script to explore database design principles like relationships, foreign keys, and normalization.

- **Test Data Generation**: Generate meaningful data for testing applications or conducting SQL experiments without manually entering information.

## Project Structure

```
.
├── sql_shell.py   # Interactive SQL shell with transaction support
├── schema.py           # Database schema creation using SQLAlchemy
├── gendata.py           # Data generation for testing the schema
└── README.md                  # Project documentation
```

## Conclusion

This project offers a comprehensive yet straightforward way to practice SQL, database schema design, and data manipulation in Python. By using SQLAlchemy and SQLite, you can gain practical experience with relational databases, transactions, and real-world data scenarios, making you better prepared for database-related projects in the real world.

Citations:
[1] https://devcamp.com/trails/python-api-development-with-flask/campsites/hello-flask/guides/creating-sqlite-database-flask-sqlalchemy
[2] https://realpython.com/python-sqlite-sqlalchemy/
[3] https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
[4] https://python-forum.io/thread-24127.html
[5] https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
[6] https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
[7] https://docs.sqlalchemy.org/en/20/core/engines.html
[8] https://stackoverflow.com/questions/51756650/using-proper-file-structure-with-sqlalchemy-and-how-to-add-data-to-db
