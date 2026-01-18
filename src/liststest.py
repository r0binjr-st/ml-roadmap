def square(x):
    return x*x


user_input = input("Enter list of numbers: ")

nums = []
for i in user_input.split():
    if i == "q":
        break
    num = int(i)
    nums.append(num)
    nums.append(square(num))
    
with open("D:/ml-roadmap/reports/results1.txt", "w") as file:
    for b in range(0, len(nums), 2):
        file.write(f"{nums[b]} {nums[b+1]}\n")
    file.close
