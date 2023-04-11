import sqlite3
import flask

# espose rest api endpoint using flask framework
# to serve the serialized json list of books \
# queried from the sqlite database

app = flask.Flask(__name__)


@app.route("/books")
def get_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return flask.jsonify(books)


if __name__ == "__main__":
    app.run(debug=True)
