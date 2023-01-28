import numpy as np

SIZE = 10

MATRIX = np.random.choice([x for x in range(0, 5)], SIZE * SIZE).reshape(SIZE, SIZE)

MATRIX.resize(SIZE, SIZE)

print(MATRIX)

