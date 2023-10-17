n = 20  # The number of rows in the pyramid

for i in range(1, n + 1):
    # Print spaces for alignment
    for j in range(n - i):
        print(" ", end=" ")
    
    # Print numbers in ascending order
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print numbers in descending order
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    
    # Move to the next line for the next row
    print()
