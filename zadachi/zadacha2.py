def main():

    name = input("Введіть своє ім'я: ")


    age = int(input("Введіть свій вік: "))


    print(f"Привіт, {name}!")


    if age > 18:
        print("Ти дорослий.")
    elif age == 18:
        print("Ти дорослий, але ще не дуже.")
    else:
        print("Ти ще дитина.")


if __name__ == "__main__":
    main()
