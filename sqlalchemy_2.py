"""
- Create a connection using sqlalchemy and after creating a connection use `connect()` function on connection object to
ensure connection is successfully established or not

- Metadata_obj contains all the information about our database which is why we pass it in when creating the table(for
understanding see profile variable value)

- The metadata_obj.create_all(engine) binds the metadata to the engine and creates the table if table does not exist in
database
"""
import sqlalchemy as db

# defining a DB engine
engine = db.create_engine(url="mysql+pymysql://root:Aaibaba@localhost:3306/starwarsDB")

# Actual connection with database
conn = engine.connect()

metadata_obj = db.MetaData()

# defining a table using sqlalchemy
profile = db.Table(
    "Profile",
    metadata_obj,
    db.Column("Id", db.Integer, primary_key=True),
    db.Column("Name", db.String(250)),
    db.Column("Email", db.String(250)),
    db.Column("Contact", db.Integer)
                   )

# Creation of Table

metadata_obj.create_all(bind=engine)
