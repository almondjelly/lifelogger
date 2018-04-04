from flask import Flask, request, render_template
import datetime
import quotes


# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()


# def connect_to_db(app):
#     """Connect to database."""

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///melondb'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.app = app
#     db.init_app(app)


app = Flask(__name__)

# connect_to_db(app)


@app.route("/")
def index():
    """Display homepage."""

    return render_template("index.html")


@app.route("/quotes_archive")
def view_quotes():

    quote = quotes.display_quotes()

    return render_template("quotes_archive.html", quote=quote)


@app.route("/log")
def view_log():
    """Display daily log page."""

    date = datetime.date.today()
    year = date.strftime("%G")
    month = date.strftime("%B")
    day = date.strftime("%e")


    quote = quotes.choose_quote()

    return render_template("log.html",
                           date=date,
                           year=year,
                           month=month,
                           day=day,
                           quote=quote
                           )


if __name__ == "__main__":

    app.run(debug=True)
