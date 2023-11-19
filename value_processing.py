def processing_options():
    value1 = input("Введіть перше значення: ")
    value2 = input("Введіть друге значення: ")

    try:
        result = float(value1) + float(value2)
    except ValueError:
        result = value1 + value2

    return result


if __name__ == "__main__":
    output = processing_options()
    print("Результат:", output)
