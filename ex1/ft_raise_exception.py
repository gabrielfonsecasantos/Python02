def input_temperature(temp_str: str) -> None:
    if int(temp_str) < 0:
        raise ValueError(f"Caught input_temperature error: "
                         f"{temp_str}°C is too cold for plants (min 0°C)")
    elif int(temp_str) > 40:
        raise ValueError(f"Caught input_temperature error: "
                         f"{temp_str}°C is too hot for plants (max 40°C)")
    else:
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
        print(f"Input data is '{input}'")
        input_temperature(input)
        print(f"Temperature is now {input}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        input = "100"
        print(f"Input data is '{input}'")
        input_temperature(input)
        print(f"Temperature is now {input}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        input = "-50"
        print(f"Input data is '{input}'")
        input_temperature(input)
        print(f"Temperature is now {input}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All testes completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
