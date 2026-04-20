def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    result: str = ""
    if unit == "packets":
        result = f"{quantity} packets available"
    elif unit == "grams":
        result = f"{quantity} grams total"
    elif unit == "area":
        result = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: {result}")
