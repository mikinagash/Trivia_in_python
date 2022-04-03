def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1
    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)

         questions_num += 1




def check_game():
    pass
def display_score():
    pass
def play_agine():
    pass
#
questions = {" In what year was the first-ever Wimbledon Championship held?:" : "A",
"Hg is the chemical symbol of which element?: " : "B",
"Which email service is owned by Microsoft?:" : "D",
"Which country produces the most coffee in the world?:" : "B" ,
"In which city was Jim Morrison buried?:" : "A",
"Which song by Luis Fonsi and Daddy Yankee has the most views (of all time) on YouTube?:" : "A",
"What was the first state?: " : "A",
"What is the capital city of Spain?:" : "A",
"What is the painting “La Gioconda” more usually known as?:" : "A",
"What is Chandler’s last name in the sitcom Friends?:" : "A",}
