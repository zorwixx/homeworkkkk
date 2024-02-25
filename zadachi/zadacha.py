def main():

    length = float(input("Введіть довжину прямокутника: "))
    width = float(input("Введіть ширину прямокутника: "))

    area = length * width

    perimeter = 2 * (length + width)

    print(f"Площа прямокутника: {area}")
    print(f"Периметр прямокутника: {perimeter}")


if __name__ == "__main__":
    main()
