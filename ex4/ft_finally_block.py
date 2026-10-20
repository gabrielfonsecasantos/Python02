class GardenError(Exception):
    def __init__(self, default_message="Unknown plant error"):
        super().__init__(default_message)


class PlantError(GardenError):
    def __init__(self, default_message="Unknown plant error"):
        super().__init__(default_message)


def water_plant(plant_name: str):
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name.capitalize()}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list):
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid parameters...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("Testing invalid parameters...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print("Cleanup always happens, even with errors!")