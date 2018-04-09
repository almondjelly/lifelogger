from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lifelogger'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def add_new_weekly_question(question_short, question_long):
    """Adds a new question to the weekly review."""

    QUERY = """INSERT INTO questions (question_short, question_long)
                   VALUES (:question_short, :question_long)
            """

    db.session.execute(QUERY, {'question_short': question_short,
                               'question_long': question_long})

    db.session.commit()

    print "Successfully added new question: {} // {}".format(
        question_short, question_long)


def answer_weekly_question(question_short, answer):
    """Fills in a new answer to a question for the weekly review."""

    QUERY = """INSERT INTO weeklyreview (date, question, answer)
                   VALUES (current_date, :question_short, :answer)
            """

    db.session.execute(QUERY, {'question_short': question_short,
                               'answer': answer})

    db.session.commit()

    print "Answered question {} with {}".format(question_short, answer)


def get_question_long(question_short):
    """Returns the long version of the question given the short version."""

    QUERY = """SELECT question_long
               FROM questions
               WHERE question_short = :question_short
            """

    cursor = db.session.execute(QUERY, {'question_short': question_short})

    question_long = cursor.fetchone()[0]

    return question_long


def get_last_week_questions(last_week):
    """Returns a list of questions that were answered last week."""

    QUERY = """SELECT question, answer
               FROM weeklyreview
               WHERE date = :last_week
            """

    cursor = db.session.execute(QUERY, {'last_week': last_week})

    last_questions_answers = []

    for question in cursor.fetchall():
        short_question = question[0]
        answer = question[1]
        short_question.strip()
        answer.strip()
        last_questions_answers.append((short_question, get_question_long(short_question), answer))

    return last_questions_answers


if __name__ == "__main__":
    connect_to_db(app)
    db.session.close()
