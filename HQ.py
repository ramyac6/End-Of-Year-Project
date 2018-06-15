import os
import time
import crayons
import wikipedia
import nltk
import pytesseract
import re


#This is the stuff that gets input from the ocr
question = "Which actor turned down the role of James Bond twice before finally accepting?"
answers = ["Timothy Dalton", "Roger Moore", "Sean Connery"]

print question 
print answers 

#Creates terms that are searched
q_terms = question.split(" ")
q_terms = set(q_terms)

#Removes extra words
phrases = q_terms
words=['a', 'of', 'the', 'In', 'for', 'at']
phrases2 = [" ".join([w for w in t.split() if not w in words]) for t in phrases]
#print phrases2      

#Creates a map of answer results
answer_results = {}

#For each of the answers, creates text of wikipedia page
for answer in answers:
    records = wikipedia.search(answer)  
    r = records[0] if len(records) else None

    if r is not None:
        p = wikipedia.WikipediaPage(title = r).content
        answer_results[answer] = {
            #"content": p.content,
            "words": p.split(" ")
        }

#For each of the question terms, looks up in each of the answer texts
for a in answer_results:
    term_count = 0.0

    #Counts number of times it appears
    for t in phrases2:
        term_count += answer_results[a]["words"].count(t)

    #Creates a score like thing by finding the ratio of the amount of times the
    # term shows up
    tc = term_count / len(answer_results[a]["words"])
    tcp = round(tc * 10000, 2)

    answer_results[a]["score"] = tcp

max_a = 0
max_a_key = None

# Finds the max score and prints it
for a in answer_results:
    if answer_results[a]["score"] > max_a:
        max_a_key = a
        max_a = max(answer_results[a]["score"], max_a)

print(max_a_key)


#All this does is crash the program
'''
input("Continue?")

if not DEBUG:
    os.rename(file_path, file_path.replace("Screen Shot", "Done"))

    time.sleep(0.1)
    os.system("clear")
'''
