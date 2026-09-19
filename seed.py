"""Seed the database with the starter question bank.
Run with: python seed.py
"""
from app import create_app
from app.models import db, Question

QUESTIONS = [
    ("What was the independence year of Ghana?", ["1959", "1966", "1957", "1965"], "1957", "geography"),
    ("What is the specific name given to the infant of a dog?", ["cub", "puppy", "slay", "kitten"], "puppy", "general"),
    ("A global network of interconnected devices is known as what?", ["internet", "network", "world wide web", "transfer"], "internet", "tech"),
    ("What country is the largest in Africa?", ["senegal", "ghana", "cote-d'ivore", "nigeria"], "nigeria", "geography"),
    ("Full meaning of CPU?", ["Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Central Power Unit"], "Central Processing Unit", "tech"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars", "science"),
    ("Who invented the light bulb?", ["Albert Einstein", "Thomas Edison", "Isaac Newton", "Nikola Tesla"], "Thomas Edison", "history"),
    ("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific", "geography"),
    ("Which continent is the hottest in the world?", ["Asia", "Africa", "Australia", "South America"], "Africa", "geography"),
    ("What is H2O commonly known as?", ["Oxygen", "Hydrogen", "Water", "Salt"], "Water", "science"),
    ("Who wrote the play 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Mark Twain", "George Orwell"], "William Shakespeare", "literature"),
    ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Carbon Dioxide", "science"),
    ("How many days are in a leap year?", ["364", "365", "366", "367"], "366", "general"),
    ("Which device is used to measure temperature?", ["Barometer", "Thermometer", "Hygrometer", "Speedometer"], "Thermometer", "science"),
    ("What is the capital city of Kenya?", ["Nairobi", "Accra", "Lagos", "Cairo"], "Nairobi", "geography"),
    ("Which animal is known as the King of the Jungle?", ["Elephant", "Lion", "Tiger", "Cheetah"], "Lion", "general"),
    ("How many chromosomes does a human have?", ["23", "46", "44", "48"], "46", "science"),
    ("Which element has the chemical symbol 'O'?", ["Osmium", "Oxygen", "Oxide", "Ozone"], "Oxygen", "science"),
    ("What is the longest river in the world?", ["Nile", "Amazon", "Congo", "Mississippi"], "Nile", "geography"),
    ("Which country invented paper?", ["Ghana", "China", "Egypt", "India"], "China", "history"),
    ("What is the freezing point of water?", ["0°C", "10°C", "32°C", "100°C"], "0°C", "science"),
    ("What is the capital of South Africa?", ["Johannesburg", "Pretoria", "Durban", "Cape Town"], "Pretoria", "geography"),
    ("Which language is the most spoken in the world?", ["Spanish", "English", "Mandarin Chinese", "Hindi"], "Mandarin Chinese", "general"),
    ("How many planets are in the solar system?", ["7", "8", "9", "10"], "8", "science"),
    ("Which organ pumps blood through the body?", ["Brain", "Lungs", "Liver", "Heart"], "Heart", "science"),
]


def seed():
    app = create_app()
    with app.app_context():
        if Question.query.first():
            print("Questions already seeded, skipping.")
            return

        for text, options, answer, category in QUESTIONS:
            q = Question(
                text=text,
                option_a=options[0],
                option_b=options[1],
                option_c=options[2],
                option_d=options[3],
                answer=answer,
                category=category,
            )
            db.session.add(q)

        db.session.commit()
        print(f"Seeded {len(QUESTIONS)} questions.")


if __name__ == "__main__":
    seed()
