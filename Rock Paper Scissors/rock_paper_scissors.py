import random

emojis = { 'r': '🪨', 'p': '📄', 's': '✂️' }
choices = ('r','p','s')

while True :
    user_choice = input( "Choose Rock,Paper,Scissors ? (r/p/s): ").lower()
    if user_choice not in choices :
        print("Invalid input.Please choose again.")
        continue

    computer_choice = random.choice(choices)
    print(f'You choose {emojis[user_choice]}')
    print(f'Computer choose {emojis[computer_choice]}')

    if user_choice == computer_choice :
        print("Tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's') or\
        (user_choice == 's' and computer_choice == 'p') or\
        (user_choice == 'p' and computer_choice == 'r')) :
      print("You win!")
    else :
        print("You lose.")

    should_continue  = input('Continue? (y/n): ').lower()
    if should_continue == 'n' :
        break  