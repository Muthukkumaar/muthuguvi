def is_palindrome(input_str):
    # Remove spaces and convert the string to lowercase for case-insensitive comparison
    cleaned_str = ''.join(input_str.split()).lower()
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]

#Input
print(is_palindrome("Malayalam"))
