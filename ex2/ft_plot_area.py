def ft_plot_area() -> None:
    input_length: str = input("Enter length: ")
    input_width: str = input("Enter width: ")
    width: int = int(input_width)
    length: int = int(input_length)
    area: int = width * length
    print(f"Plot area: {area}")
