#!/usr/bin/env python3

"""
Helper file for Growing Code.

This file helps you test your exercises easily.
Just run: python3 main.py

How it works:
1. It tries to import your exercise files (like ft_plot_area.py)
2. It calls your functions to test them
3. If there's an error, it tells you what went wrong

Your exercise files can be in the same folder as this main.py file,
or in subfolders (the tester will search recursively).
"""

import importlib.util
import os
import sys
from pathlib import Path
from typing import Optional


_SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "env", ".mypy_cache", ".pytest_cache"}


def _find_exercise_path(exercise_file_name: str) -> Optional[Path]:
    """Find `<exercise_file_name>.py` under the main.py folder (recursive)."""
    root = Path(__file__).resolve().parent
    target_file = f"{exercise_file_name}.py"

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in _SKIP_DIRS]
        if target_file in filenames:
            return (Path(dirpath) / target_file).resolve()

    return None


def _import_module_from_path(module_basename: str, module_path: Path):
    """Import a python file by path and return the loaded module."""
    module_name = f"_growing_code_{module_basename}"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not import from path: {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_ft_exercise(exercise_file_name):
    """
    This function tries to run one of your exercises.

    For example: test_ft_exercise("ft_plot_area") will:
    - Look for a file called ft_plot_area.py
    - Import it
    - Call the function ft_plot_area() inside it
    """
    print(f"\n=== Testing {exercise_file_name} ===")

    try:
        exercise_path = _find_exercise_path(exercise_file_name)
        if exercise_path is None:
            raise ImportError(
                f"Could not find {exercise_file_name}.py under {Path(__file__).resolve().parent}"
            )

        # Import your exercise file from its path (supports subfolders)
        ft_module = _import_module_from_path(exercise_file_name, exercise_path)
        print(f"Loaded from: {exercise_path.relative_to(Path(__file__).resolve().parent)}")

        # Get the function from your file
        # This is like doing: ft_plot_area.ft_plot_area
        ft_function = getattr(ft_module, exercise_file_name)

        # Special handling for ft_seed_inventory (Exercise 7)
        # This function takes parameters, unlike the others
        if exercise_file_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            # Test with packets
            ft_function("tomato", 15, "packets")
            # Test with grams
            ft_function("carrot", 8, "grams")
            # Test with area
            ft_function("lettuce", 12, "area")
            # Test with unknown unit
            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            # Run your function normally (no parameters)
            ft_function()

    except ImportError as error:
        print(f"❌ Could not load {exercise_file_name}.py")
        print(f"   {error}")
        print("   Make sure your file exists in this folder or any subfolder.")

    except AttributeError:
        print(f"❌ Could not find function {exercise_file_name}() in your file")
        print(f"   Make sure you have: def {exercise_file_name}():")

    except TypeError as error:
        msg = str(error)
        if "missing" in msg and "required positional argument" in msg:

            print(f"❌ Function signature error: {error}")
            print(
                """   For exercise 7, make sure your
                function takes parameters:"""
            )
            print(
                f"   def {exercise_file_name}"
                "(seed_type: str, quantity: int, unit: str) -> None:"
            )
        else:
            print(f"❌ Type error: {error}")
            print("   Check your function parameters and types")

    except Exception as error:
        print(f"❌ Error running your function: {error}")
        print("   Check your code for syntax errors")


def main():
    """Run main function - this runs when you execute: python3 main.py ."""
    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises for you.")
    print("\nWhich exercise would you like to test?")
    print()
    print("0 - ft_hello_garden     (Say hello to the garden community)")
    print("1 - ft_plot_area        (Calculate garden plot area)")
    print("2 - ft_harvest_total    (Add up harvest weights)")
    print("3 - ft_plant_age        (Check if plant is ready)")
    print("4 - ft_water_reminder   (Check if plants need water)")
    print("5 - ft_count_harvest    (Count days to harvest)")
    print("6 - ft_garden_summary   (Display garden info)")
    print("7 - ft_seed_inventory    (Seed inventory with type hints)")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ")

    # Test the exercise based on user choice
    if choice == "0":
        test_ft_exercise("ft_hello_garden")
    elif choice == "1":
        test_ft_exercise("ft_plot_area")
    elif choice == "2":
        test_ft_exercise("ft_harvest_total")
    elif choice == "3":
        test_ft_exercise("ft_plant_age")
    elif choice == "4":
        test_ft_exercise("ft_water_reminder")
    elif choice == "5":
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
    elif choice == "6":
        test_ft_exercise("ft_garden_summary")
    elif choice == "7":
        test_ft_exercise("ft_seed_inventory")
    elif choice == "a":
        # Test all exercises one by one
        test_ft_exercise("ft_hello_garden")
        test_ft_exercise("ft_plot_area")
        test_ft_exercise("ft_harvest_total")
        test_ft_exercise("ft_plant_age")
        test_ft_exercise("ft_water_reminder")
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
        test_ft_exercise("ft_garden_summary")
        test_ft_exercise("ft_seed_inventory")
    else:
        print("❌ Invalid choice! Please enter 0, 1, 2, 3, 4, 5, 6, 7, or a")


# This line means: "If someone runs this file directly, call main()"
# You don't need to understand this yet, just know it makes the program start
if __name__ == "__main__":
    main()
