import random
from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from .models import db, Question

main = Blueprint("main", __name__)


@main.route("/")
def home():
    categories = [c[0] for c in db.session.query(Question.category).distinct()]
    return render_template("index.html", categories=categories)


@main.route("/start", methods=["POST", "GET"])
def start():
    category = request.values.get("category", "all")

    query = Question.query
    if category != "all":
        query = query.filter_by(category=category)

    all_ids = [q.id for q in query.all()]
    if not all_ids:
        all_ids = [q.id for q in Question.query.all()]

    random.shuffle(all_ids)
    n = min(current_app.config["QUESTIONS_PER_ROUND"], len(all_ids))

    session["question_ids"] = all_ids[:n]
    session["current_index"] = 0
    session["score"] = 0
    session["category"] = category

    return redirect(url_for("main.question"))


@main.route("/question", methods=["GET", "POST"])
def question():
    question_ids = session.get("question_ids")
    if not question_ids:
        return redirect(url_for("main.home"))

    index = session.get("current_index", 0)

    if request.method == "POST":
        submitted_id = int(request.form["question_id"])
        current_q = Question.query.get(submitted_id)
        chosen = request.form.get("answer", "").strip()

        if current_q and chosen == current_q.answer:
            session["score"] = session.get("score", 0) + 1

        index += 1
        session["current_index"] = index

    if index >= len(question_ids):
        return redirect(url_for("main.result"))

    current_q = Question.query.get(question_ids[index])
    options = current_q.options()
    random.shuffle(options)

    return render_template(
        "question.html",
        question=current_q,
        options=options,
        current_number=index + 1,
        total=len(question_ids),
    )


@main.route("/result")
def result():
    question_ids = session.get("question_ids", [])
    total = len(question_ids)
    score = session.get("score", 0)
    percent = round((score / total) * 100, 1) if total else 0

    return render_template(
        "result.html",
        score=score,
        total=total,
        percent=percent,
    )
