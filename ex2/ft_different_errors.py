def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        res = 10 / 0
        print(res)
    elif operation_number == 2:
        open("sample.txt")

    elif operation_number == 3:
        res = "1" + 1
        print(res)
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")

    for i in range(0, 4):
        try:
            print(f"Testing operation {i}")
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
