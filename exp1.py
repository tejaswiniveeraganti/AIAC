# Multiplication Table Code 1: Without Function
def print_multiplication_table_without_function():
    print("=" * 50)
    print("Multiplication Tables (1-30) - Without Function")
    print("=" * 50)
    
    for i in range(1, 31):
        print(f"\nMultiplication Table of {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")


# Multiplication Table Code 2: Using Function
def print_table(num):
    """Function to print multiplication table for a given number"""
    for j in range(1, 11):
        print(f"{num} x {j} = {num * j}")

def print_multiplication_table_with_function():
    print("\n" + "=" * 50)
    print("Multiplication Tables (1-30) - With Function")
    print("=" * 50)
    
    for i in range(1, 31):
        print(f"\nMultiplication Table of {i}:")
        print_table(i)


if __name__ == "__main__":
    # Run both multiplication table codes
    print_multiplication_table_without_function()
    print_multiplication_table_with_function()

