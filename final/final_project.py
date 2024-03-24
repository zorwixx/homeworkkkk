import random

def game():
    print("Виберіть: 1 - камінь, 2 - ножиці, 3 - папір")
    user_choice = int(input("Ваш вибір: "))
    computer_choice = random.randint(1, 3)

    if user_choice == computer_choice:
        print("Нічия!")
    elif user_choice == 1 and computer_choice == 2 or \
         user_choice == 2 and computer_choice == 3 or \
         user_choice == 3 and computer_choice == 1:
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг((")

while True:
    game()
    play_again = input("Хочете зіграти ще раз? (так/ні): ")
    if play_again.lower() != 'так':
        break
