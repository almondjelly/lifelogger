from flask import Flask, request, render_template
import datetime
import quotes
import stopwatch


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


@app.route("/daily")
def view_daily_log():
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

# @app.route("/weekly")
# def view_weekly_log():

swatch = stopwatch.Stopwatch()

@app.route("/start")
def start_stopwatch():
    swatch = stopwatch.Stopwatch()
    swatch.start_time()
    return render_template("index.html")



@app.route("/stop")
def staph_stopwatch():
    duration = swatch.stop_time()
    return render_template("index.html", duration=duration)

if __name__ == "__main__":

    app.run(debug=True)
