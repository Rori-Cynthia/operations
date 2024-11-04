def add(first_number: int, second_number: int) -> int:
    return first_number + second_number


def subtract(first_number: int, second_number: int) -> int:
    return first_number - second_number


def multiply(first_number: int, second_number: int) -> int:
    return first_number * second_number


def divide(first_number: int, second_number: int) -> int:
    return first_number / second_number


def calculate(first_number: int, second_number: int) -> dict:
    results = {
        "Suma": add(first_number, second_number),
        "Resta": subtract(first_number, second_number),
        "Multiplicación": multiply(first_number, second_number),
        "División": divide(first_number, second_number),
    }
    return results


def run():
    while True:
        try:
            first_number = int(input("Ingrese el primer número: "))
            second_number = int(input("Ingrese el segundo número: "))

            results = calculate(first_number, second_number)
            print(results)

        except ValueError:
            print("Entrada inválida, por favor, solo ingrese números enteros.")


if __name__ == "__main__":
    run()