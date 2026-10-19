class GardenError(Exception):
    def __init__(self, default_message="Unknown plant error"):
        super().__init__(default_message)


class PlantError(GardenError):
    def __init__(self, default_message="Unknown plant error"):
        super().__init__(default_message)


class WaterError(GardenError):
    def __init__(self, default_message="Unknown plant error"):
        super().__init__(default_message)


def plant_error_test():
    raise PlantError("The tomato plant is wilting!")


def water_error_test():
    raise WaterError("Not enough water in the tank!")


def garden_error_test():
    raise GardenError()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    
    print("Testing PlantError...")
    try:
        plant_error_test()
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}\n")
        
    print("Testing WaterError...")
    try:
        water_error_test()
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}\n")
        
    print("Testing catching all garden errors...")
    try:
        plant_error_test()
    except GardenError as e:
        print(f"Caught {type(e).__name__}: {e}")
        
    try:
        water_error_test()
    except GardenError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

    print("All custom error types work correctly!")