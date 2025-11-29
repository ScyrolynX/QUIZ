from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions =[
{
"question": "What was the independence year of Ghana?",
"options":["1959", "1966", "1957", "1965"],
"answer": "1957"}
{
"question": "What is the specific name given to the infant of a dog?", 
"options": ["cub", "puppy", "slay", "kitten"],
"answer": "puppy"}
{
"question": "A global network of interconnected devices is known as what?",
"options": ["internet", "network", "world wide web", "transfer"],
"answer": "internet"}
{
"question": "What country is the largest in Africa? ",
"options": ["senegal", "ghana", "cote-d'ivore", "nigeria"],
"answer": "nigeria"}
{
"question": "Full meaning of CPU?",
"options": ["Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Central Power Unit"],
"answer": "Central Processing Unit"
}
]


@app.route("/")
def home():      # This is you URL for your welcome screen
    return render_template("index.html")


@app.route("/start")
def start():  # This run at start
    global score_no, ques_no, correct
    score_no = 0
    ques_no = 0
    correct = 0
    return redirect(url_for("question"))


@app.route("/question", methods=["GET", "POST"])
def question():
    global score_no, ques_no
    if request.method == "POST":
        user_opt = request.form["answer"].strip().lower()
        corr_opt = questions[ques_no]["answer"].lower()

        if user_opt == corr_opt:
            score_no += 1
            correct += 1
        ques_no += 1
        if ques_no >= len(questions):
            return redirect(url_for("result"))

    current = questions[ques_no]
    return render_template("question.html", question=current["question"], options= current["options"], ques_no = ques_no +1)


@app.route("/result")
def result():
    global score_no, ques_no, correct
    total_per = round(score_no/len(questions)*100, 2)
    return render_template("result.html", total=len(questions), percent=total_per, correct= correct, score=score_no * 2, num=ques_no)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)