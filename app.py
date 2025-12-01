from flask import Flask, render_template, request, redirect, url_for
from random import shuffle

app = Flask(__name__)

score_no = 0
ques_no = 0
correct = 0
questions = []

questions_master = [
    {
        "question": "What was the independence year of Ghana?",
        "options": ["1959", "1966", "1957", "1965"],
        "answer": "1957"},
    {
        "question": "What is the specific name given to the infant of a dog?",
        "options": ["cub", "puppy", "slay", "kitten"],
        "answer": "puppy"},
    {
        "question": "A global network of interconnected devices is known as what?",
        "options": ["internet", "network", "world wide web", "transfer"],
        "answer": "internet"},
    {
        "question": "What country is the largest in Africa? ",
        "options": ["senegal", "ghana", "cote-d'ivore", "nigeria"],
        "answer": "nigeria"},
    {
        "question": "Full meaning of CPU?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Central Power Unit"],
        "answer": "Central Processing Unit"},
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["Albert Einstein", "Thomas Edison", "Isaac Newton", "Nikola Tesla"],
        "answer": "Thomas Edison"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific"
    },

    {
        "question": "Which continent is the hottest in the world?",
        "options": ["Asia", "Africa", "Australia", "South America"],
        "answer": "Africa"
    },

    {
        "question": "What is H2O commonly known as?",
        "options": ["Oxygen", "Hydrogen", "Water", "Salt"],
        "answer": "Water"
    },

    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "George Orwell"],
        "answer": "William Shakespeare"
    },

    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },

    {
        "question": "How many days are in a leap year?",
        "options": ["364", "365", "366", "367"],
        "answer": "366"
    },

    {
        "question": "Which device is used to measure temperature?",
        "options": ["Barometer", "Thermometer", "Hygrometer", "Speedometer"],
        "answer": "Thermometer"
    },

    {
        "question": "What is the capital city of Kenya?",
        "options": ["Nairobi", "Accra", "Lagos", "Cairo"],
        "answer": "Nairobi"
    },

    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["Elephant", "Lion", "Tiger", "Cheetah"],
        "answer": "Lion"
    },

    {
        "question": "How many chromosomes does a human have?",
        "options": ["23", "46", "44", "48"],
        "answer": "46"
    },

    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Osmium", "Oxygen", "Oxide", "Ozone"],
        "answer": "Oxygen"
    },

    {
        "question": "What is the longest river in the world?",
        "options": ["Nile", "Amazon", "Congo", "Mississippi"],
        "answer": "Nile"
    },

    {
        "question": "Which country invented paper?",
        "options": ["Ghana", "China", "Egypt", "India"],
        "answer": "China"
    },

    {
        "question": "What is the freezing point of water?",
        "options": ["0°C", "10°C", "32°C", "100°C"],
        "answer": "0°C"
    },

    {
        "question": "What is the capital of South Africa?",
        "options": ["Johannesburg", "Pretoria", "Durban", "Cape Town"],
        "answer": "Pretoria"
    },

    {
        "question": "Which language is the most spoken in the world?",
        "options": ["Spanish", "English", "Mandarin Chinese", "Hindi"],
        "answer": "Mandarin Chinese"
    },

    {
        "question": "How many planets are in the solar system?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
    },

    {
        "question": "Which organ pumps blood through the body?",
        "options": ["Brain", "Lungs", "Liver", "Heart"],
        "answer": "Heart"
    },

]


@app.route("/")
def home():      
    return render_template("index.html")


@app.route("/start")
def start():
    global score_no, ques_no, correct, questions
    score_no = 0
    ques_no = 0
    correct = 0
    questions = questions_master.copy()
    shuffle(questions)
    return redirect(url_for("question"))


@app.route("/question", methods=["GET", "POST"])
def question():
    global score_no, ques_no, correct, questions

    if not questions or ques_no >= len(questions):
        return redirect(url_for("result"))

    current = questions[ques_no]
    options = current["options"].copy()
    shuffle(options)

    if request.method == "POST":
        user_opt = request.form["answer"].strip().lower()
        corr_opt = current["answer"].lower()

        if user_opt == corr_opt:
            score_no += 1
            correct += 1

        ques_no += 1

        if ques_no >= len(questions):
            return redirect(url_for("result"))

    current = questions[ques_no]
    options = current["options"].copy()
    shuffle(options)
    overall = len(questions_master)
    return render_template("question.html", question=current["question"], options=options, ques_no=ques_no + 1, all=overall)


@app.route("/result")
def result():
    global score_no, ques_no, correct, questions
    total_questions = len(questions_master)
    total_per = round(score_no / total_questions * 100, 2)
    return render_template(
        "result.html",
        total=total_questions,
        percent=total_per,
        correct=correct,
        score=score_no * 2,
        num=ques_no
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
