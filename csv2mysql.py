import pandas as pd
from sqlalchemy import create_engine


def config():
    username = input("Enter username: ")
    password = input("Enter password: ")
    host = input("Enter host: ")
    database_name = input("Enter database name: ")
    return username, password, host, database_name


def get_file():
    return input("Enter csv file path: ")


def read_csv(csv_file):
    return pd.read_csv(csv_file)


def write2mysqldb(df, table_name, engine):
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)


def main():
    username, password, host, database_name = config()
    csv_file = get_file()
    df = read_csv(csv_file)
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database_name}')
    table_name = input("Enter table name: ")
    write2mysqldb(df, table_name, engine)
    print("Done")
    
    
if __name__ == '__main__':
    main()