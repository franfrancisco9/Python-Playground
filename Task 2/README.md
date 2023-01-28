## TASK 2: Island in the Sun

### Preface
  * You can use whatever language you like.

### Description
In this task we'll try to solve an algorithmic challenge. 

Given a 2 dimensional array with n columns and n rows that contains random numbers between 0 and 4. 


You can use 

```python
In [0]: import numpy as np
In [1]: n = 10
In [2]: matrix = np.random.choice([x for x in range(0, 5)], n*n)
In [3]: matrix.resize(n, n)
In [4]: matrix
Out[0]: 
array([[1, 1, 3, 3, 1, 2, 0, 4, 2, 4],
       [2, 4, 0, 4, 3, 2, 0, 4, 4, 3],
       [1, 3, 2, 1, 0, 0, 0, 0, 0, 1],
       [1, 1, 3, 0, 2, 0, 0, 2, 3, 1],
       [2, 3, 1, 2, 3, 0, 4, 4, 1, 0],
       [0, 0, 2, 1, 0, 0, 3, 4, 1, 0],
       [1, 2, 0, 1, 0, 2, 0, 1, 4, 3],
       [0, 3, 3, 3, 3, 1, 3, 2, 1, 0],
       [4, 4, 4, 4, 0, 3, 2, 1, 2, 2],
       [1, 2, 4, 4, 3, 4, 3, 3, 4, 2]])
In [5]: 
```
to create the array.

### Task
Find the largest connected "island" in this matrix with the same numbers. Connected means connected to the north, west, south and east. 
First, we will display the random matrix and then we show the largest island. Everytime the script is executed, a new and random matrix is created.

### Example
```
user@maya:~$ ./find_island
1 1 3 3 1 2 0 4 2 4
2 4 0 4 3 2 0 4 4 3
1 3 2 1 0 0 0 0 0 1
1 1 3 0 2 0 0 2 3 1
2 3 1 2 3 0 4 4 1 0
0 0 2 1 0 0 3 4 1 0
1 2 0 1 0 2 0 1 4 3
0 3 3 3 3 1 3 2 1 0
4 4 4 4 0 3 2 1 2 2
1 2 4 4 3 4 3 3 4 2

. . . . . . X . . .
. . . . . . X . . .
. . . . X X X X X .
. . . . . X X . . .
. . . . . X . . . .
. . . . X X . . . .
. . . . X . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
```
