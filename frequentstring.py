def most_frequent_character(input_string):
    # Create a dictionary to store character frequencies
    char_frequency = {}

    # Iterate through the string and update character frequencies
    for char in input_string:
        if char.isalpha():  # Ignore non-alphabet characters
            char = char.lower()  # Consider characters as case-insensitive
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

    # Find the character with the highest frequency
    most_frequent_char = max(char_frequency, key=char_frequency.get)
    return most_frequent_char

# Input:
input_string = "Hello, World!"
result = most_frequent_character(input_string)
print(f"The most frequent character in '{input_string}' is '{result}'.")
