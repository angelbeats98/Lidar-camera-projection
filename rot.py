import numpy as np

# 定义一个行向量
row_vector = np.array([1, 2, 3])

# 使用transpose函数将行向量转置为列向量
column_vector = np.transpose(row_vector)

print(column_vector)