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

def make_stats(nums: list[int]) -> dict[str, float]:
    arr = np.array(nums)
    stats = {'min': int(np.min(arr)), 
            'max': int(np.max(arr)),
            'mean': float(np.mean(arr)),
            'std': float(np.std(arr))}
    return(stats)

def save_stats(make_stats: dict[str, float]):
    with open(path_w, "w") as file:
        for key, value in make_stats.items():
            print(key, value)
            file.write(f"{key} {value}\n")

path_r = "D:/ml-roadmap/data/input_numbers1.txt"
path_w = "D:/ml-roadmap/reports/stats1.txt"
nums = read_file(path_r)
stats = make_stats(nums)
save_stats(stats)
print("Done!")

