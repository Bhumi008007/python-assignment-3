import math

# Ask the user for a number
try:
    number = float(input("Enter a positive number: "))

    if number <= 0:
        print("Please enter a number greater than 0 for logarithm and square root.")
    else:
        # Calculate results
        square_root = math.sqrt(number)
        natural_log = math.log(number)  # log base e
        sine_value = math.sin(number)   # in radians

        # Display the results
        print(f"Square root of {number}: {square_root}")
        print(f"Natural logarithm (ln) of {number}: {natural_log}")
        print(f"Sine of {number} radians: {sine_value}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
