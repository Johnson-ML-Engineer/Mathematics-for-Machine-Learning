row1=int(input("Enter the no of rows in matrix1 :"))
column1=int(input("Enter the no of columns in matrix1 :"))
print(f"Enter {column1*row1} elements in matrix1 ")
matrix1=[[int(input()) for j in range(column1)] for i in range(row1) ]

row2=int(input("Enter the no of rows in matrix2 :"))

if column1==row2:
    column2=int(input("Enter the no of columns in matrix2 :"))
    print(f"Enter {column2*row2} elements in matrix2 ")
    matrix2=[[int(input()) for j in range(column2)] for i in range(row2)]
else:
    print(f"number of columns({column1}) in matrix1 and rows({row2}) in matrix2 are not same \n we cannot do multiplication in such case")
    exit()
matrix_multiplication=[[sum(matrix1[i][k]*matrix2[k][i] for k in range(column1))] for i in range(row1)]
print("Multiplication of two matrices \n",matrix_multiplication)