import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

data = response.json()

questions = []
question_dict = {}

for question in data["results"]:
    question_dict={
        "type":question["type"],
        "difficulty":question["difficulty"],
        "category":question["category"],
        "question":question["question"],
        "correct_answer":question["correct_answer"],
        "incorrect_answers":question["incorrect_answers"]}

    questions.append(question_dict)