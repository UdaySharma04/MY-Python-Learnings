Questions = [
    ["Which language was used to create Facebook?",
     "Java", "Python", "PHP", "JavaScript", 1],  
    ["Which language is primarily used for Android development?",
     "Java", "Python", "PHP", "JavaScript", 1],  
    ["Which language is used for data science?",
     "Java", "Python", "PHP", "JavaScript", 1],  
    ["Which language is used for web development?",
     "Java", "Python", "PHP", "JavaScript", 1]   
]
levels = [1000, 2000, 3000, 4000, 5000, 10000, 16000, 32000]
money = 0

for i in range(len(Questions)):
    question = Questions[i]  # Access the current question
    print(f"Question for Rs. {levels[i]}:")
    print(f"1. {question[1]}                2. {question[3]}")
    print(f"3. {question[2]}               4. {question[4]}")
    
    reply = int(input("Enter your answer (1-4): "))
    if reply == question[-1]:  # Check if the answer is correct
        print(f"Correct answer! You have won Rs. {levels[i]}")
        money = levels[i]  # Update the money won so far
        if i == 4:
            money = 10000  # First milestone
        elif i == 9:
            money = 32000  # Second milestone
    else:
        print("Wrong answer! You have lost the game.")
        break




