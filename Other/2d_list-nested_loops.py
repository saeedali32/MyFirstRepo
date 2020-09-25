number_grid = [  #2d list 
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]

#  print(number_grid[0][0])  #[Which List][Which item]

for row in number_grid: #nested for loop 
    for col in row:
        print(col)
