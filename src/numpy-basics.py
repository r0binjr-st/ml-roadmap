import numpy as np

def square(x: int) -> int:
    return x*x

def read_file(path_r) -> list[int]:
    with open(path_r, "r") as file_r:
        nums = []
        for line in file_r:
            for i in line.split():
                if i == "q":
                    break
                num = int(i)
                nums.append(num)
        return nums

def make_pairs(nums: list[int]) -> np.ndarray:
    arr = np.array(nums)
    squares = square(arr)
    nums_pair = np.column_stack((arr, squares))
    return(nums_pair)

def save_pairs(nums_pair: np.ndarray):
    with open(path_w, "w") as file:
        for x, y in nums_pair:
            print(f"{x} {y}")
            file.write(f"{x} {y}\n")
    file.close

path_r = "D:/ml-roadmap/data/input_numbers1.txt"
path_w = "D:/ml-roadmap/reports/results3.txt"
nums = read_file(path_r)
pairs = make_pairs(nums)
save_pairs(pairs)
print("\nDone")

