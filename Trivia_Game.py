

def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        questions_num += 1


    display_score(correct_guesses,guesses)

def check_answer(answer, guss):
    if answer == guss:
        print("CORRECT")
        return 1
    else:
        print("WORNG")
        return  0


def check_game():
    pass
def display_score(correct_guesses,guesses):
    print("-----------------------")
    print("RESULTS")
    print("-----------------------")
    print("ANSWERS:",end=" ")
    print()
    for i in questions:
        print(questions.get(i),end="")
        print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is "+str(score)+"%")

def play_agine():
    response = input("Do you want to play again ? (yes or no ?)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {" In what year was the first-ever Wimbledon Championship held?:" : "A",
"Hg is the chemical symbol of which element?: " : "B",
"Which email service is owned by Microsoft?:" : "D",
"Which country produces the most coffee in the world?:" : "B" ,
"In which city was Jim Morrison buried?:" : "A",
"Which song by Luis Fonsi and Daddy Yankee has the most views (of all time) on YouTube?:" : "B",
"What was the first state?: " : "C",
"What is the capital city of Spain?:" : "B",
"What is the painting “La Gioconda” more usually known as?:" : "C",
"What is Chandler’s last name in the sitcom Friends?:" : "A",}

options = [["A.1877","B.1876","C.1890","D.H2O"],["A.Tocsic","B.Mercury","C.H20","D.Oxidisers"],
           ["A.Gmail","B.Walla","C.Outlook","D.Hotmail"],["A.Albania","B.Brazil","C.Etiopia","D.Turkey"],
           ["A.Pris","B.london","C.China","D.USA"],["A.Mia","B.despacito","C.Baby","D.nosa"],
           ["A.Los angles","B.Denver","C.Delaware","D.New york"],["A.Barcelona","B.Madrid","C.Valencia","D.Sevilla"],
           ["A.Girl with a Pearl Earring","B.The Starry Night","C.Mona Lisa","D.The Birth of Venus"],
           ["A.bing","B.Geler","C.Grin","D.Bufe"]]



new_game()
while play_agine():
     new_game()

print("byeee Falisha!")






