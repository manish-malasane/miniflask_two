import json

"""
Implementing the model for our website by simulating database.

Note - 
    Although this is nice as an simple example, 
    In real-world project we do not use global object for application data.
"""


def load_db():
    with open(
        "C:\\Users\\Manthan\\Desktop\\PyCharm\\flask_two\\models\\flashcard_db.json"
    ) as foo:
        return json.load(foo)


db = load_db()
