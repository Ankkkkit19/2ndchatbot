from flask import Flask, render_template, request
import os

from dataset_trainer import train_dataset
from dataset_bot import dataset_answer

# -------------------------------
# Flask App
# -------------------------------
app = Flask(__name__)

# -------------------------------
# Load datasets (ONLY ONCE)
# -------------------------------
# This loads:
# - dataset.json
# - intents.json (converted internally to Q&A)
questions, answers, vectorizer, question_vectors = train_dataset(
    "dataset.json",
    "intents.json"
)

# -------------------------------
# Routes
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    user = ""
    reply = ""

    if request.method == "POST":
        user = request.form.get("msg", "").strip()

        if user:
            reply = dataset_answer(
                user,
                questions,
                answers,
                vectorizer,
                question_vectors
            )

    return render_template(
        "index.html",
        user=user,
        reply=reply
    )

# -------------------------------
# Run App (LOCAL + RENDER)
# -------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
