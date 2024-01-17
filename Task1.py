def reverse_string(string_input):
    string_reversed = ""
    for char in string_input:
        string_reversed= char + string_reversed
    return string_reversed

# Get user input
string_input = input("Enter a string: ")

# Call the function and print the result
print("Reversed string: ", reverse_string(string_input))