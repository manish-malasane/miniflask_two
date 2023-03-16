from flask import Flask, render_template, abort, jsonify
from models.dal import db

# Flask is a class we used to instantiate an application
app = Flask(__name__)


# route decorater allows us to bind a function with certain `relative URL path`
@app.route("/welcome")
def welcome():
    return render_template("welcome.html", message="This is the message from view")


@app.route("/card/<int:index>")
def flash_card(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index)
    except IndexError:
        abort(404)


@app.route("/api/card")
def card_list():
    """
    NOTE:-
        We use jsonify method for explicitly getting the content type as application/json even after it is not like a
        json
    """
    return jsonify(db)
