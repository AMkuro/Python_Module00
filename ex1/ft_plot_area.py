def ft_plot_area() -> None:
    input_width: str = input("Enter the width of the plot: ")
    input_length: str = input("Enter the length of the plot: ")
    width: int = int(input_width)
    length: int = int(input_length)
    area: int = width * length
    print(f"Plot area: {area}")
