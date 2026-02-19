def ft_count_harvest_recursive() -> None:
    days_until_harvest: int = int(input("Days until harvest: "))

    def helper(day: int, end_day: int) -> None:
        if day > end_day:
            return
        print(f"Day {day}")
        helper(day + 1, end_day)

    helper(1, days_until_harvest)
    print("Harvest time!")
