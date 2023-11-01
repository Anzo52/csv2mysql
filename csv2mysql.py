import pandas as pd
from sqlalchemy import create_engine


def config():
    """
    Prompts the user to enter database credentials and returns them as a tuple.

    Returns:
        tuple: A tuple containing the username, password, host, and database name.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")
    host = input("Enter host: ")
    database_name = input("Enter database name: ")
    return username, password, host, database_name


def get_file():
    """
    Prompts the user to enter the path of a CSV file and returns it.

    Returns:
        str: The path of the CSV file.
    """
    return input("Enter csv file path: ")


def read_csv(csv_file):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Args:
        csv_file (str): The path of the CSV file.

    Returns:
        pandas.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(csv_file)


def write2mysqldb(df, table_name, engine):
    """
    Writes a pandas DataFrame to a MySQL database table.

    Args:
        df (pandas.DataFrame): The pandas DataFrame to write to the database.
        table_name (str): The name of the database table to write to.
        engine (sqlalchemy.engine.base.Engine): The SQLAlchemy engine to use for the database connection.
    """
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)


def main():
    """
    The main function that prompts the user for input, reads a CSV file, writes the data to a MySQL database table,
    and prints a message when done.
    """
    username, password, host, database_name = config()
    csv_file = get_file()
    df = read_csv(csv_file)
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database_name}"
    )
    table_name = input("Enter table name: ")
    write2mysqldb(df, table_name, engine)
    print("Done")


if __name__ == "__main__":
    main()
