def square(x):
    return x*x

def get_numbers() -> list[int]:
    usr_input = input()
    nums = []
    for i in usr_input.split():
        if i == "q":
            break
        num = int(i)
        nums.append(num)
    return nums

def make_pairs(nums: list[int]) -> list[tuple[int, int]]:
    nums_pair = []
    for j in nums:
        nums_pair.append((j, square(j)))
    return nums_pair
        
def save_pairs(nums_pair: list[tuple[int, int]]):
    with open(path, "w") as file:
        for x, y in nums_pair:
            print(f"{x} {y}")
            file.write(f"{x} {y}")
    file.close


print("Enter list of numbers: ")
nums = get_numbers()
pairs = make_pairs(nums)
path = "D:/ml-roadmap/reports/results2.txt"
save_pairs(pairs)
