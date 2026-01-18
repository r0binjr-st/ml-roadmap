def square(x):
    return x * x

while True:
    user_input = input("Enter number: ")
    try:
        num = int(user_input)
        break
    except ValueError:
        print("Input error, enter number")
        continue

print(f"Square of {num} = {square(num)}")
