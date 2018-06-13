import os
import time
import crayons
import wikipedia
import nltk
import pytesseract

from PIL import Image, ImageEnhance

# Split up newlines until we have our question and answers

question = "In Mexico, a saladito is always known as what?"
answers = ["Taco salad", "Salted plum", "Guava roll"]

q_terms = question
#for char in '-.,\n':
#    q_terms=q_terms.replace(char,' ')
q_terms = q_terms.split()
print question 
print answers 
print q_terms 

#q_terms = question.split(" ")

q_terms = set(q_terms)


answers = list(filter(lambda p: len(p) > 0, q_terms)) 
        

print("\n".format(crayons.blue(question), crayons.blue(", ".join(answers))))


answer_results = {}

for answer in answers:
    records = wikipedia.search(answer)
    r = records[0] if len(records) else None

    if r is not None:
        p = wikipedia.page(r)
        answer_results[answer] = {
            "content": p.content,
            "words": p.content.split(" ")
        }

for a in answer_results:
    term_count = 0

    for t in q_terms:
        term_count += answer_results[a]["words"].count(t)

    tc = term_count / len(answer_results[a]["words"])
    tcp = round(tc * 10000, 2)

    answer_results[a]["score"] = tcp

max_a = 0
max_a_key = None

# Maximize
for a in answer_results:
    if answer_results[a]["score"] > max_a:
        max_a_key = a
        max_a = max(answer_results[a]["score"], max_a)

print(crayons.green(max_a_key))

input("Continue?")

if not DEBUG:
    os.rename(file_path, file_path.replace("Screen Shot", "Done"))

    time.sleep(0.1)
    os.system("clear")