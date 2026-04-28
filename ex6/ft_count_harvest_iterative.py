def ft_count_harvest_iterative() -> None:
    count_harvest: int = int(input("Days until harvest: "))
    for i in range(1, count_harvest + 1):
        print(f"Day {i}")
    print("Harvest time!")
