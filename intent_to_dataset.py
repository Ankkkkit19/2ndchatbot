import json

def load_intents_as_qa(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    questions = []
    answers = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            questions.append(pattern.lower())
            answers.append(intent["responses"][0])  # first response

    return questions, answers
