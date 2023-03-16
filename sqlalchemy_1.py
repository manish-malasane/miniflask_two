from sqlalchemy import create_engine
# create engine function is for creating the db connection using sqlalchemy library

user = "root"
password = "Aaibaba"
port = 3306
host = "127.0.0.1"
database_name = "starwarsDB"


def get_sqlalchemy_conn():
    return create_engine(
        url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"
                         )


if __name__ == "__main__":
    conn = get_sqlalchemy_conn()
    if conn:
        print("[ INFO ] Connection created successfully.")
    else:
        print("[ ERROR ] You have entered wrong credentials.")
    breakpoint()
