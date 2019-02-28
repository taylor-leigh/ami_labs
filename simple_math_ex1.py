# init
first_number = ""
second_number = ""

# welcome message
print("Hi, I will sum two integer numbers...")

# insert the first number; if not an integer, ask again
while not first_number.isdigit():
    first_number = input("Please, insert a number: ")

# insert the second number; if not an integer, ask again
while not second_number.isdigit():
    second_number = input("Now, insert another number: ")

# perform the sum
result = int(first_number) + int(second_number)

print(first_number, "+", second_number, "is equal to", result)
