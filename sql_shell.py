import logging
from sqlalchemy import create_engine,text
import sys

logging.basicConfig(
    filename = 'errors.log',
    level = logging.ERROR,
    format = '%(asctime)s - %(levelname)s -%(message)s'
)

def connect_to_db(database_url):
    try:
        engine = create_engine(database_url)
        connection = engine.connect()
        return connection
    except Exception as error:
        logging.error(f'Error connectiong to database:{error}', exc_info=True)
        print(f'Error connectiong to database:{error}')
        sys.exit(1)

def run_query(connection,query):
    try:
        if query.strip().lower() in ["begin", "begin transaction"]:
            connect.begin()
            print("Transaction started.")
            return
        elif query.strip().lower() == "commit":
            connection.commit()
            print("Transaction committed.")
            return
        elif query.strip().lower() == "rollback":
            connection.rollback()
            print("Transaction rolled back.")

        result = connection.execute(text(query))

        if result.returns_rows:
            rows = result.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No rows returned.")
        else:
            print(f"Query executed successfully")
            print(f"Rows affected:{result.rowcount}")

    except Exception as error:
        logging.error("Error executing query", exc_info=True)
        print(f"Error executing query:{error}")

def main():
    database_url = r"sqlite:///enter db path here !"
    connection = connect_to_db(database_url)
    print(f"Connected to the database at {database_url}")
    print(f"Enter SQL Queries (type 'exit' to quite):")

    while True:
        query = input("Sql>")
        if query.lower() in ('exit','quit'):
            break
        if query.strip():
            run_query(connection, query)
    
    connection.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
