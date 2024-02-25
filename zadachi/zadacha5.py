def main():

    number1 = float(input("введіть перше число: "))

    number2 = float(input("введіть друге число: "))

    if number1 > number2:
        print(f"Більше число: {number1}")
    elif number2 > number1:
        print(f"Більше число: {number2}")
    else:
        print("Числа рівні.")


if __name__ == "__main__":
    main()
