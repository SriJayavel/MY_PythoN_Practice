#---------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("---------------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)
        guess = input("Enter (A,B,C,or D): ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answers(questions.get(key),guess)

        questions_num += 1

   
    
    display_score(correct_guesses,guesses)
#---------------------------
def check_answers(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#---------------------------
def display_score(correct_guesses,guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")   

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#---------------------------
def play_again():
    response = input("Do you wanna play again?: (YES OR NO)")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

#---------------------------

questions = {
    "What is a panda?: ":"B",
    "Who was a key figure in WW2?: ":"D",
    "What pokemon is popular?: ":"A",
    "Do Banana is Naturally created First?: ":"B"
}
options = [["A.Toy","B.Animal","C.My Tiddy","D.Plant"],
           ["A.I'm","B.Stalin","C.RussPutin","D.Hitler"],
           ["A.Pikachiu","B.DarkPikachiu","C.Babapet","D.Diglet"],
           ["A.True","B.Man made","C.IDK","D.God created it"]]

new_game()

while play_again():
    new_game()
print("See ya")