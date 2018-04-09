from flask import Flask, request, render_template, redirect
import datetime
import quotes
import stopwatch
import weekly


app = Flask(__name__)


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


@app.route("/weekly-add", methods=["POST"])
def add_weekly_question():
    """Add a new question to the weekly review."""

    question_short = request.form.get('question_short')
    question_long = request.form.get('question_long')
    weekly.add_new_weekly_question(question_short, question_long)

    return redirect("/weekly")


@app.route("/weekly-submit", methods=["POST"])
def submit_answer():
    """Add answer to weeklyreview table."""

    count = int(request.form.get('count'))
    while count > 0:
        short_q_str = 'short_q' + str(count)
        short_q = request.form.get(short_q_str)

        question_answer_str = 'question_answer' + str(count)
        answer = request.form.get(question_answer_str)

        weekly.answer_weekly_question(short_q, answer)

        count = count - 1

    return redirect("/weekly")


@app.route("/weekly")
def view_weekly_log():
    """Display weekly review page."""

    q = weekly.get_last_week_questions('2018-04-08')

    return render_template("weekly-review.html", questions=q)


swatch = stopwatch.Stopwatch()

@app.route("/start")
def start_stopwatch():
    global swatch
    swatch = stopwatch.Stopwatch()
    swatch.start_time()

    return render_template("index.html")


@app.route("/stop")
def staph_stopwatch():
    duration = swatch.stop_time()

    return render_template("index.html", duration=duration)



if __name__ == "__main__":

    weekly.connect_to_db(app)

    app.run(debug=True)
