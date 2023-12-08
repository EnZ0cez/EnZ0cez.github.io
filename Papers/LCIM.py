import random

# 设置生成的序列数量
num_sequences = 4000

# 设置物品的编号范围和每个序列中物品的数量范围
item_range = list(range(1, 101))
num_items_range = list(range(2, 31))

# 设置 cost 和 utility 的范围
cost_range = list(range(5, 1001))
utility_range = list(range(2, 51))

# 生成序列
sequences = []
for _ in range(num_sequences):
    num_items = random.choice(num_items_range)
    items = random.sample(item_range, num_items)
    cost = random.choice(cost_range)
    utilities = [random.choice(utility_range) for _ in range(num_items)]

    sequence = f"{ ' '.join(map(str, items))}:{cost}:{' '.join(map(str, utilities))}"
    sequences.append(sequence)

# 将生成的序列写入文件
with open('generated_sequences.txt', 'w') as file:
    for sequence in sequences:
        file.write(sequence + '\n')

print(f"{num_sequences} sequences generated and saved in 'generated_sequences.txt'.")
