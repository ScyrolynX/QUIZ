from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    option_a = db.Column(db.String(150), nullable=False)
    option_b = db.Column(db.String(150), nullable=False)
    option_c = db.Column(db.String(150), nullable=False)
    option_d = db.Column(db.String(150), nullable=False)
    answer = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), default="general")
    difficulty = db.Column(db.String(20), default="medium")

    def options(self):
        return [self.option_a, self.option_b, self.option_c, self.option_d]

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.text,
            "options": self.options(),
            "answer": self.answer,
        }
