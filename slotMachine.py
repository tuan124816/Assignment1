from random import randint
current_cash = 10
# gacha system
def start_gacha():
    global current_cash
    first_num = randint(0, 9)
    second_num = randint(0, 9)
    third_num = randint(0, 9)
    print("The slot machine shows {0}{1}{2}".format(first_num, second_num, third_num))
    current_cash -= 0.25
        
    # all numbers are the same
    if (first_num == second_num) and (first_num == third_num): 
        print("You win the big prize, $10.00!")
        current_cash += 10
        print("You have ${0:.2f}.\nChoose one of the following menu options:".format(current_cash))
            
    # 2 out of 3 numbers are the same
    elif (first_num == second_num) or (first_num == third_num) or (second_num == third_num): 
        print("You win 50 cents!")
        current_cash += 0.5
        print("You have ${0:.2f}.\nChoose one of the following menu options:".format(current_cash))
            
    # all numbers are different
    else: 
        print("Sorry you dont' win anything.")
        print("You have ${0:.2f}.\nChoose one of the following menu options:".format(current_cash))

# save function
def save():
    print("Your money had saved!")

# quit funciton
def cash_out():
    print("Thank you for playing! You end with ${0:.2f}!".format(current_cash))

# menu interface
def menu():
    print("1) Play the slot machine.\n2) Save game. \n3) Cash out.")


# Start playing
print("You have ${0:.2f}.\nChoose one of the following menu options:".format(current_cash))
while True:
    if current_cash == 0:
        print("You have no money left.")
        break
    # get the menu up    
    menu()
    # Check if user didn't enter anything
    try:
        user_choice = int(input())
    except: 
        print("Error!")
        break
    # user choose to play
    if user_choice == 1: 
        start_gacha()
            
    # user choose to save
    elif user_choice == 2: 
        save()
        
    # user choose to leave
    elif user_choice == 3: 
        cash_out()
        break
    
    #check if user entered the wrong number
    else: 
        print("Wrong number! Please enter the correct number:")
