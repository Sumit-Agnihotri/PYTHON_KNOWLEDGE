# Example 4: Using % Operator

# We can use ‘%’ operator. % values are replaced with zero or more value of elements. The formatting using % is similar to that of ‘printf’ in the C programming language.

# %d –integer
# %f – float
# %s – string
# %x –hexadecimal
# %o – octal

# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)