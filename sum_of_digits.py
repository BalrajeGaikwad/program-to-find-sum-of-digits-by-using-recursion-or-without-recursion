"""def sum_of_digits_non_recursive(n):
    total = 0
    while n > 0:
        total += n % 10  # Extract the last digit
        n //= 10  # Remove the last digit
    return total

# Input from the user
number = int(input("Enter a 5-digit number: "))

# Ensure the input is a 5-digit number
if 10000 <= number <= 99999:
    print(f"The sum of the digits of {number} is: {sum_of_digits_non_recursive(number)}")
else:
    print("Please enter a valid 5-digit number.")"""





def sum(n):
    total=0
    while n > 0:
        total+=n%10
        n//=10
    return total

num=int(input("Enter the 5 number : "))
print(sum(num))


