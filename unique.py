def count_unique_characters(input_string):
    # Initialize an empty set to store unique characters
    unique_chars = set()

    # Iterate through the characters in the input string
    for char in input_string:
        # Add the character to the set
        unique_chars.add(char)

    # Return the count of unique characters in the set
    return len(unique_chars)

# Example Input:
input_str = "muthukkumaar"
result = count_unique_characters(input_str)
print(f"The number of unique characters in '{input_str}' is {result}.")
