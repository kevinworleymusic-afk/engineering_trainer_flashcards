import json
import random

# -----------------------------
# Load configuation and data
# -----------------------------

with open("config.json", "r") as file:   
    config = json.load(file)

with open("questions.json", "r") as file:   
    questions = json.load(file)

channels = config["channels"]

# -----------------------------
# Choose a training Channel
# -----------------------------


def choose_channel():
    channels = config["channels"]

    print("Choose a channel:")

    for number, channel in enumerate(channels, start=1):
        print(f"{number}. {channel}")

    selection = int(input("Enter the number of your choice:"))

    selected_channel = channels[selection - 1]

    return selected_channel

selected_channel = choose_channel()

# -----------------------------
# Filter questions by channel
# -----------------------------

#Create new list only questions 
#that belong to the selected channel

selected_questions = [question for question in questions if question["category"] == selected_channel]


#-----------------------------
# Choose a question type
#-----------------------------

#Find the different question types 
#within the selected channel. 
question_types = sorted(set(question["type"] for question in selected_questions))
print("Choose a question type:")
for number, question_type in enumerate(question_types, start=1):
    print(f"{number}. {question_type}")

type_selection = int(input("Enter the number of your choice: "))

#Select the questions that match the user's selection.
selected_type = question_types[type_selection - 1]

#Filter the questions again so that only questions
#matching BOTH the selected channel and the selected type remain.
selected_questions = [question for question in selected_questions if question["type"] == selected_type]


#-----------------------------
# Build the training session
#-----------------------------


print(f"How many questions would you like to answer? (Max: {len(selected_questions)})")

num_questions = int(input("Enter the number of questions you want to answer: "))

#Randomly select questions without repeating them
#min() prevents the program from requesting more
#questions than are available. 

session_questions = random.sample(selected_questions, min(num_questions, len(selected_questions)))


#-----------------------------
# Run the Question session
#-----------------------------
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

#-----------------------------
## Display the results
#-----------------------------

print(f"You scored {score} out of {len(session_questions)}.")

accuracy = (score / len(session_questions)) * 100
print(f"Your accuracy is {accuracy:.2f}%.")

#print(f"You selected: {selected_channel}")



