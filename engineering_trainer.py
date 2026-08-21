import json
import random


with open("config.json", "r") as file:   
    config = json.load(file)

with open("questions.json", "r") as file:   
    questions = json.load(file)

channels = config["channels"]

def choose_channel():
    channels = config["channels"]

    print("Choose a channel:")

    for number, channel in enumerate(channels, start=1):
        print(f"{number}. {channel}")

    selection = int(input("Enter the number of your choice:"))

    selected_channel = channels[selection - 1]

    return selected_channel

selected_channel = choose_channel()

selected_questions = [question for question in questions if question["category"] == selected_channel]

print(f"How many questions would you like to answer? (Max: {len(selected_questions)})")

num_questions = int(input("Enter the number of questions you want to answer: "))

session_questions = random.sample(selected_questions, min(num_questions, len(selected_questions)))

score = 0

for question in session_questions:


        print(f"Question: {question['question']}")

        for letter, choice in question["choices"].items():
            print(f"{letter}: {choice}")

        answer = input("Your answer: ")
        if answer.strip().upper() == question["correct_answer"]:
            print("Correct!")
            score += 1
        else: 
            print(f"Incorrect. The correct answer is {question['correct_answer']}.")

print(f"You scored {score} out of {len(session_questions)}.")

accuracy = (score / len(session_questions)) * 100
print(f"Your accuracy is {accuracy:.2f}%.")

#print(f"You selected: {selected_channel}")



