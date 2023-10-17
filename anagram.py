def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters in both strings are the same
    return sorted(str1) == sorted(str2)

result = are_anagrams("listen", "silent")
print(result)  # This will print True

result = are_anagrams("Milk", "Food")
print(result)  # This will print False
