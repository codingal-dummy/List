# Input range from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Generate square values
squares = [num ** 2 for num in range(start, end + 1)]

# Separate even and odd square values
even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

# Display results
print("\nSquare Values:")
print(squares)

print("\nEven Square Values:")
print(even_squares)

print("\nOdd Square Values:")
print(odd_squares)