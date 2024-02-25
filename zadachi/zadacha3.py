def main():

    correct_password = "unicorn12"

    user_password = input("Введіть пароль: ")

    if user_password == correct_password:
        print("Пароль вірний")
    else:
        print("Пароль невірний")


if __name__ == "__main__":
    main()
