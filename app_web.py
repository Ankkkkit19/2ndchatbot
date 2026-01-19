from flask import Flask, render_template, request
from dataset_trainer import train_dataset
from dataset_bot import dataset_answer

app = Flask(__name__)

# 🔥 LOAD BOTH dataset.json + intents.json
questions, answers, vectorizer, question_vectors = train_dataset(
    "dataset.json",
    "intents.json"
)

@app.route("/", methods=["GET", "POST"])
def home():
    user = ""
    reply = ""

    if request.method == "POST":
        user = request.form.get("msg")
        reply = dataset_answer(
            user,
            questions,
            answers,
            vectorizer,
            question_vectors
        )

    return render_template("index.html", user=user, reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
