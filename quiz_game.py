print("Hello, Welcome to the daily quiz!\n")
score = 0


def answer():
    ans = input("Would you like to play? ")
    if ans == "yes":
        print("Let's get started!")
    elif ans == "no":
        print("Thanks  for coming!")
        quit()
    else:
        print("Please try again!")
        answer()


answer()

question_1 = "1. How many letters are there in the alphabet? "
ans = input(question_1)
if ans == "26":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_2 = "2. Who is the best player in the world? "
ans = input(question_2)
if ans.lower() == "ronaldo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_3 = "3. How many bones does the human body have? "
ans = input(question_3)
if ans == "256":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_4 = "4. Who is the president of the United States? "
ans = input(question_4)
if ans.lower() == "joe biden":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_5 = "5. Who is the prime minister of Bangladesh? "
ans = input(question_5)
if ans.lower() == "sheikh hasina":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_6 = "6. How many hours are there in a day? "
ans = input(question_6)
if ans == "24":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_7 = "7. What is the easiest programming language? "
ans = input(question_7)
if ans.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_8 = "8. What does cpu stand for? "
ans = input(question_8)
if ans.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_9 = "9. What does DS stand for? "
ans = input(question_9)
if ans.lower() == "data science":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question_10 = "10. What does ML stand for? "
ans = input(question_10)
if ans.lower() == "machine learning":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")
print("Congratulations, the quiz is over!")
print(f"You got {score} out of 10 correct")
print("Thanks for playing!")
