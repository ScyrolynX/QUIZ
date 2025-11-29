from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {"question": "What was the independence year of Ghana?", "answer": "1957"},
    {"question": "What is the specific name given to the infant of a dog?", "answer": "puppy"},
    {"question": "A global network of interconnected devices is known as what?", "answer": "internet"},
    {"question": "What is the full meaning of CPU?", "answer": "central processing unit"}
]

score_no = 0
ques_no = 0


@app.route("/")
def home():      # This is you URL for your welcome screen
    return render_template("index.html")


@app.route("/start")
def start():  # This run at start
    global score_no, ques_no
    score_no = 0
    ques_no = 0
    return redirect(url_for("question"))


@app.route("/question", methods=["GET", "POST"])
def question():
    global score_no, ques_no
    if request.method == "POST":
        user_ans = request.form["answer"].strip().lower()
        corr_ans = questions[ques_no]["answer"].lower()

        if user_ans == corr_ans:
            score_no += 1
        ques_no += 1
        if ques_no >= len(questions):
            return redirect(url_for("result"))

    current = questions[ques_no]
    return render_template("question.html", question=current["question"], ques_no = ques_no +1)


@app.route("/result")
def result():
    global score_no, ques_no
    total_per = round(score_no/len(questions)*100, 2)
    return render_template("result.html", total=len(questions), percent=total_per, score=score_no * 2, num=ques_no)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)