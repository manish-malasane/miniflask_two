from sqlalchemy import create_engine, MetaData, Integer, VARCHAR, Table, Column

"""
host = localhost OR 127.0.0.1
user = root
port = 3306
password = *****
database_name = starwarsDB
"""


def get_engine():
    # Defining an engine
    return create_engine("mysql+pymysql://root:Aaibaba@localhost:3306/starwarsDB")


if __name__ == "__main__":
    # Getting an engine
    engine = get_engine()

    # Actual connection to the database
    conn = engine.connect()

    # Knows all the info about the database and this we have to pass when we create a table
    meta_obj = MetaData()

    # defining a table
    book_table = Table(
        "BOOKS",
        meta_obj,
        Column("Id", Integer, primary_key=True),
        Column("Book_Name", VARCHAR(250)),
        Column("Book_Price", Integer),
        Column("POV", VARCHAR(100)),
    )

    # creating the table using sqlalchemy (ORM)
    meta_obj.create_all(bind=engine)

    # Defining Insert records
    st_1 = book_table.insert().values(
        Id=1, Book_Name="Sherlock_Holmes", Book_Price=499, POV="Related with sherlock"
    )
    st_2 = book_table.insert().values(
        Id=2, Book_Name="500 Days", Book_Price=399, POV="Something"
    )
    st_3 = book_table.insert().values(
        Id=3, Book_Name="Detectives", Book_Price=699, POV="Caught the Murderer"
    )

    # Inserting the records into database
    with engine.connect() as conn_:
        res_1 = conn_.execute(st_1)
        res_2 = conn_.execute(st_2)
        res_3 = conn_.execute(st_3)
        conn_.commit()
