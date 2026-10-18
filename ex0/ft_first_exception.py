def input_temperature(temp_str: str) -> None:
    return int(temp_str)


def test_temperature():
    print("=== Garden Temperature ===\n")
    try:
        input = "25"
        print(f"Input data is '{input}'")
        input_temperature(input)
        print(f"Temperature is now {input}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        input = "abc"
        input_temperature(input)
        print(f"Temperature is now {input}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All testes completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
