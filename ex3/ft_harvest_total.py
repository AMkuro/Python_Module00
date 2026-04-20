def ft_harvest_total() -> None:
    total_harvest: int = 0
    day: int = 1
    while day <= 3:
        input_harvest: str = input(f"Day {day} harvest: ")
        harvest: int = int(input_harvest)
        total_harvest += harvest
        day += 1
    print(f"Total harvest: {total_harvest}")
